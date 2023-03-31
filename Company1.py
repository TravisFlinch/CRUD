import sqlite3
conn = sqlite3.connect('company.db')
print("successfully opened database")

conn.execute("""CREATE TABLE Company3(
ID INT PRIMARY KEY  NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL,
TASK TEXT CHAR(20))""")

print("succesfully created company1")
conn.close()