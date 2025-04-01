import os
from dotenv import load_dotenv
import openai
from sqlalchemy import create_engine, text
import pandas as pd
import re

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize database connection
engine = create_engine('sqlite:///data/titanic.db')

def get_table_schema():
    """Get the schema of the passengers table"""
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM passengers LIMIT 1"))
        columns = result.keys()
        return list(columns)

def execute_query(query):
    """Execute SQL query and return results as DataFrame"""
    try:
        with engine.connect() as conn:
            df = pd.read_sql_query(query, conn)
            return df
    except Exception as e:
        return f"Error executing query: {str(e)}"

def clean_sql_query(query):
    """Clean up the SQL query by removing markdown formatting and extra whitespace"""
    # Remove markdown code block formatting
    query = re.sub(r'```sql\n?', '', query)
    query = re.sub(r'```\n?', '', query)
    # Remove leading/trailing whitespace
    query = query.strip()
    return query

def generate_sql_query(user_question):
    """Generate SQL query from natural language using OpenAI"""
    schema = get_table_schema()
    schema_str = ", ".join(schema)
    
    prompt = f"""Given the following SQL table schema for the Titanic passengers:
    Table name: passengers
    Columns: {schema_str}

    Generate a SQL query to answer this question: {user_question}

    Guidelines:
    1. For counting questions, use COUNT(*) with an appropriate alias
    2. For questions about specific groups, use COUNT(*) with WHERE clause
    3. Only return detailed data when specifically asked for details
    4. Always use the correct table name 'passengers'
    5. Format the output to be clear and readable
    6. For rate calculations (like survival rate):
       - Use COUNT(CASE WHEN condition THEN 1 END) for counting specific cases
       - Calculate as: (COUNT(CASE WHEN condition THEN 1 END) / COUNT(*)) * 100
       - Use ROUND() to limit decimal places
       - Include both the count and percentage in the output
    7. For grouped statistics:
       - Include the grouping column
       - Show both counts and percentages where relevant
       - Order results logically

    Example queries:
    - For survival rate: 
      SELECT Pclass,
             COUNT(*) as total_passengers,
             COUNT(CASE WHEN Survived = 1 THEN 1 END) as survivors,
             ROUND((COUNT(CASE WHEN Survived = 1 THEN 1 END) * 100.0 / COUNT(*)), 2) as survival_rate
      FROM passengers
      GROUP BY Pclass
      ORDER BY Pclass;

    Return only the SQL query without any explanation or markdown formatting."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a SQL expert. Generate only SQL queries without explanations or markdown formatting. Always use the correct table name 'passengers' and follow the guidelines for query generation."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return clean_sql_query(response.choices[0].message.content.strip())

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
            
        # Generate SQL query
        sql_query = generate_sql_query(user_input)
        print(f"\nGenerated SQL query: {sql_query}")
        
        # Execute query and display results
        results = execute_query(sql_query)
        
        if isinstance(results, str):
            print(f"Error: {results}")
        else:
            print("\nResults:")
            print(results)

if __name__ == "__main__":
    main() 