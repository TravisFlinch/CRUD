import sqlite3
conn = sqlite3.connect('company.db')
print("Connected")

conn.execute("INSERT INTO Company3(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
             VALUES (1, 'Andrew', 'Tate', 28, 300.00, 'Manager')");
conn.execute("INSERT INTO Company3(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
             VALUES(2, 'Travis', 'Scott', 26, 400.00, 'Artist')")
conn.execute("INSERT INTO Company3(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
             VALUES (3, 'Fenton', 'Elias', 20,500.00, 'Inventrory')")
conn.execute("INSERT INTO Company3(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
             VALUES(4, 'Mf', 'Doom', 31, 600.00, 'Chief')")
conn.commit()
print("Succesfully inserted values in Company1")

conn.close()