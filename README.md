# Data Analysis Chatbot

A proof-of-concept chatbot that can analyze data from a SQL database based on natural language queries. This implementation uses LangChain's SQL query chain to convert natural language questions into SQL queries and execute them against a SQLite database.

## Features
- Natural language to SQL query conversion using LangChain
- SQLite database integration
- Data analysis capabilities
- Sample Titanic dataset included

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. Run the setup script to initialize the database:
```bash
python setup_database.py
```

5. Start the chatbot:
```bash
python chatbot_langchain.py
```

## Sample Queries
You can ask questions like:
- "How many passengers are there?"
- "How many female passengers?"
- "What is the average age of passengers?"
- "What was the survival rate by passenger class?"
- "What percentage of first class passengers survived?"

## Project Structure
- `setup_database.py`: Script to initialize the database and load sample data
- `chatbot_langchain.py`: Main chatbot application using LangChain
- `data/titanic.csv`: Sample Titanic dataset
- `requirements.txt`: Project dependencies

## Technical Details
The chatbot uses:
- LangChain's `create_sql_query_chain` for converting natural language to SQL
- SQLAlchemy for database operations
- SQLite as the database backend
- OpenAI's GPT-3.5-turbo model for query generation

## Example Output
When you ask a question, the chatbot will:
1. Generate the appropriate SQL query
2. Execute the query against the database
3. Display both the SQL query and the results

Example:
```
Your question: How many female passengers?

Generated SQL query:
SELECT COUNT(*) FROM passengers WHERE Sex = 'female';

Results:
314
``` 