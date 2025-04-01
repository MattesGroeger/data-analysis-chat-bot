import pandas as pd
from sqlalchemy import create_engine
import os

def setup_database():
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Download Titanic dataset if it doesn't exist
    if not os.path.exists('data/titanic.csv'):
        print("Downloading Titanic dataset...")
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        df = pd.read_csv(url)
        df.to_csv('data/titanic.csv', index=False)
        print("Dataset downloaded successfully!")
    
    # Create SQLite database
    engine = create_engine('sqlite:///data/titanic.db')
    
    # Load data into database
    df = pd.read_csv('data/titanic.csv')
    df.to_sql('passengers', engine, if_exists='replace', index=False)
    print("Database initialized successfully!")

if __name__ == "__main__":
    setup_database() 