from sqlalchemy import create_engine
import pandas as pd
from rag_db import build_knowledge

from sqlalchemy import create_engine

def db_conn(host, port, database, user, password):
  engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
  build_knowledge(engine)
  try:
    with engine.connect() as conn:
      pass
    return engine
  except Exception as e:
    raise ConnectionError(f"Database connection failed: {e}")

class ChatMemory:
  def __init__(self):
    self.buffer = []

  def add_user_message(self, message):
    self.buffer.append({"role": "user", "content": message})

  def add_ai_message(self, message: str, sql_query: str = None, df: pd.DataFrame = None):
    entry = {"role": "assistant", "content": message}

    if sql_query is not None:
      entry["sql_query"] = sql_query

    if df is not None:
      entry["df"] = df  # store only preview

    self.buffer.append(entry)

  def get_history_text(self, limit=None):
    messages = self.buffer[-limit:] if limit else self.buffer
    text = ""
    for msg in messages:
      role = "User" if msg["role"] == "user" else "Assistant"
      text += f"{role}: {msg['content']}\n"
    return text
