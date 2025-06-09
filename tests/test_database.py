from dotenv import load_dotenv
import sys
import os
# Add src directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from src.oracle_db_manager import OracleDBManager

# Load environment variables from .env
load_dotenv()

def test_db_connection():
    print("Testing Oracle DB connection...")

    db = OracleDBManager(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=os.getenv("ORACLE_DSN")
    )

    try:
        db.connect()
        print(" Successfully connected to Oracle DB.")
    except Exception as e:
        print(" Failed to connect to Oracle DB:")
        print(e)
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()
