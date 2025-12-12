# Secure User Search API — SQL Injection Prevention (Python)

## Scenario

Your HR team uses a small internal microservice to search for employee records. Recently, security researchers discovered that the user search API is vulnerable to **SQL injection**, allowing attackers to exfiltrate all employee records by injecting malicious SQL through the search bar.

Your job is to **fix the SQL injection vulnerability** by replacing raw string-formatted SQL with **parameterized prepared statements** using Python’s `sqlite3` module.

## Your Tasks

1. Examine the existing `search_users` function inside `starter/user_search.py`.
2. Identify how SQL injection occurs.
3. Update the function to safely parameterize the SQL query.
4. Ensure all existing functionality still works.
5. Run the test suite found in `starter/tests/` to confirm:
   - normal behavior remains intact  
   - SQL injection payloads no longer work  
   - the API interface is unchanged  

Estimated time to complete: **30–60 minutes**

You do **not** need to write new features or refactor other components.  
Your objective is strictly to fix the security flaw.

Good luck!
