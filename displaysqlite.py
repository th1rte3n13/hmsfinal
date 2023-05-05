import sqlite3

conn = sqlite3.connect('dbhms.db')

cursor = conn.cursor()

cursor.execute("SELECT * FROM visitors")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()

"""import sqlite3

# create a connection to the database
conn = sqlite3.connect('dbhms.db')

# create a cursor object
cursor = conn.cursor()

# execute an SQL statement to create the "users" table
cursor.execute('''CREATE TABLE visitors (vname TEXT, vaddress TEXT, phno INT, emailid TEXT, roomno INT, roomtype TEXT, vpayment TEXT, vtotal INT, vdate TEXT, vtime TEXT)''')

# commit the changes
conn.commit()

# close the cursor and the connection objects
cursor.close()
conn.close()"""
