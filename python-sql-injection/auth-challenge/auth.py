# =========================================================================
# FinTrust Solutions - User Authentication Module (auth.py)
# Version 1.0.0 - Production Code Base
# WARNING: Contains CRITICAL Vulnerability (SQL Injection)
# Total Lines: 105
# =========================================================================

import sqlite3
import os
import re
from datetime import datetime
from hashlib import sha256

# Configuration Constants
DATABASE_NAME = "/tmp/auth.db"
LOGIN_ATTEMPTS_LIMIT = 5
SESSION_TIMEOUT_MINUTES = 30

# Utility Function: Database Connection
def get_db_connection():
    """Establishes and returns a connection to the user database."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # Allows column access by name
    return conn

# Initialization: Sets up the database schema if it doesn't exist
def initialize_database():
    """Creates the users table and necessary indices."""
    print(f"[{datetime.now().isoformat()}] INFO: Initializing database schema...")
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                is_admin INTEGER DEFAULT 0,
                last_login TEXT,
                failed_attempts INTEGER DEFAULT 0
            )
        ''')
        # Create index on username for fast lookups
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_username ON users (username)")
        conn.commit()
        print(f"[{datetime.now().isoformat()}] INFO: Database schema ready.")
    except sqlite3.Error as e:
        print(f"[{datetime.now().isoformat()}] ERROR: Database initialization failed: {e}")
    finally:
        conn.close()

# --- Non-Vulnerable Utility Functions for Code Length ---

def log_login_attempt(username, success):
    """Logs the outcome of a login attempt and updates the counter."""
    conn = get_db_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    log_message = "SUCCESS" if success else "FAILURE"
    
    # Log the attempt (print simulates logging to a system log)
    print(f"[{timestamp}] LOG: Login attempt for user '{username}' - {log_message}")

    if success:
        # Reset failed attempts and update last login time
        cursor.execute(
            "UPDATE users SET failed_attempts = 0, last_login = ? WHERE username = ?",
            (timestamp, username)
        )
    else:
        # Increment failed attempts
        cursor.execute(
            "UPDATE users SET failed_attempts = failed_attempts + 1 WHERE username = ?",
            (username,)
        )
    conn.commit()
    conn.close()

def is_account_locked(username):
    """Checks if the account is locked due to too many failed attempts."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT failed_attempts FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    if row and row['failed_attempts'] >= LOGIN_ATTEMPTS_LIMIT:
        return True
    return False

# Function to simulate secure password storage (for contrast)
def hash_password(password):
    """Placeholder for secure hashing (e.g., bcrypt). Using simple SHA256 for demo."""
    return sha256(password.encode('utf-8')).hexdigest()

# --- VULNERABLE FUNCTION: The Target of the Challenge ---

def authenticate_user(username, password):
    """
    VULNERABLE: Authenticate user against the database.
    Returns True if credentials are valid, False otherwise.
    """
    if is_account_locked(username):
        log_login_attempt(username, False)
        return False
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    input_hash = hash_password(password)
    
    # !!! CRITICAL VULNERABILITY HERE: SQL INJECTION VIA STRING FORMATTING !!!
    # The input hash is concatenated directly into the SQL query string.
    
    query = f"SELECT * FROM users WHERE username='{username}' AND password_hash='{input_hash}'"
    
    print(f"[{datetime.now().isoformat()}] DEBUG: Executing query: {query[:80]}...")
    
    try:
        cursor.execute(query)
        result = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"[{datetime.now().isoformat()}] ERROR: Query execution failed: {e}")
        result = None
        
    conn.close()
    
    # Check result and log the attempt
    if result:
        log_login_attempt(username, True)
        return True
    
    log_login_attempt(username, False)
    return False


# Initialize the database when the module is first imported or run
if __name__ == '__main__':
    initialize_database()
