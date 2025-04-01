import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from sqlalchemy import create_engine
import pandas as pd

# Load environment variables
load_dotenv()

# Initialize database connection
engine = create_engine('sqlite:///data/titanic.db')
db = SQLDatabase(engine)

# Initialize the LLM
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo",
    api_key=os.getenv('OPENAI_API_KEY')
)

# Create the SQL chain
chain = create_sql_query_chain(llm, db)

def main():
    print("Welcome to the Titanic Data Analysis Chatbot!")
    print("Ask questions about the Titanic passengers (type 'exit' to quit)")
    print("\nExample questions:")
    print("- How many passengers are there?")
    print("- How many female passengers?")
    print("- What is the average age of passengers?")
    print("- What was the survival rate by passenger class?")
    print("- What percentage of first class passengers survived?")
    
    while True:
        user_input = input("\nYour question: ")
        
        if user_input.lower() == 'exit':
            break
            
        try:
            # Get the response
            response = chain.invoke({"question": user_input})
            
            # Display the SQL query
            print("\nGenerated SQL query:")
            print(response)
            
            # Execute the query and display results
            results = db.run(response)
            print("\nResults:")
            print(results)
            
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Please try rephrasing your question or ask for clarification.")

if __name__ == "__main__":
    main() 