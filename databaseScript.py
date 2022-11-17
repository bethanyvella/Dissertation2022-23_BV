import sqlite3
import traceback

try:
	#creation of database
	conn = sqlite3.connect('dissertation_database.db')
	conn.execute("PRAGMA foreign_keys = 1")

	#dropping tables for a clean run
	#conn.execute("DROP TABLE IF EXISTS url;")
	#conn.execute("DROP TABLE IF EXISTS variant;")
	#conn.execute("DROP TABLE IF EXISTS version;")
	#conn.execute("DROP TABLE IF EXISTS library;")

	#table 1 -  library table where it will hold the library names 
	conn.execute('''CREATE TABLE library
			(libraryID INTEGER PRIMARY KEY AUTOINCREMENT,
		libraryName varchar(20) not null);''')

	#table 2 -  version table where it will hold the versions for each library  
	conn.execute('''CREATE TABLE version
			(versionID INTEGER PRIMARY KEY AUTOINCREMENT,
		versionName nvarchar(20) not null,
		isVulnerable bit not null,
		libraryID int not null,
		foreign key(libraryID) References library(libraryID));''')

	#table 3 -  variant table where it will hold the different variants found in each library version 
	conn.execute('''CREATE TABLE variant
			(variantID INTEGER PRIMARY KEY AUTOINCREMENT,
		fileName nvarchar(20) not null,
		hashKey uniqueidentifier not null,
		content text not null,
		versionID int not null,
		foreign key(versionID) References version(versionID));''')

	#table 4 -  url table where it will hold the known and trusted urls for the same javascript version/library 
	conn.execute('''CREATE TABLE url
			(urlID INTEGER PRIMARY KEY AUTOINCREMENT,
		url varchar(250),
		variantID int not null,
		foreign key(variantID) References variant(variantID));''')

	#inserting values
	#insert in table 1 
	conn.execute('INSERT INTO library (libraryName) VALUES ("jQuery")')
	for row in (conn.execute("SELECT * FROM library")):
		print(row)

	for row1 in (conn.execute("SELECT * FROM version")):
		print(row1)
	#insert data in table 2
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.6.0', 0 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.5.1', 0 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.5.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.4.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.4.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.3.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.3.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.2.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.2.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.1.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.1.0', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.0.0', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.2.4', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.2.3', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.2.2', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.2.1', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.2.0', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.1.4', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.1.3', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.1.2', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.1.1', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.1.0', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.0.3', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.0.2', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.0.1', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('2.0.0', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.12.', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.12.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.12.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.12.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.12.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.11.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.11.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.11.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.11.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.10.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.10.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.10.', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.9.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.9.0', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.8.3', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.8.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.8.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.8.0', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.7.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.7.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.7.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.6.4', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.6.3', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.6.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.6.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.6.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.5.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.5.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.5.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.4.4', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.4.3', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.4.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.4.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.4.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.3.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.3.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.3.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.2.6', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.2.5', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.2.4', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.2.3', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.2.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.2.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.2.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.1.4', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.1.3', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.1.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.1.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.1.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.0.4', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.0.3', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.0.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.0.1', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.0.0', 1 , 1)")
	conn.close()
except Exception as e: 
	print(type(e))
	print(e) 
	print(traceback.print_exc()) 
else:
	print("SQL Creation is ready")
