import streamlit as st
import pandas as pd
from utils import db_conn, ChatMemory
from sqlalchemy import inspect, text
from llm import agent_run
from io import BytesIO

st.set_page_config(page_title="BI Analyst", page_icon="💬", layout="wide")

#Session States
if "db_engine" not in st.session_state:
  st.session_state["db_engine"] = None
if "messages" not in st.session_state:
  st.session_state["messages"] = []
if "uploaded_data" not in st.session_state:
  st.session_state["uploaded_data"] = None
if "graphs" not in st.session_state:
  st.session_state["graphs"] = []
if "memory" not in st.session_state:
  st.session_state["memory"] = ChatMemory()

#Sidebar
st.sidebar.header("🗂️ Data Source")

data_source = st.sidebar.radio(
  "Select a data source:",
  ["Connect to PostgreSQL", "Upload CSV/Excel", "Display tables in the database"]
)

data = None

if data_source == "Connect to PostgreSQL":
  st.sidebar.subheader("PostgreSQL Connection")
  host = st.sidebar.text_input("Host")
  port = st.sidebar.text_input("Port")
  database = st.sidebar.text_input("Database")
  user = st.sidebar.text_input("User")
  password = st.sidebar.text_input("Password", type="password")
  connect_btn = st.sidebar.button("Connect")

  if connect_btn:
    try:
      st.session_state["db_engine"] = db_conn(host, port, database, user, password)
      st.sidebar.success("✅ Connection established")
    except Exception as e:
      st.sidebar.error(f"Failed {e}")

elif data_source == "Upload CSV/Excel":
  uploaded_file = st.sidebar.file_uploader("Upload a file", type=["csv", "xlsx"])
  if uploaded_file:
    try:
      #Reading uploaded file
      if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
      else:
        data = pd.read_excel(uploaded_file)

      st.session_state["uploaded_data"] = data
      st.sidebar.success("✅ File uploaded successfully!")

      st.sidebar.write("Preview:")
      st.sidebar.dataframe(data.head())

      table_name = st.sidebar.text_input("📝 Enter table name for insertion:")

      #Inserting the data into PostgreSQL
      if st.sidebar.button("⬆️ Insert into Database"):
        if not st.session_state["db_engine"]:
          st.sidebar.error("⚠️ Please connect to the PostgreSQL database first.")
        elif not table_name:
          st.sidebar.warning("⚠️ Please enter a valid table name.")
        else:
          try:
            data.to_sql(table_name, st.session_state["db_engine"], index=False, if_exists="fail")
            st.sidebar.success(f"✅ Data inserted successfully into table '{table_name}'.")
          except ValueError:
            st.sidebar.error(f"❌ Table '{table_name}' already exists. Try a different name.")
          except Exception as e:
            st.sidebar.error(f"❌ Failed to insert data: {e}")
    except Exception as e:
      st.sidebar.error(f"❌ Error reading file: {e}")

#Displaying availabe tables in the database
elif data_source == "Display tables in the database":
  if not st.session_state["db_engine"]:
    st.sidebar.warning("⚠️ Database is not connected.")
  else:
    engine = st.session_state["db_engine"]
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    st.sidebar.subheader("Tables in Database:")
    for table in tables:
      cols = st.sidebar.columns([0.3, 0.7])  # small column for X icon
      if cols[0].button("❌", key=f"delete_{table}"):
        try:
          with engine.begin() as conn:
            conn.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE"))
          st.sidebar.success(f"✅ Table '{table}' deleted successfully.")
          st.rerun()
        except Exception as e:
          st.sidebar.error(f"❌ Failed to delete '{table}': {e}")
      cols[1].write(table)

#Chat memory management
st.sidebar.subheader("Memory Management")

if st.sidebar.button("🗑️ Clear Memory"):
  #reinitialize memory
  st.session_state["memory"] = ChatMemory()
  st.sidebar.success("✅ Memory cleared successfully")
  st.rerun()

#MAIN CHAT INTERFACE
st.title("💬 BI Analyst")

st.markdown("""
Ask questions related to your data or connected database.
""")

#Displaying previous chat messages
for msg in st.session_state.messages:
  with st.chat_message(msg["role"]):
    if msg["role"] == "assistant" and msg["solution"] != "":
      with st.expander("See generated solution", expanded=False):
        st.code(msg["solution"])
    st.markdown(msg["content"])
    if "graph" in msg and msg["graph"] is not None:
      msg["graph"].seek(0)
      st.image(msg["graph"], width=700)

#User input
user_input = st.chat_input("Type your message here...")

#Displaying user input
if user_input:
  st.chat_message("user").markdown(user_input)
  st.session_state.messages.append({"role": "user", "content": user_input})

  #Displaying assistant response
  with st.chat_message("assistant"):
    with st.spinner("Thinking..."):
      response = agent_run(user_input, st.session_state, stream=True)

    solution = response["solution"]
    answer = response["output"]
    fig = response["graph"]

    if solution != "":
      with st.expander("See generated solution", expanded=False):
        st.code(solution)
    #st.markdown(answer)

    if fig is not None:
      st.session_state["graphs"].append(fig)

      # Resize figure dynamically
      image_width = 700
      image_height = 400

      fig.set_size_inches(image_width / 100, image_height / 100)  # adjust figure size in inches

      # Display in Streamlit
      buf = BytesIO()
      fig.tight_layout()
      fig.savefig(buf, format="png", dpi=100)
      buf.seek(0)
      st.image(buf, width=image_width)

  st.session_state.messages.append({
    "role": "assistant",
    "solution": solution,
    "content": answer,
    "graph": buf if response["graph"] is not None else None
  })

  #print(st.session_state["memory"].get_history_text(limit=10))
