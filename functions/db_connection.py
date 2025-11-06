import mysql.connector
from dotenv import load_dotenv
import os

# Load variabel from .env file
load_dotenv()

# Creating conncection to MySQL database using .env configuration
def connect_db():
    try: # Using try/except for better error management rather than if/else
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if db.is_connected():
            print('Python connected with MySQL with your credentials!')
            return db



    except mysql.connector.Error as e:
        print(f"Failed connection to database: {e}")