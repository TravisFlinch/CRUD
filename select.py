import sqlite3

conn = sqlite3.connect('company.db')
print("Succesfully connected to the database")

data = conn.execute("SELECT * FROM Company3");
for rows in data:
    print('ID= ', rows[0])
    print('FIRSTNAME= ', rows[1])
    print('LASTNAME= ', rows[2])
    print('AGE= ', rows[3])
    print('SALARY= ', rows[4])
    print('TASK= ', rows[5])

print("Succesfully selected from Company3")
conn.close()