# Data Analysis Chatbot

A proof-of-concept chatbot that can analyze data from a SQL database based on natural language queries.

## Features
- Natural language processing of user queries
- SQL database integration
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
python chatbot.py
```

## Sample Queries
You can ask questions like:
- "What was the survival rate by passenger class?"
- "What was the average age of passengers?"
- "How many passengers embarked from each port?"
- "What was the gender distribution of survivors?"

## Project Structure
- `setup_database.py`: Script to initialize the database and load sample data
- `chatbot.py`: Main chatbot application
- `data/titanic.csv`: Sample Titanic dataset
- `requirements.txt`: Project dependencies 