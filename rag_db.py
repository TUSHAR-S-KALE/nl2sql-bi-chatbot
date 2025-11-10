import chromadb
from sentence_transformers import SentenceTransformer
from sqlalchemy import inspect
from example_queries import examples
from example_codes import plot_examples

#Create/connect to a Chroma DB
chroma_client = chromadb.Client()

schema_collection = chroma_client.get_or_create_collection("schema_store")
examples_collection = chroma_client.get_or_create_collection("examples_store")
plot_examples_collection = chroma_client.get_or_create_collection("plot_examples_store")

#Loading the embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def build_knowledge(engine):
  inspector = inspect(engine)
  tables = inspector.get_table_names()

  #Stores schema
  schema_docs = []
  schema_metas = []
  schema_ids = []

  for table in tables:
    columns = inspector.get_columns(table)
    col_info = ", ".join([f"{c['name']} ({c['type']})" for c in columns])
    text = f"Table {table} with columns: {col_info}"
    schema_docs.append(text)
    schema_metas.append({"table": table})
    schema_ids.append(table)

  schema_embeddings = embedder.encode(schema_docs).tolist()
  schema_collection.add(
    documents=schema_docs,
    embeddings=schema_embeddings,
    metadatas=schema_metas,
    ids=schema_ids
  )
  print(f"✅ Added {len(tables)} tables to schema vector store.")

  #Stores example SQL queries
  for i, ex in enumerate(examples):
    embedding = embedder.encode(ex["user_input"]).tolist()
    examples_collection.add(
      ids=[f"example_{i}"],
      embeddings=[embedding],
      documents=[ex["user_input"]],
      metadatas=[{"sql": ex["sql"]}]
    )
  print(f"✅ Added {len(examples)} SQL examples to example vector store.")

  #Stores example graph codes
  for i, ex in enumerate(plot_examples):
    embedding = embedder.encode(ex["User request"]).tolist()
    plot_examples_collection.add(
      ids=[f"plot_example_{i}"],
      embeddings=[embedding],
      documents=[ex["code"]],
      metadatas=[{"User request": ex["User request"]}]
    )
  print(f"✅ Added {len(plot_examples)} plotting examples to vector store.")

#Retrieves relevant schema based on user prompt
def retrieve_relevant_schema(prompt: str, top_k=3):
  query_emb = embedder.encode([prompt]).tolist()[0]
  results = schema_collection.query(query_embeddings=[query_emb], n_results=top_k)
  return "\n".join(results["documents"][0])

#Retrieves relevant SQL query examples based on user prompt
def retrieve_relevant_examples(prompt: str, top_k=3):
  query_emb = embedder.encode([prompt]).tolist()[0]
  results = examples_collection.query(query_embeddings=[query_emb], n_results=top_k)
  documents = results["documents"][0]
  metadatas = results["metadatas"][0]

  combined_docs = []
  for doc, meta in zip(documents, metadatas):
    combined_docs.append(f"User Query: {doc}\nSQL: {meta['sql']}")
  return "\n\n".join(combined_docs)

#Retrieves relevant plot code examples based on user prompt
def retrieve_relevant_plot_examples(prompt: str, top_k=3):
  query_emb = embedder.encode([prompt]).tolist()[0]
  results = plot_examples_collection.query(query_embeddings=[query_emb], n_results=top_k)
  codes = results["documents"][0]
  metas = results["metadatas"][0]

  combined_docs = []
  for code, meta in zip(codes, metas):
    combined_docs.append(f"User Request: {meta['User request']}\nCode:\n{code}")
  return "\n\n".join(combined_docs)