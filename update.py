import sqlite3

conn = sqlite3.connect('company.db')
print("Succesfully connected to the database")

conn.execute("UPDATE Company3 set SALARY=5000.00 where ID=1")
conn.commit()

data = conn.execute("SELECT * FROM Company3")
for rows in data:
    print("ID:", rows[0])
    print("FIRSTNAME:", rows[1])
    print("LASTNAME:", rows[2])
    print("AGE:", rows[3])
    print("SALARY:", rows[4])
    print("TASK:", rows[5])

conn.close()