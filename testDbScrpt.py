import sqlite3

conn = sqlite3.connect('test.db')
conn.execute("PRAGMA foreign_keys = 1")

#conn.execute("DROP TABLE IF EXISTS testing;")
#conn.execute("DROP TABLE IF EXISTS testingFK;")

conn.execute('''CREATE TABLE testing
			(testID INTEGER PRIMARY KEY AUTOINCREMENT,
		    testName varchar(20) not null);''')

conn.execute("INSERT INTO testing (testName) VALUES ('jQuery')")
conn.execute("INSERT INTO testing (testName) VALUES ('bethany')")
conn.execute("INSERT INTO testing (testName) VALUES ('testing')")

for row in conn.execute("SELECT * FROM testing"):
    print(row)

conn.execute('''CREATE TABLE testingFK
            (tfkID INTEGER PRIMARY KEY AUTOINCREMENT,
		    testFKName varchar(20) not null,
            testID INTEGER not null,
            FOREIGN KEY(testID) REFERENCES testing(testID));''')

conn.execute("INSERT INTO testingFK (testFKName, testID) VALUES ('library', 1)")
conn.execute("INSERT INTO testingFK (testFKName, testID) VALUES ('vella', 2)")

for row2 in conn.execute("SELECT * FROM testingFK"):
    print(row2)

