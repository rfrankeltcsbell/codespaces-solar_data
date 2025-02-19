import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("db.sql")
cursor = conn.cursor()


