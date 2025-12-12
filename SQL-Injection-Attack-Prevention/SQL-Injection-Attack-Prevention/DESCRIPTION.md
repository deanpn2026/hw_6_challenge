# Scenario

Welcome to your first week at FinTrust Solutions, a rapidly growing fintech startup that provides digital banking services to over 50,000 customers. You've been assigned to the Security Response Team, and your first ticket has just landed in your queue.

## Ticket #SEC-2847: CRITICAL - SQL Injection Vulnerability in User Authentication

During a routine security audit, the external penetration testing team discovered a critical SQL injection vulnerability in the user login system (auth.py). The vulnerability allows attackers to bypass authentication entirely and potentially access any user account without knowing the password. This is a CRITICAL severity issue that must be fixed immediately before it can be exploited in the wild.

Your manager has assigned you to patch this vulnerability. The security team has already disabled public access to the login system, but it needs to be patched and tested within the next hour before the service can be brought back online.

**Impact if not fixed:** Unauthorized access to customer accounts, potential data breach (affecting 50,000+ customers), regulatory fines, and permanent damage to company reputation.

---

# Your Mission

Your task is to refactor the vulnerable authentication function to eliminate the SQL injection vulnerability while maintaining all existing functionality. Specifically, you need to:

1. Identify the SQL injection vulnerability in the current `authenticate_user()` implementation.
2. Replace unsafe SQL query construction with parameterized queries (prepared statements) to correctly handle user input.
3. Implement proper input validation to sanitize user inputs.
4. Ensure all legitimate login functionality still works.
5. Verify that SQL injection attacks are blocked.

---

# Why This Matters

SQL injection is consistently ranked in the OWASP Top 10 most critical web application security risks. By completing this challenge, you'll learn the difference between unsafe and safe database query practices and how to use parameterized queries, which is a fundamental defense that every modern developer must master.

---

# Completing the Challenge

1. Read through the current implementation in `auth.py` and identify the vulnerability  
  *(Hint: look for string concatenation).*

2. Refactor the code to use parameterized queries (`?` placeholders).

3. Run the checker script by executing: ./checker


4. Ensure all tests pass, including: valid logins, invalid logins, and blocked SQL injection attempts (e.g., `' OR '1'='1' --`).

