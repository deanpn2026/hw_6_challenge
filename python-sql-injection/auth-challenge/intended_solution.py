import sqlite3
import os
import re
from datetime import datetime
from hashlib import sha256

# --- SECURE FUNCTION: The Intended Solution ---


def authenticate_user(username, password):
    """
    SECURE: Authenticate user against the database using parameterized queries.
    Returns True if credentials are valid, False otherwise.
    """
    if is_account_locked(username):
        log_login_attempt(username, False)
        return False
        
    # 1. Input Validation (Defense in Depth)
    # Ensure inputs are strings and not excessively long
    if not isinstance(username, str) or not username or len(username) > 50:
        return False
        
    # Optional: Basic character check for username
    if not re.match(r'^[a-zA-Z0-9_.-]+$', username):
        return False

    conn = get_db_connection()
    cursor = conn.cursor()

    input_hash = hash_password(password)

    # 2. FIX: SECURE PARAMETERIZED QUERY (Prepared Statement)
    # Use '?' placeholders and pass parameters as a tuple.
    # The database driver safely escapes the inputs, preventing SQL injection.
    
    query = "SELECT * FROM users WHERE username=? AND password_hash=?"
    
    try:
        # Pass (username, input_hash) as a tuple of parameters
        cursor.execute(query, (username, input_hash)) 
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

