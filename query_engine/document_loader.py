# query_engine/document_loader.py
from llama_index.core import SimpleDirectoryReader


def load_documents(data_dir="data"):
    """Loads documents from the specified directory."""
    return SimpleDirectoryReader(data_dir).load_data()

