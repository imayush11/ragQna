# query_engine/index_manager.py
from llama_index.core import VectorStoreIndex


def create_index(documents, service_context):
    """Creates the VectorStoreIndex from documents and service context."""
    return VectorStoreIndex.from_documents(documents, service_context=service_context, show_progress=True)


def get_query_engine(index):
    """Returns a query engine from the index."""
    return index.as_query_engine()


def query_model(query_engine, query_str):
    """Queries the model and returns the response."""
    response = query_engine.query(query_str)
    return response

