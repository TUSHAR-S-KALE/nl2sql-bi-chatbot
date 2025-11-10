import pandas as pd
import streamlit as st

from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_community.tools.sql_database.tool import QuerySQLCheckerTool
from langchain_community.utilities import SQLDatabase

from prompts import *
from helper_functions import *
from rag_db import retrieve_relevant_schema, retrieve_relevant_examples, retrieve_relevant_plot_examples

#Initializing LLMs
code_llm = OllamaLLM(model="codellama", temperature=0)
nlg_llm = OllamaLLM(model="mistral:7b-instruct", temperature=0.3)

#Function definition for streaming response/tokens as they arrive
def stream_llm_response(llm, prompt):
  stream = llm.stream(prompt)
  response_text = ""
  for chunk in stream:
    if isinstance(chunk, dict):
      delta = chunk.get("message", {}).get("content", "")
    else:
      delta = str(chunk)
    yield delta
  return response_text

#Main BI Pipeline
def agent_run(prompt, session_state, allow_write_queries: bool = False, stream=False):
  memory_context = ""
  if "memory" in session_state:
    memory_context = session_state["memory"].get_history_text(limit=5)

  session_state["memory"].add_user_message(prompt)

  #Classify the task (SQL_QUERY / PLOT / Other)
  classify_prompt = PromptTemplate(
    input_variables=["prompt"],
    template=CLASSIFIER_PROMPT
  )
  task_type = (classify_prompt | nlg_llm).invoke({"prompt": prompt}).strip().upper()
  print(f"[DEBUG] Task type: {task_type}")

  #Handles prompts suuch as greetings or any random questions
  if task_type not in ["SQL_QUERY", "PLOT"]:
    response_container = st.empty()
    partial_text = ""
    for delta in stream_llm_response(nlg_llm, f"{memory_context}\nUser: {prompt}"):
      partial_text += delta
      response_container.markdown(partial_text + "▌")
    response_container.markdown(partial_text)
    
    session_state["memory"].add_ai_message(partial_text, None, None)
    return {"solution": "", "output": partial_text, "graph": None}


  #SQL Query Generation
  elif task_type in ["SQL_QUERY", "PLOT"]:
    sql_query, df, graph_plot = None, None, None
    engine = session_state.get("db_engine")

    #Checking for db engine and fetching the db schema and relevant examples based on the user query
    if engine:
      try:
        schema = retrieve_relevant_schema(prompt, top_k=3)
        examples = retrieve_relevant_examples(prompt, top_k=1)
        print(f"[DEBUG]: RELEVANT EXAMPLES: {examples}")
      except Exception as e:
        schema = f"Schema introspection failed: {e}"
    else:
      response_container = st.empty()
      response_container.markdown("⚠️ Connect to a database first.")
      return {"solution": "", "output": "⚠️ Connect to a database first.", "graph": None}

    sql_prompt = PromptTemplate(
      input_variables=["prompt", "schema", "memory", "examples"],
      template=SQL_QUERY_GEN_PROMPT
    )

    sql_chain = sql_prompt | code_llm
    raw_sql_output = sql_chain.invoke({
      "prompt": prompt,
      "schema": schema,
      "memory": memory_context,
      "examples": examples
    })
    print(f"[DEBUG] Raw SQL Query: {raw_sql_output}")
    sql_query = extract_sql_query(raw_sql_output)
    print(f"[DEBUG] Extracted SQL:\n{sql_query}")
    #db = SQLDatabase(engine)
    #sql_query = QuerySQLCheckerTool(db=db, llm=code_llm).invoke({"query": sql_query})
    #print(f"[DEBUG] Checked SQL Query: {sql_query}")

    #Risky SQL Query Detection
    if sql_query and is_sql_risky(sql_query):
      if not allow_write_queries:
        warning_msg = (
          "⚠️ The generated SQL query contains operations that may modify or delete data "
          "(e.g., ALTER, DELETE, UPDATE, INSERT, DROP, etc.).\n"
          "Execution refused due to read-only mode.\n"
          "If this operation is intentional, please enable write mode manually."
        )
        return {"solution": sql_query, "output": warning_msg, "graph": None}

    if sql_query:
      df = run_sql_query(sql_query, engine)
      print(f"DATAFRAME:\n{df}")
    else:
      df = pd.DataFrame({"error": ["No valid SQL query extracted."]})
  
    #Natural Language Output
    nlg_prompt = PromptTemplate(
      input_variables=["prompt", "df", "memory"],
      template=NLG_PROMPT
    )
    response_container = st.empty()
    partial_nlg = ""

    stream = nlg_llm.stream(
      nlg_prompt.format(prompt=prompt, df=df.to_dict(), memory=memory_context)
    )
    for chunk in stream:
      if isinstance(chunk, dict):
        delta = chunk.get("message", {}).get("content", "")
      else:
        delta = str(chunk)
      if delta:
        partial_nlg += delta
        response_container.markdown(partial_nlg + "▌")

    response_container.markdown(partial_nlg)
    natural_output = partial_nlg

    #Graph code generation
    if task_type == "PLOT" and isinstance(df, pd.DataFrame) and "error" not in df.columns:
      plot_context = retrieve_relevant_plot_examples(prompt, top_k=1)
      print("[DEBUG] Retrieved Plot Context:\n", plot_context)
      graph_prompt = PromptTemplate(
        input_variables=["prompt", "plot_context"],
        template=GRAPH_CODE_GEN_PROMPT
      )
      graph_chain = graph_prompt | code_llm
      raw_graph_code = graph_chain.invoke({"prompt": prompt, "plot_context": plot_context})
      print(f"[DEBUG] Raw Graph Code:\n{raw_graph_code}")
      clean_graph_code = extract_python_code(raw_graph_code)
      print(f"[DEBUG] Cleaned Graph Code:\n{clean_graph_code}")
      try:
        graph_plot = run_graph_code(clean_graph_code, df)
      except Exception as e:
        df = pd.DataFrame({"error": [f"Graph execution failed: {e}"]})

  session_state["memory"].add_ai_message(
    natural_output,
    sql_query,
    df
  )

  return {"solution": sql_query or "", "output": natural_output, "graph": graph_plot}
