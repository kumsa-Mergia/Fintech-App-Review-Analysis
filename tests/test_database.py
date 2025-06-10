from dotenv import load_dotenv
import sys
import os
import cx_Oracle # This import is REQUIRED to access cx_Oracle.SYSDBA

# Add src directory to path (assuming your current script is one level up from 'src')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd # Needed if you use pandas functions in your main script
from src.oracle_db_manager import OracleDBManager

# Load environment variables from .env
load_dotenv()

def test_db_connection():
    print("Testing Oracle DB connection...")

    # Retrieve connection details from environment variables
    oracle_user = os.getenv("ORACLE_USER")
    oracle_password = os.getenv("ORACLE_PASSWORD")
    oracle_dsn = os.getenv("ORACLE_DSN")

    # Determine the connection mode (e.g., SYSDBA) if the user is SYS
    connection_mode = None
    if oracle_user and oracle_user.upper() == "SYS":
        connection_mode = cx_Oracle.SYSDBA # Set the SYSDBA mode

    # Instantiate OracleDBManager with the retrieved details and mode
    db = OracleDBManager(
        user=oracle_user,
        password=oracle_password,
        dsn=oracle_dsn,
        mode=connection_mode # Pass the connection mode
    )

    try:
        db.connect()
        print("Successfully connected to Oracle DB.")
        
        # Example: Try creating tables (only if you want to test this)
        # db.create_tables()

    except Exception as e:
        print(f"Failed to connect to Oracle DB: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()