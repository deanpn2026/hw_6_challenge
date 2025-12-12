# Python SQL Injection Prevention Dojo

Welcome to the **Python SQL Injection Prevention Dojo**!

In this dojo, you will explore how insecure SQL queries can expose applications to SQL injection attacks, and you will practice securing a vulnerable Python codebase by replacing unsafe SQL string formatting with **prepared statements**.

This dojo contains one module with a single challenge focused on secure software development.

---

## Overview

The goal of this dojo is to help you understand:

- How SQL injection works in Python applications
- Why directly inserting user input into SQL queries is dangerous
- How to correctly use Python’s `sqlite3` parameter binding
- How to verify your fix using automated tests

This dojo follows a realistic scenario: you are maintaining an internal microservice that allows HR staff to search for employee records. A penetration test revealed that the `search_users` function is vulnerable to SQL injection. Your job is to patch it while preserving all existing functionality.

---

## Structure

