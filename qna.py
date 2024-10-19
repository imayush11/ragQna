# qna.py
from query_engine.document_loader import load_documents
from query_engine.llm_service import create_llm_service, create_service_context
from query_engine.index_manager import create_index, get_query_engine
from query_engine.query_interface import run_query_interface


def main():
    # Load the documents
    documents = load_documents("data")
    
    # Initialize the LLM service
    llm = create_llm_service()
    
    # Create service context
    service_context = create_service_context(llm)
    
    # Create the index
    index = create_index(documents, service_context)
    
    # Get the query engine
    query_engine = get_query_engine(index)
    
    # Run the query interface
    run_query_interface(query_engine)


if __name__ == "__main__":
    main()

