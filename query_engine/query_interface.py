# query_engine/query_interface.py
def run_query_interface(query_engine):
    """Runs a loop to take user input and query the model."""
    print("Welcome to the Query Engine. Type 'quit' to exit.")
    while True:
        query = input("Please enter your query: ")
        if query.lower() == 'quit':
            print("Exiting the query engine. Goodbye!")
            break
        
        response = query_engine.query(query)
        print("Response:\n", response)

