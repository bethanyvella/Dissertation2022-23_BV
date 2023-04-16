import sqlite3
import traceback

try:
	#creation of database
	conn = sqlite3.connect('dissertation_database.db')
	conn.execute("PRAGMA foreign_keys = 1")

	#dropping tables for a clean run
	conn.execute("DROP TABLE IF EXISTS url;")
	conn.execute("DROP TABLE IF EXISTS variant;")
	conn.execute("DROP TABLE IF EXISTS version;")
	conn.execute("DROP TABLE IF EXISTS library;")

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
	conn.execute('INSERT INTO library (libraryName) VALUES ("jQuery-Migrate")')
	conn.execute('INSERT INTO library (libraryName) VALUES ("underscore.js")')
	for row in (conn.execute("SELECT * FROM library")):
		print(row)

	#insert data in table 2
	
	# insert jquery data

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
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.12.4', 1 , 1)"), 
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.12.3', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.12.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.12.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.12.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.11.3', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.11.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.11.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.11.0', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.10.2', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.10.1', 1 , 1)"),
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.10.0', 1 , 1)"),
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
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.0.0', 1 , 1)"),

	#entering data for library 2 - jquery-migrare
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.4.1', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.4.0', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.3.2', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.3.1', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.3.0', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.2.0', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.1.0', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.0.1', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('3.0.0', 0 , 2)"),	

	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.4.1', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.4.0', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.3.0', 0 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.2.0', 1 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.1.1', 1 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.1.0', 1 , 2)"),	
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.0.0', 1 , 2)"),
	
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.1.0',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.2.0',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.3.0',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.3.1',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.3.2',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.3.3',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.4.0',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.4.1',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.4.2',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.4.3',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.4.4',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.4.5',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.4.6',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.4.7',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.5.0',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.5.1',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.5.2',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.5.3',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.5.4',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.5.5',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.5.6',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.5.7',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.5.8',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('0.6.0',0,3)"),

	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.0.0',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.0.1',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.0.2',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.0.3',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.0.4',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.1.0',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.1.1',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.1.2',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.1.3',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.1.4',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.1.5',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.1.6',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.1.7',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.2.0',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.2.1',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.2.2',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.2.3',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.2.4',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.3.0',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.3.1',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.3.2',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.3.3',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.4.0',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.4.1',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.4.2',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.4.3',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.4.4',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.5.0',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.5.1',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.5.2',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.6.0',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.7.0',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.8.0',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.8.1',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.8.2',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.8.3',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.9.0',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.9.1',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.9.2',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.10.0',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.10.1',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.10.2',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.11.0',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.12.0',1,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.12.1',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.13.1',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.13.2',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.13.3',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.13.4',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.13.5',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.13.6',0,3)"),
	conn.execute("INSERT INTO version(versionName, isVulnerable, libraryID) VALUES ('1.3.1-amdjs',0,3)"),

	#entering data for library 3 - underscore.js


	#inserting in table 3

	#entering data for library 1- jqeury 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.6.0/jquery.js', '1fe2bb5390a75e5d61e72c107cab528fc3c29a837d69aab7d200e1dbb5dcd239',\
		 'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.6.0.js', 1)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.5.1/jquery.js', '416a3b2c3bf16d64f6b5b6d0f7b079df2267614dd6847fc2f3271b4409233c37',\
		 'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.5.1.js', 2)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.5.0/jquery.js', 'aff01a147aeccc9b70a5efad1f2362fd709f3316296ec460d94aa7d31decdb37',\
		 'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.5.0.js', 3)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.4.1/jquery.js', '5a93a88493aa32aab228bf4571c01207d3b42b0002409a454d404b4d8395bd5',\
		 'C\\JQueries\\3.0.0\\uncompressed\\jquery-3.4.1.js', 4)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.4.0/jquery.js', '0d864c082f074c2f900ebe5035a21c7d1ed548fb5c212ca477ee9e4a6056e6aa',\
			'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.4.0.js', 5)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.3.1/jquery.js', 'd8aa24ecc6cecb1a60515bc093f1c9da38a0392612d9ab8ae0f7f36e6eee1fad',\
			'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.3.1.js', 6)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.3.0/jquery.js', '4c5592b8326dea44be86e57ebd59725758ccdddc0675e356a9ece14f15c1fd7f',\
			'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.3.0.js', 7)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.2.1/jquery.js', '0d9027289ffa5d9f6c8b4e0782bb31bbff2cef5ee3708ccbcb7a22df9128bb21',\
			'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.2.1.js', 8)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.2.0/jquery.js', 'c0f149348165558e3d07e0ae008ac3afddf65d26fa264dc9d4cdb6337136ca54',\
			'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.2.0.js', 9)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.1.1/jquery.js', 'd7a71d3dd740e95755227ba6446a3a21b8af6c4444f29ec2411dc7cd306e10b0',\
			'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.1.1.js', 10)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.1.0/jquery.js', 'b25a2092f0752b754e933008f10213c55dd5ce93a791e355b0abed9182cc8df9',\
			'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.1.0.js', 11)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.0.0/jquery.js', '8eb3cb67ef2f0f1b76167135cef6570a409c79b23f0bc0ede71c9a4018f1408a',\
			'C:\\JQueries\\3.0.0\\uncompressed\\jquery-3.0.0.js', 12)"),

	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.6.0/jquery.min.js', 'ff2cc831926cb50addf4e52dc5fc9c660c354cc8563cf4f26800a13bac363a81',\
		 'C:\\JQueries\\3.0.0\\minified\\jquery-3.6.0.min.js', 1)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.5.1/jquery.min.js', 'f7f6a5894f1d19ddad6fa392b2ece2c5e578cbf7da4ea805b6885eb6985b6e3d',\
		 'C:\\JQueries\\3.0.0\\minified\\jquery-3.5.1.min.js', 2)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.5.0/jquery.min.js', 'c4dccdd9ae25b64078e0c73f273de94f8894d5c99e4741645ece29aeefc9c5a4',\
		 'C:\\JQueries\\3.0.0\\minified\\jquery-3.5.0.min.js', 3)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.4.1/jquery.min.js', '0925e8ad7bd971391a8b1e98be8e87a6971919eb5b60c196485941c3c1df089a',\
			'C:\\JQueries\\3.0.0\\minified\\jquery-3.4.1.min.js', 4)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.4.0/jquery.min.js', '0497a8d2a9bde7db8c0466fae73e347a3258192811ed1108e3e096d5f34ac0e8',\
			'C:\\JQueries\\3.0.0\\minified\\jquery-3.4.0.min.js', 5)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.3.1/jquery.min.js', '160a426ff2894252cd7cebbdd6d6b7da8fcd319c65b70468f10b6690c45d02ef',\
			'C:\\JQueries\\3.0.0\\minified\\jquery-3.3.1.min.js', 6)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.3.0/jquery.min.js', '453432f153a63654fa6f63c846eaf7ee9e8910165413ba3cc0f80cbeed7c302e',\
			'C:\\JQueries\\3.0.0\\minified\\jquery-3.3.0.min.js', 7)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.2.1/jquery.min.js', '87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de',\
			'C:\\JQueries\\3.0.0\\minified\\jquery-3.2.1.min.js', 8)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.2.0/jquery.min.js', '2405bdf4c255a4904671bcc4b97938033d39b3f5f20dd068985a8d94cde273e2',\
			'C:\\JQueries\\3.0.0\\minified\\jquery-3.2.0.min.js', 9)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.1.1/jquery.min.js', '85556761a8800d14ced8fcd41a6b8b26bf012d44a318866c0d81a62092efd9bf',\
			'C:\\JQueries\\3.0.0\\minified\\jquery-3.1.1.min.js', 10)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.1.0/jquery.min.js', '702b9e051e82b32038ffdb33a4f7eb5f7b38f4cf6f514e4182d8898f4eb0b7fb',\
			'C:\\JQueries\\3.0.0\\minified\\jquery-3.1.0.min.js', 11)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.0.0/jquery.min.js', '266bcea0bb58b26aa5b16c5aee60d22ccc1ae9d67daeb21db6bad56119c3447d',\
			'C:\\JQueries\\3.0.0\\minified\\jquery-3.0.0.min.js', 12)"), 

	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.6.0/jquery.slim.js', '1f058e34466ba6ea21f79d5c403d68bf61d42b9cc0e43c09d433545da33a16c6',\
		 'C:\\JQueries\\3.0.0\\slim\\jquery-3.6.0.slim.js', 1)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.5.1/jquery.slim.js', '0eb4f935fc5f6c7bcc1eec77d4b921c60e362d8ea87fc4da6322b9d239f14673',\
		 'C:\\JQueries\\3.0.0\\slim\\jquery-3.5.1.slim.js', 2)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.5.0/jquery.slim.js', 'b027b185a2a901fbaaba52a3b5263b57d1fb413d1308df741fe6393659aa3941',\
		 'C:\\JQueries\\3.0.0\\slim\\jquery-3.5.0.slim.js', 3)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.4.1/jquery.slim.js', '0539537503bdfdf6ac701d5dade92b0d591a29df4f93007298c9473a21bea8b2',\
			'C:\\JQueries\\3.0.0\\slim\\jquery-3.4.1.slim.js', 4)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.4.0/jquery.slim.js', '9a295ecf1e656a4ad9bb438ff5bd90585cb57edfd41142ba347d49ab3f215214',\
			'C:\\JQueries\\3.0.0\\slim\\jquery-3.4.0.slim.js', 5)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.3.1/jquery.slim.js', '7cd5c914895c6b4e4120ed98e73875c6b4a12b7304fbf9586748fe0a1c57d830',\
			'C:\\JQueries\\3.0.0\\slim\\jquery-3.3.1.slim.js', 6)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.3.0/jquery.slim.js', 'ec89a3d1f2cab57e4d144092d6e9a8429ecd0b594482be270536ac366ee004b6',\
			'C:\\JQueries\\3.0.0\\slim\\jquery-3.3.0.slim.js', 7)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.2.1/jquery.slim.js', 'b40f32d17aa2c27a7098e225dd218070597646fc478c0f2aa74fb5b821a64668',\
			'C:\\JQueries\\3.0.0\\slim\\jquery-3.2.1.slim.js', 8)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.2.0/jquery.slim.js', 'f18ac10930e84233b80814f5595bcc1f6ffad74047d038d997114e08880aec03',\
			'C:\\JQueries\\3.0.0\\slim\\jquery-3.2.0.slim.js', 9)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.1.1/jquery.slim.js', 'e62fe6437d3433befd3763950eb975ea56e88705cd51dccbfd1d9a5545f25d60',\
			'C:\\JQueries\\3.0.0\\slim\\jquery-3.1.1.slim.js', 10)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.1.0/jquery.slim.js', '2faa690232fa8e0b5199f8ae8a0784139030348da91ff5fd2016cfc9a9c9799c',\
			'C:\\JQueries\\3.0.0\\slim\\jquery-3.1.0.slim.js', 11)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.0.0/jquery.slim.js', '1a9ea1a741fe03b6b1835b44ac2b9c59e39cdfc8abb64556a546c16528fc2828',\
			'C:\\JQueries\\3.0.0\\slim\\jquery-3.0.0.slim.js', 12)"), 
	
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.6.0/jquery.slim.min.js', '1f058e34466ba6ea21f79d5c403d68bf61d42b9cc0e43c09d433545da33a16c6',\
		 'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.6.0.slim.min.js', 1)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.5.1/jquery.slim.min.js', '0eb4f935fc5f6c7bcc1eec77d4b921c60e362d8ea87fc4da6322b9d239f14673',\
		 'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.5.1.slim.min.js', 2)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
	 VALUES ('3.5.0/jquery.slim.min.js', 'b027b185a2a901fbaaba52a3b5263b57d1fb413d1308df741fe6393659aa3941',\
		 'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.5.0.slim.min.js', 3)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.4.1/jquery.slim.min.js', '0539537503bdfdf6ac701d5dade92b0d591a29df4f93007298c9473a21bea8b2',\
			'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.4.1.slim.min.js', 4)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.4.0/jquery.slim.min.js', '9a295ecf1e656a4ad9bb438ff5bd90585cb57edfd41142ba347d49ab3f215214',\
			'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.4.0.slim.min.js', 5)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.3.1/jquery.slim.min.js', '7cd5c914895c6b4e4120ed98e73875c6b4a12b7304fbf9586748fe0a1c57d830',\
			'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.3.1.slim.min.js', 6)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.3.0/jquery.slim.min.js', 'ec89a3d1f2cab57e4d144092d6e9a8429ecd0b594482be270536ac366ee004b6',\
			'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.3.0.slim.min.js', 7)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.2.1/jquery.slim.min.js', 'b40f32d17aa2c27a7098e225dd218070597646fc478c0f2aa74fb5b821a64668',\
			'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.2.1.slim.min.js', 8)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.2.0/jquery.slim.min.js', 'f18ac10930e84233b80814f5595bcc1f6ffad74047d038d997114e08880aec03',\
			'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.2.0.slim.min.js', 9)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.1.1/jquery.slim.min.js', 'e62fe6437d3433befd3763950eb975ea56e88705cd51dccbfd1d9a5545f25d60',\
			'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.1.1.slim.min.js', 10)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.1.0/jquery.slim.min.js', '2faa690232fa8e0b5199f8ae8a0784139030348da91ff5fd2016cfc9a9c9799c',\
			'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.1.0.slim.min.js', 11)"), 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('3.0.0/jquery.slim.min.js', '1a9ea1a741fe03b6b1835b44ac2b9c59e39cdfc8abb64556a546c16528fc2828',\
			'C:\\JQueries\\3.0.0\\slimminifed\\jquery-3.0.0.slim.min.js', 12)"),
	

	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.2.4/jquery.js', '893e90f6230962e42231635df650f20544ad22affc3ee396df768eaa6bc5a6a2',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.2.4.js', 13)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.2.3/jquery.js', '95a5d6b46c9da70a89f0903e5fdc769a2c266a22a19fcb5598e5448a044db4fe',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.2.3.js', 14)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.2.2/jquery.js', 'e3fcd40aa8aad24ab1859232a781b41a4f803ad089b18d53034d24e4296c6581',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.2.2.js', 15)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.2.1/jquery.js', '78d714ccede3b2fd179492ef7851246c1f1b03bfc2ae83693559375e99a7c077',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.2.1.js', 16)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.2.0/jquery.js', 'a18aa92dea997bd71eb540d5f931620591e9dee27e5f817978bb385bab924d21',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.2.0.js', 17)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.1.4/jquery.js', 'b2215cce5830e2350b9d420271d9bd82340f664c3f60f0ea850f7e9c0392704e',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.1.4.js', 18)"),		
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.1.3/jquery.js', '828cbbcacb430f9c5b5d27fe9302f8795eb338f2421010f5141882125226f94f',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.1.3.js', 19)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.1.2/jquery.js', '07cb07bdfba40ceff869b329eb48eeede41740ba6ce833dd3830bd0af49e4898',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.1.2.js', 20)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.1.1/jquery.js', '140ff438eaaede046f1ceba27579d16dc980595709391873fa9bf74d7dbe53ac',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.1.1.js', 21)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.1.0/jquery.js', '0fa7752926a95e3ab6b5f67a21ef40628ce4447c81ddf4f6cacf663b6fb85af7',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.1.0.js', 22)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.0.3/jquery.js', '9427fe2df51f7d4c6bf35f96d19169714d0b432b99dc18f41760d0342c538122',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.0.3.js', 23)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.0.2/jquery.js', 'd2ed0720108a75db0d53248ba8e36332658064c4189714d16c0f117efb42016d',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.0.2.js', 24)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.0.1/jquery.js', '820fb338fe8c7478a1b820e2708b4fd306a68825de1194803e7a93fbc2177a16',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.0.1.js', 25)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.0.0/jquery.js', '896e379d334cf0b16c78d9962a1579147156d4a72355032fce0de5f673d4e287',\
			'C:\\JQueries\\2.0.0\\uncompressed\\jquery-2.0.0.js', 26)"),


	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.2.4/jquery.min.js', '05b85d96f41fff14d8f608dad03ab71e2c1017c2da0914d7c59291bad7a54f8e',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.2.4.min.js', 13)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.2.3/jquery.min.js', '6b6de0d4db7876d1183a3edb47ebd3bbbf93f153f5de1ba6645049348628109a',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.2.3.min.js', 14)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.2.2/jquery.min.js', 'dfa729d82a3effadab1000181cb99108f232721e3b0af74cfae4c12704b35a32',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.2.2.min.js', 15)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.2.1/jquery.min.js', '82f420005cd31fab6b4ab016a07d623e8f5773de90c526777de5ba91e9be3b4d',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.2.1.min.js', 16)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.2.0/jquery.min.js', '8a102873a33f24f7eb22221e6b23c4f718e29f85168ecc769a35bfaed9b12cce',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.2.0.min.js', 17)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.1.4/jquery.min.js', 'f16ab224bb962910558715c82f58c10c3ed20f153ddfaa199029f141b5b0255c',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.1.4.min.js', 18)"),		
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.1.3/jquery.min.js', '8af93bd675e1cfd9ecc850e862819fdac6e3ad1f5d761f970e409c7d9c63bdc3',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.1.3.min.js', 19)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.1.2/jquery.min.js', '604ec12a7d5e6bd8e2ac21cfaff11a5b93719a465919be76f99683d942a87576',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.1.2.min.js', 20)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.1.1/jquery.min.js', '874706b2b1311a0719b5267f7d1cf803057e367e94ae1ff7bf78c5450d30f5d4',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.1.1.min.js', 21)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.1.0/jquery.min.js', 'f284353a7cc4d97f6fe20a5155131bd43587a0f1c98a56eeaf52cff72910f47d',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.1.0.min.js', 22)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.0.3/jquery.min.js', 'b13cb5989e08fcb02314209d101e1102f3d299109bdc253b62aa1da21c9e38ba',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.0.3.min.js', 23)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.0.2/jquery.min.js', '4d9586a075f082a04fd40178499c472012b351db4c1a4d210907a0891f7d8ad9',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.0.2.min.js', 24)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.0.1/jquery.min.js', '243f6ee513637db6d897f01b89862f54f29c2cd94a35edaead432e1b334421c9',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.0.1.min.js', 25)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('2.0.0/jquery.min.js', 'd482871a5e948cb4884fa0972ea98a81abca057b6bd3f8c995a18c12487e761c',\
			'C:\\JQueries\\2.0.0\\minifed\\jquery-2.0.0.min.js', 26)"),


	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.12.4/jquery.js', '430f36f9b5f21aae8cc9dca6a81c4d3d84da5175eaedcf2fdc2c226302cb3575',\
			'C:\\JQueries\\1.12.4\\uncompressed\\jquery-1.0.0.js', 27)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.12.3/jquery.js', 'd5732912d03878a5cd3695dc275a6630fb3c255fa7c0b744ab08897824049327',\
			'C:\\JQueries\\1.12.3\\uncompressed\\jquery-1.0.0.js', 28)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.12.2/jquery.js', '5540b2af46570795610626e8d8391356176ca639b1520c4319a2d0c7ba9bef16',\
			'C:\\JQueries\\1.12.2\\uncompressed\\jquery-1.0.0.js', 29)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.12.1/jquery.js', '56e843a66b2bf7188ac2f4c81df61608843ce144bd5aa66c2df4783fba85e8ef',\
			'C:\\JQueries\\1.12.1\\uncompressed\\jquery-1.0.0.js', 30)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.12.0/jquery.js', 'c85537acad72f0d7d409dfc1e2d2daa59032f71d29642a8b64b9852f70166fbb',\
			'C:\\JQueries\\1.12.0\\uncompressed\\jquery-1.0.0.js', 31)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.11.3/jquery.js', '2065aecca0fb9b0567358d352ed5f1ab72fce139bf449b4d09805f5d9c3725ed',\
			'C:\\JQueries\\1.11.3\\uncompressed\\jquery-1.0.0.js', 32)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.11.2/jquery.js', '58c27035b7a2e589df397e5d7e05424b90b8c1aaaf73eff47d5ed6daecb70f25',\
			'C:\\JQueries\\1.11.2\\uncompressed\\jquery-1.0.0.js', 33)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.11.1/jquery.js', '3029834a820c79c154c377f52e2719fc3ff2a27600a07ae089ea7fde9087f6bc',\
			'C:\\JQueries\\1.11.1\\uncompressed\\jquery-1.0.0.js', 34)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.11.0/jquery.js', 'ce0343e1d6f489768eeefe022c12181c6a0822e756239851310acf076d23d10c',\
			'C:\\JQueries\\1.11.0\\uncompressed\\jquery-1.0.0.js', 35)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.10.2/jquery.js', '8ade6740a1d3cfedf81e28d9250929341207b23a55f1be90ccc26cf6d98e052a',\
			'C:\\JQueries\\1.10.2\\uncompressed\\jquery-1.0.0..js', 36)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.10.1/jquery.js', 'ebaded49db62a60060caa2577f2a4ec1ff68726bc40861bc65d977abeb64fa7d',\
			'C:\\JQueries\\1.10.1\\uncompressed\\jquery-1.0.0.js', 37)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.10.0/jquery.js', '8aa0f84b5331efcc3cb72c7d504c2bc6ebd861da003d72c33df99ce650d4531d',\
			'C:\\JQueries\\1.10.1\\uncompressed\\jquery-1.0.0.js', 38)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.9.1/jquery.js', '7bd80d06c01c0340c1b9159b9b4a197db882ca18cbac8e9b9aa025e68f998d40',\
			'C:\\JQueries\\1.9.1\\uncompressed\\jquery-1.0.0.js', 39)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.9.0/jquery.js', '4d7b01c2f6043bcee83a33d0f627dc6fbc27dc8aeb5bdd5d863e84304b512ef3',\
			'C:\\JQueries\\1.9.0\\uncompressed\\jquery-1.0.0.js', 40)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.8.3/jquery.js', '756d7dfac4a35bb57543f677283d6c682e8d704e5350884b27325badd2b3c4a7',\
			'C:\\JQueries\\1.8.3\\uncompressed\\jquery-1.0.0.js', 41)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.8.2/jquery.js', 'cfa69516375e27e56519cae71f28818e0e52515b70e705a600d1db459998335a',\
			'C:\\JQueries\\1.8.2\\uncompressed\\jquery-1.0.0.js', 42)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.8.1/jquery.js', '7baae7dee44c0f5fc953e15dfce6027f639215c50e5c74259022f4ad847f2543',\
			'C:\\JQueries\\1.8.1\\uncompressed\\jquery-1.0.0.js', 43)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.8.0/jquery.js', 'd34161f2d90f01ef849956871690fe1e8bf15a4edbf7bab0a958bb9cbbe3760b',\
			'C:\\JQueries\\1.8.0\\uncompressed\\jquery-1.0.0.js', 44)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.7.2/jquery.js', '1717ea1fde8ceb7584341a24efc85c853083c660a1185968fbf94520f7193de2',\
			'C:\\JQueries\\1.7.2\\uncompressed\\jquery-1.0.0.js', 45)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.7.1/jquery.js', '9fcc241093405946885039df428cfa7f0051a1f2bdbcc5a313a177a9e35f8806',\
			'C:\\JQueries\\1.7.1\\uncompressed\\jquery-1.0.0.js', 46)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.7.0/jquery.js', '7c1885ec8620f40a10d045948d3f9f7b8f9c4f7bd2ff1ddfb486a9f27e95e3e3',\
			'C:\\JQueries\\1.7.0\\uncompressed\\jquery-1.0.0.js', 47)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.6.4/jquery.js', '54964f8b580ad795a962fb27066715d3281ae1ad13a28bf8aedd5d8859ebae37',\
			'C:\\JQueries\\1.6.4\\uncompressed\\jquery-1.0.0.js', 48)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.6.3/jquery.js', '9baa10e1c5630c3dcd9bb46bf00913cc94b3855d58c9459ae9848339c566e97b',\
			'C:\\JQueries\\1.6.3\\uncompressed\\jquery-1.0.0.js', 49)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.6.2/jquery.js', 'a57292619d14eb8cbd923bde9f28cf994ac66abc48f7c975b769328ff33bddc9',\
			'C:\\JQueries\\1.6.2\\uncompressed\\jquery-1.0.0.js', 50)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.6.1/jquery.js', '0eef76a9583a6c7a1eb764d33fe376bfe1861df79fab82c2c3f5d16183e82016',\
			'C:\\JQueries\\1.6.1\\uncompressed\\jquery-1.0.0.js', 51)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.6.0/jquery.js', 'a7c98da2a0260a5c8ac615cad956b8b220b7a2d73d85364dcf77b63f92e907b3',\
			'C:\\JQueries\\1.6.0\\uncompressed\\jquery-1.0.0.js', 52)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.5.2/jquery.js', 'e2107c8ecdb479c36d822d82bda2a8caf4429ab2d2cf9f20d5c931f75275403c',\
			'C:\\JQueries\\1.5.2\\uncompressed\\jquery-1.0.0.js', 53)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.5.1/jquery.js', 'e2ea0a6ca6b984a9405a759d24cf3c51eb3164e5c43e95c3e9a59b316be7b3b9',\
			'C:\\JQueries\\1.5.1\\uncompressed\\jquery-1.0.0.js', 54)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.5.0/jquery.js', '3613c89747be4a2d5dc17f442d0a482da665784e2e5a3931fb9a1fc38fa0fa8d',\
			'C:\\JQueries\\1.5.0\\uncompressed\\jquery-1.0.0.js', 55)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.4.4/jquery.js', 'b31cd094af7950b3a461dc78161fd2faf01faa9d0ed8c1c072790f83ab26d482',\
			'C:\\JQueries\\1.8.3\\uncompressed\\jquery-1.0.0.js', 56)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.4.3/jquery.js', '0e3303a3a0cec95ebc8c3cc3e19fc71c99487faa286b05d01a3eb8cca4d90bc7',\
			'C:\\JQueries\\1.4.3\\uncompressed\\jquery-1.0.0.js', 57)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.4.2/jquery.js', '95c023c80dfe0d30304c58244878995061f87801a66daa5d6bf4f2512be0e6f9',\
			'C:\\JQueries\\1.4.2\\uncompressed\\jquery-1.0.0.js', 58)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.4.1/jquery.js', '9edc9f813781eca2aad6de78ef85cdbe92ee32bb0a56791be4da0fa7b472c1d8',\
			'C:\\JQueries\\1.4.1\\uncompressed\\jquery-1.0.0.js', 59)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.4.0/jquery.js', '882927b9aadb2504b5c6a823bd8c8c516f21dec6e441fe2c8fa228e35951bcc8',\
			'C:\\JQueries\\1.4.0\\uncompressed\\jquery-1.0.0.js', 60)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.3.2/jquery.js', '233a5d16bee5a64bf3bc19abe3cc812a1e0619435f01c163f628773a469ff719',\
			'C:\\JQueries\\1.3.2\\uncompressed\\jquery-1.0.0.js', 61)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.3.1/jquery.js', '04175a2929f4d72b7cfc63be13103632e200ddb741c999cab76bed7775fd547d',\
			'C:\\JQueries\\1.3.1\\uncompressed\\jquery-1.0.0.js', 62)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.3.0/jquery.js', '5c44ebfc4b86e80fad397c5fb99fc35a0a97bbf6793dd295b224e46ea9bf2393',\
			'C:\\JQueries\\1.3.0\\uncompressed\\jquery-1.0.0.js', 63)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.6/jquery.js', '3cc5c121471323b25de45fcab48631d4a09c78e76af21c10d747352682605587',\
			'C:\\JQueries\\1.2.6\\uncompressed\\jquery-1.0.0.js', 64)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.5/jquery.js', '7b038f185fdf7611317c5714ff7ccfe83e768d2c5e6e80df8659210160321c37',\
			'C:\\JQueries\\1.2.5\\uncompressed\\jquery-1.0.0.js', 65)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.4/jquery.js', '94624d40721f1c352b2fecc802295da4d3083192fb2d7a1049b3aee26d8fdb7c',\
			'C:\\JQueries\\1.2.4\\uncompressed\\jquery-1.0.0.js', 66)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.3/jquery.js', 'd977fc32dd4bdb0479604abf078f1045b0e922666313f2f42cd71ce7835e0061',\
			'C:\\JQueries\\1.2.3\\uncompressed\\jquery-1.0.0.js', 67)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.2/jquery.js', '717d8d9b9802ac9fd75cc287c0624f37f9306c470c5a6da05abe9659d790e7cc',\
			'C:\\JQueries\\1.2.2\\uncompressed\\jquery-1.0.0.js', 68)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.1/jquery.js', '43b98f6d029d12c6a1623302b2d03b70799099641200965c006582d82d341b85',\
			'C:\\JQueries\\1.2.1\\uncompressed\\jquery-1.0.0.js', 69)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.0/jquery.js', 'e95be8c2affede53b586a32b2863aaa01870f120981367b2cf958951df2fdc67',\
			'C:\\JQueries\\1.2.0\\uncompressed\\jquery-1.0.0.js', 70)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.1.4/jquery.js', 'f00531f499c731c6985d4a460cced2fee38bda891d4820ce959dae7d78834812',\
			'C:\\JQueries\\1.1.4\\uncompressed\\jquery-1.0.0.js', 71)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.1.3/jquery.js', 'd374a0c5a109404028493a8685b62ec577dd1c55658bfff5cb54581ee5df219c',\
			'C:\\JQueries\\1.1.3\\uncompressed\\jquery-1.0.0.js', 72)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.1.2/jquery.js', '8be4bfe64c6e8c2c85f6a31e6a8b44bb7417dc9835873a83dfa4b0b8fa5c0f5e',\
			'C:\\JQueries\\1.1.2\\uncompressed\\jquery-1.0.0.js', 73)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.1.1/jquery.js', 'ebfead106f7529d2c976f6100d1223726cec07837f410f76026953b419d20944',\
			'C:\\JQueries\\1.1.1\\uncompressed\\jquery-1.0.0.js', 74)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.1.0/jquery.js', '582fd438f0901d64d06c63255d4d7dd8ac2a21767d5da7b51617da8c6851323e',\
			'C:\\JQueries\\1.1.0\\uncompressed\\jquery-1.0.0.js', 75)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.0.4/jquery.js', 'a1efd8aad160c17fd9afe1aca8e93bef444692988af58852dccdb1942fe3abb8',\
			'C:\\JQueries\\1.0.4\\uncompressed\\jquery-1.0.0.js', 76)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.0.3/jquery.js', 'b83a31e6bb8c91e113e18f899091e941dc21bfa4e4bcdbde133f2bee0aef4051',\
			'C:\\JQueries\\1.0.3\\uncompressed\\jquery-1.0.0.js', 77)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.0.2/jquery.js', '16d5d701bb80202ab68da7ccd88421a94818c42588cc6cf3a984129492d8dffc',\
			'C:\\JQueries\\1.0.2\\uncompressed\\jquery-1.0.0.js', 78)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.0.1/jquery.js', 'ec5129f542849aa777ee6054326a39b92b4dff3036c2055ffbf5f0249a6515e3',\
			'C:\\JQueries\\1.0.1\\uncompressed\\jquery-1.0.0.js', 79)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.0.0/jquery.js', '826c64c13cb636dc1596b19f78f11fc8aefd8792f00aa8151abb4b22528e73d7',\
			'C:\\JQueries\\1.0.0\\uncompressed\\jquery-1.0.0.js', 80)"),
	
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.12.4/jquery.min.js', '668b046d12db350ccba6728890476b3efee53b2f42dbb84743e5e9f1ae0cc404',\
			'C:\\JQueries\\1.12.4\\minifed\\jquery-1.0.0.min.js', 27)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.12.3/jquery.min.js', '69a3831c082fc105b56c53865cc797fa90b83d920fb2f9f6875b00ad83a18174',\
			'C:\\JQueries\\1.12.3\\minifed\\jquery-1.0.0.min.js', 28)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.12.2/jquery.min.js', '95914789b5f3307a3718679e867d61b9d4c03f749cd2e2970570331d7d6c8ed9',\
			'C:\\JQueries\\1.12.2\\minifed\\jquery-1.0.0.min.js', 29)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.12.1/jquery.min.js', '2359d383bf2d4ab65ebf7923bdf74ce40e4093f6e58251b395a64034b3c39772',\
			'C:\\JQueries\\1.12.1\\minifed\\jquery-1.0.0.min.js', 30)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.12.0/jquery.min.js', '5f1ab65fe2ad6b381a1ae036716475bf78c9b2e309528cf22170c1ddeefddcbf',\
			'C:\\JQueries\\1.12.0\\minifed\\jquery-1.0.0.min.js', 31)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.11.3/jquery.min.js', 'ecb916133a9376911f10bc5c659952eb0031e457f5df367cde560edbfba38fb8',\
			'C:\\JQueries\\1.11.3\\minifed\\jquery-1.0.0.min.js', 32)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.11.2/jquery.min.js', '2ecd295d295bec062cedebe177e54b9d6b19fc0a841dc5c178c654c9ccff09c0',\
			'C:\\JQueries\\1.11.2\\minifed\\jquery-1.0.0.min.js', 33)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.11.1/jquery.min.js', '540bc6dec1dd4b92ea4d3fb903f69eabf6d919afd48f4e312b163c28cff0f441',\
			'C:\\JQueries\\1.11.1\\minifed\\jquery-1.0.0.min.js', 34)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.11.0/jquery.min.js', 'b294e973896f8f874e90a8eb1a8908ac790980d034c4c4bdf0fc3d37b8abf682',\
			'C:\\JQueries\\1.11.0\\minifed\\jquery-1.0.0.min.js', 35)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.10.2/jquery.min.js', '0ba081f546084bd5097aa8a73c75931d5aa1fc4d6e846e53c21f98e6a1509988',\
			'C:\\JQueries\\1.10.2\\minifed\\jquery-1.0.0.min.js', 36)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.10.1/jquery.min.js', '4837f7e1f1565ff667528cd75c41f401e07e229de1bd1b232f0a7a40d4c46f79',\
			'C:\\JQueries\\1.10.1\\minifed\\jquery-1.0.0.min.js', 37)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.10.0/jquery.min.js', 'dbe2f39d679680bec02757226881b9ac53fb18a7a6cf397e2bbe6d4724c1c8e1',\
			'C:\\JQueries\\1.10.1\\minifed\\jquery-1.0.0.min.js', 38)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.9.1/jquery.min.js', 'c12f6098e641aaca96c60215800f18f5671039aecf812217fab3c0d152f6adb4',\
			'C:\\JQueries\\1.9.1\\minifed\\jquery-1.0.0.min.js', 39)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.9.0/jquery.min.js', '7fa0d5c3f538c76f878e012ac390597faecaabfe6fb9d459b919258e76c5df8e',\
			'C:\\JQueries\\1.9.0\\minifed\\jquery-1.0.0.min.js', 40)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.8.3/jquery.min.js', '61c6caebd23921741fb5ffe6603f16634fca9840c2bf56ac8201e9264d6daccf',\
			'C:\\JQueries\\1.8.3\\minifed\\jquery-1.0.0.min.js', 41)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.8.2/jquery.min.js', 'f554d2f09272c6f71447ebfe4532d3b1dd1959bce669f9a5ccc99e64ef511729',\
			'C:\\JQueries\\1.8.2\\minifed\\jquery-1.0.0.min.js', 42)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.8.1/jquery.min.js', 'fc184f96dd18794e204c41075a00923be7e8e568744231d74f2fdf8921f78d29',\
			'C:\\JQueries\\1.8.1\\minifed\\jquery-1.0.0.min.js', 43)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.8.0/jquery.min.js', '8c574e0a06396dfa7064b8b460e0e4a8d5d0748c4aa66eb2e4efdfcb46da4b31',\
			'C:\\JQueries\\1.8.0\\minifed\\jquery-1.0.0.min.js', 44)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.7.2/jquery.min.js', '47b68dce8cb6805ad5b3ea4d27af92a241f4e29a5c12a274c852e4346a0500b4',\
			'C:\\JQueries\\1.7.2\\minifed\\jquery-1.0.0.min.js', 45)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.7.1/jquery.min.js', '88171413fc76dda23ab32baa17b11e4fff89141c633ece737852445f1ba6c1bd',\
			'C:\\JQueries\\1.7.1\\minifed\\jquery-1.0.0.min.js', 46)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.7.0/jquery.min.js', 'ff4e4975ef403004f8fe8e59008db7ad47f54b10d84c72eb90e728d1ec9157ce',\
			'C:\\JQueries\\1.7.0\\minifed\\jquery-1.0.0.min.js', 47)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.6.4/jquery.min.js', '951d6bae39eb172f57a88bd686f7a921cf060fd21f59648f0d20b6a8f98fc5a5',\
			'C:\\JQueries\\1.6.4\\minifed\\jquery-1.0.0.min.js', 48)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.6.3/jquery.min.js', 'd3f3779f5113da6da957c4d81481146a272c31aefe0d3e4b64414fd686fd9744',\
			'C:\\JQueries\\1.6.3\\minifed\\jquery-1.0.0.min.js', 49)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.6.2/jquery.min.js', 'd16d07a0353405fcec95f7efc50a2621bc7425f9a5e8895078396fb0dc460c4f',\
			'C:\\JQueries\\1.6.2\\minifed\\jquery-1.0.0.min.js', 50)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.6.1/jquery.min.js', 'c784376960f3163dc760bc019e72e5fed78203745a5510c69992a39d1d8fe776',\
			'C:\\JQueries\\1.6.1\\minifed\\jquery-1.0.0.min.js', 51)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.6.0/jquery.min.js', 'e58da58b314ccdeefa3c4865b4b8aa3153e890d7904e04483481d8fff2c27eaa',\
			'C:\\JQueries\\1.6.0\\minifed\\jquery-1.0.0.min.js', 52)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.5.2/jquery.min.js', '8f0a19ee8c606b35a10904951e0a27da1896eafe33c6e88cb7bcbe455f05a24a',\
			'C:\\JQueries\\1.5.2\\minifed\\jquery-1.0.0.min.js', 53)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.5.1/jquery.min.js', '764b9e9f3ad386aaa5cdeae9368353994de61c0bede087c8f7e3579cb443de3b',\
			'C:\\JQueries\\1.5.1\\minifed\\jquery-1.0.0.min.js', 54)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.5.0/jquery.min.js', '229278f6a9c1c27fc55bec50f06548fe64c2629f59f462d50cac28e65bb93a83',\
			'C:\\JQueries\\1.5.0\\minifed\\jquery-1.0.0.min.js', 55)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.4.4/jquery.min.js', '517364f2d45162fb5037437b5b6cb953d00d9b2b3b79ba87d9fe57ea6ee6070c',\
			'C:\\JQueries\\1.8.3\\minifed\\jquery-1.0.0.min.js', 56)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.4.3/jquery.min.js', 'f800b399e5c7a5254fc66bb407117fe38dbde0528780e68c9f7c87d299f8486a',\
			'C:\\JQueries\\1.4.3\\minifed\\jquery-1.0.0.min.js', 57)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.4.2/jquery.min.js', 'e23a2a4e2d7c2b41ebcdd8ffc0679df7140eb7f52e1eebabf827a88182643c59',\
			'C:\\JQueries\\1.4.2\\minifed\\jquery-1.0.0.min.min.js', 58)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.4.1/jquery.min.js', '2cec78f739fbddfed852cd7934d2530e7cc4c8f14b38673b03ba5fb880ad4cc7',\
			'C:\\JQueries\\1.4.1\\minifed\\jquery-1.0.0.min.js', 59)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.4.0/jquery.min.js', '89abaf1e2471b00525b0694048e179c0f39a2674e3bcb34460ea6bc4801882be',\
			'C:\\JQueries\\1.4.0\\minifed\\jquery-1.0.0.min.js', 60)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.3.2/jquery.min.js', 'c8370a2d050359e9d505acc411e6f457a49b21360a21e6cbc9229bad3a767899',\
			'C:\\JQueries\\1.3.2\\minifed\\jquery-1.0.0.min.js', 61)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.3.1/jquery.min.js', '17ec1f16efac893b9bd89bba5f13cb1e0bf938bdc9cece6cae3ed77f18fa6fd7',\
			'C:\\JQueries\\1.3.1\\minifed\\jquery-1.0.0.min.js', 62)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.3.0/jquery.min.js', '900191a443115d8b48a9d68d3062e8b3d7129727951b8617465b485baf253006',\
			'C:\\JQueries\\1.3.0\\minifed\\jquery-1.0.0.min.js', 63)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.6/jquery.min.js', 'd548530775a6286f49ba66e0715876b4ec5985966b0291c21568fecfc4178e8d',\
			'C:\\JQueries\\1.2.6\\minifed\\jquery-1.0.0.min.js', 64)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.5/jquery.min.js', 'dba3ed2e85be82c9109419d15f948eaf3832fffce09376d8665e29105c28e9c6',\
			'C:\\JQueries\\1.2.5\\minifed\\jquery-1.0.0.min.js', 65)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.4/jquery.min.js', '99f3c010ca75e5169317a43115178e9f96b1e4ac31470e5508437d4e7b46747a',\
			'C:\\JQueries\\1.2.4\\minifed\\jquery-1.0.0.min.js', 66)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.3/jquery.min.js', 'f1c4a0a7b5dead231fc9b42f06965a036ab7a2a788768847eb81e1528d6402ad',\
			'C:\\JQueries\\1.2.3\\minifed\\jquery-1.0.0.min.js', 67)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.2/jquery.min.js', 'd3d0ff1c55ef3ac8aa1fbea3e61d550f3950a6729e03fcbfc1c3ef15241ba84e',\
			'C:\\JQueries\\1.2.2\\minifed\\jquery-1.0.0.min.js', 68)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.1/jquery.min.js', '18ab106814b6251057c7b739d818b43887b443c42b8f488a052aeeaa4cea6b1f',\
			'C:\\JQueries\\1.2.1\\minifed\\jquery-1.0.0.min.js', 69)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES ('1.2.0/jquery.min.js', '100e1a173a6113218ffb49e13a14778fa3b91ff7fcd9fac5c523baedb0f1b7fb',\
			'C:\\JQueries\\1.2.0\\minifed\\jquery-1.0.0.min.js', 70)"),

	# insert data for library 2 - jquery-migrate table
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES('3.4.1/jquery-migrate.js', '09f417c2e643b736c19e96b99e166681af1002e9b192b84e4e85b0794e764f7f','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.4.1.js',81)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.4.0/jquery-migrate.js', 'd0d91bd741e7866e04259d100e9bc89dcddb469efbc1021b210996607dd8ed5c','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.4.0.js',82)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.3.2/jquery-migrate.js', '0439ad37eefd551ae47da9b30f5e949c0a093fcccc8ad033d3ddedbd90137621','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.3.2.js',83)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.3.1/jquery-migrate.js', '946b94a8950f5c910c8105ff45168cea66642baa27a398b96c7b81304e2a382a','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.3.1.js',84)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.3.0/jquery-migrate.js', '2c78abbdfd0a760eb8d5f8de8f0e1076520f3d82ad4aa1e80d4a5451e4e71ccb','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.3.0.js',85)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.2.0/jquery-migrate.js', 'f979de8f3b6ac64b524e6b0585970c6bc6389f5b4fe7e54fca16b336762a6f04','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.2.0.js',86)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.1.0/jquery-migrate.js', 'a00fe5b190a010f91bbff6f20247974931194ec18e3d90abb5bc8504799c18a3','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.1.0.js',87)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.0.1/jquery-migrate.js', '56f9c5f99829774d0b2fbdcfd9750b617127e913afa0569afef6dfa22165659e','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.0.1.js',88)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.0.0/jquery-migrate.js', '96c54e07edd8866e877b93244cedc1c3f5f0e0d5caef06184e2d58f8cff63eb3','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.0.0.js',89)"),

	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.4.1/jquery-migrate.min.js', '5274f11e6fb32ae0cf2dfb9f8043272865c397a7c4223b4cfa7d50ea52fbde89','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.4.1.min.js',81)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.4.0/jquery-migrate.min.js', '9810aee7e6d57d8cceaa96322b88e6df46710194689ae12b284149148cabc2f3','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.4.0.min.js',82)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.3.2/jquery-migrate.min.js', '029e0a2e809fd6b5dbe76abe8b7a74936be306c9a8c27c814c4d44aa54623300','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.3.2.min.js',83)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.3.1/jquery-migrate.min.js', '00f96531cd15e257ff45be42cf889d5940989410c6ddbd0470dd54b217778691','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.3.1.min.js',84)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.3.0/jquery-migrate.min.js', 'c19def3576a41fd9383f4d1f3460256cdd0f929292ca145aefa205cb85753d81','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.3.0.min.js',85)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.2.0/jquery-migrate.min.js', 'b7ef1cb811f8db4e4c611032cf3b24d2c1256bf9794123b41ae4dea331eb54d6','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.2.0.min.js',86)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.1.0/jquery-migrate.min.js', 'c9c25e5db965f66edd1ca79a3db5c19191fc06e3fdf5298f9bff2ae4ef926c17','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.1.0.min.js',87)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.0.1/jquery-migrate.min.js', '1743b54e611ae08f0ddb89d8d1bc9ae7d78feacbd672c86a5f5bb3c1a582e05e','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.0.1.min.js',88)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('3.0.0/jquery-migrate.min.js', '26494360e0db8345fef2c3e22a47055116f9cfb46f94d308684dd1036cfdeefc','C:\\JQueryMigrate\\3.0.0\\minified\\jquery-migrate-3.0.0.min.js',89)"),
	
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.1/jquery-migrate.js', 'c68a880944aa03082e88bbe6c7df7747ee45f506fa777e76fb41709a0ba5a935','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.4.1.js',90)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.0/jquery-migrate.js', '0f2b4c09062e99defd9cffa916147eaada93554fd252325264fd86648944a1e6','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.4.0.js',91)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.0/jquery-migrate.js', 'fc68fe365635bbf276506cccfc1d90ad6474d6dacaf1966aac3e4176a414b1a7','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.3.0.js',92)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.0/jquery-migrate.js', '356a8df4c95948ea9ba2c413759c033b890dd66d68991475a9184a4ce401ce12','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.2.0.js',93)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.1/jquery-migrate.js', 'fd23ab8ce969cdbc761e041f63d763e11a5864a5428e61d006042f5a49464334','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.1.1.js',94)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.0/jquery-migrate.js', '89f6e1276ff8e3b85ffaadce17ee1ea2171e2f8f9454c224793d9290ab57060f','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.1.0.js',95)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.0/jquery-migrate.js', 'd9b635248efd4b596cad402579c29a619b4379cfb553a32589350b04c07f2bfa','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.0.0.js',96)"),

	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.1/jquery-migrate.min.js', '48eb8b500ae6a38617b5738d2b3faec481922a7782246e31d2755c034a45cd5d','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.4.1.min.js',90)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.0/jquery-migrate.min.js', '9f176243815d4e6dbc79434d408273e49a1d4cc085e7f977da0e4bc1f530654a','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.4.0.min.js',91)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.0/jquery-migrate.min.js', 'fbf432b5b2d82b5afa000a663ebc21817c3bbb3e2ef47d44eb973ce575b21d1a','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.3.0.min.js',92)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.0/jquery-migrate.min.js', 'd700b745899949951caa29d5a442f14933ca3a2ff5e69fe84131ec490ea46834','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.2.0.min.js',93)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.1/jquery-migrate.min.js', 'accc55ec16d4936f2b833342cc1291655a1638fc823541e0bf5347c7f1d63354','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.1.1.min.js',94)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.0/jquery-migrate.min.js', '78c059bc96d22f347342363fbf53cfe9ffc2ff49c9d04f9dbe760c87f276c5ce','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.1.0.min.js',95)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.0/jquery-migrate.min.js', 'bc5c3fd6f35abb7ebbe143e47c55d726b5ddc3c127c8002123c15c0cae7ee122','C:\\JQueryMigrate\\1.0.0\\minified\\jquery-migrate-1.0.0.min.js',96)"),

	#entering data in table 3  - underscore.js 
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
		VALUES('0.1.0/underscore.js', '1e92921274b205f5c5167f7ff2cbd746bff20a3af1f5d063747a251f16b4573d','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.1.0.js',97)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.2.0/underscore.js', 'c9590d95f4717b55e97217d9054e4ef6f7835cb607fe9f51445f1ae975f45ac9','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.2.0.js',98)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.3.0/underscore.js', '3f8b1f7f37f87d851f6668d5cad8f92f99e60a89716e94bf925325cd08db7d9c','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.3.0.js',99)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.3.1/underscore.js', '7ecd3fdd325ed9377e6cef7af2701cfa5a1566085d54c89932aa9da693a79771','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.3.1.js',100)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.3.2/underscore.js', '9367560d6b25d558c2e1a5e8087beabac03844b8bf4ae84bb989664338bce718','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.3.2.js',101)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.3.3/underscore.js', '131d3939e0f5ff804f118cb62f06f36de53fa2b49c801ef167d57f22ec6a727a','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.3.3.js',103)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.0/underscore.js', '0584351f0a049252296d5d2000b94dcb1072445e396d5ff018121b315f9faa89','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.4.0.js',103)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.1/underscore.js', 'cdf5129c47b8b73c11d23eef0f9ac2c73303cc2a9e52f8f31066b29e6a305add','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.4.1.js',104)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.2/underscore.js', '2271e12e69d4752b68ea4d97e563d98a187317bdc1211bf5d7d38db1ff40c48a','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.4.2.js',105)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.3/underscore.js', 'c3d129c172470281e980bfcfa9f309ea92ad7ce77ba7ce612245d41a17b111f8','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.4.3.js',106)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.4/underscore.js', 'ca146bb20087edc16887edb004bde5dce56b91e9c4b4d51cb9ac7e16c03a7466','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.4.4.js',107)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.5/underscore.js', '33af9ff74f2b78822c24e24c7aacbd3e5f6509a1f0d7b6d97c56070ef5daedef','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.4.5.js',108)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.6/underscore.js', '0c54c1f6901efabc51287b1742006864abe43bf1088e04d833d4f55d2184120c','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.4.6.js',109)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.7/underscore.js', '4cc5319afcffff9822b2881a70afc34f27c4d439b88add1e95e4587930a67487','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.4.7.js',110)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.0/underscore.js', '49749c2593b419be7b828aed23304650faefefe83874cce9daac5a21cda85d89','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.5.0.js',111)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.1/underscore.js', '2c65f20705e9215f6ff7c81cc7635db9a092a4e15c5cc84c5954ac832f65a11b','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.5.1.js',112)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.2/underscore.js', '06dea7c64da176e497435c24a9ab90c18705e4c95f01018b3b47719f8c3089e9','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.5.2.js',113)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.3/underscore.js', '677c7845b81df2f260d6ee6985c45d97d96de4be6b8629c225b335c4e931ccad','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.5.3.js',114)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.4/underscore.js', 'eb1b53350a8c63533f626c568f3448143fb2f39c0976fb202ac08b98c04a20a5','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.5.4.js',115)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.5/underscore.js', '5c712a46736d6b5066fa20f19069f43b24f3a9660572b4064b1899521f56bed8','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.5.5.js',116)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.6/underscore.js', 'c5ee7a4d2ddc6fdadcbe3f917c230fbe186584dc6dd40e69dc0dbc908f214b45','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.5.6.js',117)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.7/underscore.js', 'b6088f2ca702af07fca025f4e9d96c950f42ffc916d00539684926243c7ae569','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.5.7.js',118)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.8/underscore.js', 'b2f5430c7c0f2422ea27fe06603d2fc7036b81a2c9a9ebe0675d018413b32f3a','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.5.8.js',119)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.6.0/underscore.js', 'd20d94e6c7dce8284af82c64f8deaa39085b4e18c3ff4096811c09f5e457c87e','C:\\UnderscoreJS\\0.0.0\\uncompressed\\underscore-0.6.0.js',120)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.0/underscore.js', '2481bcf7ecd425ae55874057efaabbf741565b93e3e0612190774931bbe74c58','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.0.0.js',121)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.1/underscore.js', 'eca2e496fbc8920b9b72363afe85d071e2bc58619f7075e276053c55b4c2297f','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.0.1.js',122)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.2/underscore.js', '2d927ca2dafbe1b3122e5f604fbf8dfc82f98b670e3bc3685e78eb5a46c86564','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.0.2.js',123)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.3/underscore.js', 'abe29f5213216c659c3cf2f0c02f279fd30ad351818b3616460f082e934b9d1c','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.0.3.js',124)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.4/underscore.js', 'b63ef97b9f85b0d4a07926b186083c9952568e26bbb65d610b592d15208f79a9','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.0.4.js',125)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.0/underscore.js', 'a646f62263e789d12b4d0fab38972f78ed8be6b0e358674dace79ac974225e1d','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.1.0.js',126)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.1/underscore.js', '27875e0a6e29e5471d73333b2c27ee85f17aa2ae8001a40a37faa3187fcf29c7','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.1.1.js',127)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.2/underscore.js', '52514ce8ed887e2978e039e61a5483fb7adb5a7e7c57f351be6af32270730531','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.1.2.js',128)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.3/underscore.js', '7fa6e7d6318dc2c336ae8a8c29cc11027e7db4e1e9890e8a08424c1d73031d96','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.1.3.js',129)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.4/underscore.js', '9198aab9eeab6562fd7fa74a022ba239d88a7c64e05acb4c781c9670229186b2','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.1.4.js',130)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.5/underscore.js', '6a52dcbe60c61158795cc9f023063121c11ce862b3e8dd71150523cc8d15ced1','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.1.5.js',131)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.6/underscore.js', 'ca05baf248bc3d7cb0200552785603b8995b132d886a68e75a5fe8bc338198c8','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.1.6.js',132)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.7/underscore.js', 'b81b571bbc77c027807e0f0cdbf7834c273bbc36069d560f83960472cba2428b','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.1.7.js',133)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.0/underscore.js', '420e5861e1bc03a5a93660256af02d3c7de7fbce2fa5f07183521a5d22231117','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.2.0.js',134)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.1/underscore.js', '2e2e4a7d2772c9d1ddfab745f5f973b59b4ed741c51b994334bebc454af041ca','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.2.1.js',135)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.2/underscore.js', '9836e801c314da41ebffb09a46eb0d313e76d4aa5242f7c3fff8a3a20bd45038','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.2.2.js',136)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.3/underscore.js', '22729344b976cc44fed6bb389059a647ceb8a0b89ae5c5120e6f42ecc2522b0b','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.2.3.js',137)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.4/underscore.js', 'f53f5b8c13f99c295f48b756cb23b2803246b346dd4605d396bcfce31a60fdf9','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.2.4.js',138)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.0/underscore.js', '6422a2fa2f0f31c185c169bd31366c93fa885f554ad5e7e3a4c23d6742a1d5de','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.3.0.js',139)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.1/underscore.js', 'f808f0aa32fbe90fb9c9c846917faff3fdd4e236c284b76c02dd33753dc90177','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.3.1.js',140)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.2/underscore.js', '35b15b04a8110f2631529d32d093d6c7c1007b05f71f649c64f31b0beae61aca','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.3.2.js',141)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.3/underscore.js', '49f14bad610f40f0ae76a33c55ef89a1e694219bab49b1b99cb53d754774c0fc','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.3.3.js',142)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.0/underscore.js', '1258fb3ec5df4f2fa771d26aff20a07e9b71f1c08dfd45c86fc00ed8f0326c69','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.4.0.js',143)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.1/underscore.js', '3eec9a11de61554b41d142f57ea610747e44699338e2b471f1109548ac0597b7','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.4.1.js',144)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.2/underscore.js', 'f7852d7466f17019073cb7a1a794a30b91b13f01cc49774f4075a695270c0a3b','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.4.2.js',145)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.3/underscore.js', 'a10aa2eb9078c2e19f181ac722b1c19a29b8db1069556c508a3beb5c46289d7b','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.4.3.js',146)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.4/underscore.js', '32037dee4499126b99715750145392c8b00a7db213b2052e7032afb10fadd5da','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.4.4.js',147)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.5.0/underscore.js', '57fbeb550df02488a31a2f279f41cffe469ba3c836042a35d03492385227e53c','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.5.0.js',148)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.5.1/underscore.js', '484e5a48a1d1eafdf4cfaeacafea998c3a43d25b6277ce0bd29737f5d081b598','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.5.1.js',149)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.5.2/underscore.js', '023f31d6996b4ff1b3543fea50be852ecbdbdce8b9e8d0610b72918e1f9d91c3','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.5.2.js',150)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.6.0/underscore.js', 'ee8ba6b58a9c67d9f7148b31f90851767c45aeaa8c86fbf7e981ba255d39240b','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.6.0.js',151)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.7.0/underscore.js', '53596846ab864b5bc4e4605181ad18feac56662185de74eff3373e98508cf0eb','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.7.0.js',152)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.8.0/underscore.js', 'c45c8504a0e57560128479b578e703f9533b6d56feaee5c773030138a3d3b4a1','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.8.0.js',153)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.8.1/underscore.js', '13332633f2eae3147df1ca250381a2dc391a68b353a383b2805f901d4c67923b','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.8.1.js',154)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.8.2/underscore.js', 'b84a7a5ac0e8afc4f176b95606590bfc56044eeae9286097bdee013a6909fde5','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.8.2.js',155)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.8.3/underscore.js', '4b328e42c558197d5b99d7727cfcc60bac9763fad660651230e8baf93f6067ed','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.8.3.js',156)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.9.0/underscore.js', '51aa76b532ba52182c46386e5bd2df155103d3abcd49300c7ecb6bdc7d93a25b','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.9.0.js',157)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.9.1/underscore.js', '3b8d7bf449fccda6ce94f60136f1a9f1c174ba1d2f9d26695b843a525d61fbc7','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.9.1.js',158)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.9.2/underscore.js', '716f46856dfd3d43a2848e33c91248516c3284c45e341e910e62f02fb926882e','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.9.2.js',159)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.10.0/underscore.js', '1c6728a3d862b85c33cefce07c6652c3301d98a5664fa1e2fb53732a9af4256b','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.10.0.js',160)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.10.1/underscore.js', 'a876a5e66659878bee48446fdfdcf9a11e9cde905e4f2c73ac966435ea5b1eee','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.10.1.js',161)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.10.2/underscore.js', '1445bbc252e10d7a7aab5d679a29b398b4a446ad9cc9712d63bb6eadee7c989d','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.10.2.js',162)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.11.0/underscore.js', '4136c101522c2915d8bd5d47e807d1b5fb02712ec51e893cf1dd4a3e39af68bf','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.11.0.js',163)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.12.0/underscore.js', '9964412824ab0ffe530e8019cf330e2aa2c3eacea489fe387f909e12c0f0d433','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.12.0.js',164)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.12.1/underscore.js', '7ad808820e110c0c96c0c551cfb75a9aa7d36aa2653dda02be57f07a2f7eebd7','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.12.1.js',165)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.1/underscore.js', 'cc10f799cd0f6b65f95c4012445497e5ba3cb9f51964a9468940b27bde98b487','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.13.1.js',166)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.2/underscore.js', 'ed34e97cd4a4e8e0eecc3ac156f5bc4ee78ebdd9f9f8417635102bbe13b189cb','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.13.2.js',167)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.3/underscore.js', '586128266de6b7401289f79caa3b3e38d12eda388422c43a1757d347e36b7e61','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.13.3.js',168)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.4/underscore.js', '03203363ad99fc8de92e0096e1419ff416909cb9e6d1d7e05e64905387d1949f','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.13.4.js',169)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.5/underscore.js', 'dc2b5d97ad0674a81c7916ff790669c5997e3958ee8b37cdea450e083194ab76','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.13.5.js',170)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.6/underscore.js', '56bf845439057fbf61e9925905b3c5bea88886604189dcb5312bd5281e4415f5','C:\\UnderscoreJS\\1.0.0\\uncompressed\\underscore-1.13.6.js',171)"),

	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.1.0/underscore.min.js', 'a444f56b999ff046d62f604efc34fe58e477a75881399bc5ed78217399b3d84d','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.1.0.js',97)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.2.0/underscore.min.js', '3f7df2dd7c8ff21b0d72f4d1ae3c0903e46c582c830d058aedd84632d5e3967f','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.2.0.js',98)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.3.0/underscore.min.js', 'd8e7484b23bbd8265ee4041b7eeb26aaf04239a5e242e0effb0571d4feed657d','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.3.0.js',99)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.3.1/underscore.min.js', '0806da0eee2c9772c8701052a6573977cf66c2e2d4f47e25b061275d5069d851','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.3.1.js',100)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.3.2/underscore.min.js', '45ad86935ef1512cf25dd81ef9c007199339624629e4dbe22d66df953a19e87a','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.3.2.js',101)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.3.3/underscore.min.js', '06f94f5e768e974bf1eae25fdf78f3e593323b79f850e6efdd509ff9728c7491','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.3.3.js',102)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.0/underscore.min.js', 'd944041291f92748cf4bc0428588c764bec4031905a3932b333220fae577a572','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.4.0.js',103)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.1/underscore.min.js', 'a54492496c7c6fe2acdeb30acf9d86c77e644df4f474638d90207cb951be4f07','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.4.1.js',104)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.2/underscore.min.js', '340642c78d53a4206d48fb0fcbb2e72520b0c6f786b11be0c436ffaf62f9c47e','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.4.2.js',105)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.3/underscore.min.js', '153dcb9a741d2d9a000b51b4a891938272688724bdc07add3d1802a712e8c747','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.4.3.js',106)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.4/underscore.min.js', '972fc0264a13f9beb290f2394f9c490ebb3275b585591b7e49dc2e42b6f49875','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.4.4.js',107)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.5/underscore.min.js', '12a5cf24abdc0f2d03c729aabda04300ce9c8ed46b82b94e10e07cbf1d7b527b','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.4.5.js',108)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.6/underscore.min.js', '90c1eae7896407aee774b1fd72ac1905afb25ee2c6843afeeef57167b8c8202c','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.4.6.js',109)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.4.7/underscore.min.js', 'b95568a49cf9c45dce1418f774e741d2d68f6c03c59e2e5caca8337f5868dc5c','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.4.7.js',110)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.0/underscore.min.js', 'e675194aaec0f1accc3d8d0d4216f5d7f045844eff3ae4d14547238b0227af3b','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.5.0.js',111)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.1/underscore.min.js', '15f0ffc7366d51dce455367d7a6520fa28e0b4c30e2085d68809d722925276ce','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.5.1.js',112)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.2/underscore.min.js', '1ed91ae59335cd8592ba20615cd3cbd072fdb7c8b7180f7b8cfcd1ef7a0c52b8','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.5.2.js',113)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.3/underscore.min.js', '84bf79f9a2144e5d684618786d1aa23abf6794a7ad2db1c2bffd89ebe1d497f5','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.5.3.js',114)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.4/underscore.min.js', '549f874385e98c38e9dc7be52a20a134edb204743172f230eed8abca767ade91','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.5.4.js',115)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.5/underscore.min.js', 'cae3580d9e4640a83be69b8d78d74f9b5b7602ea0eb380323cbd955d79329c4c','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.5.5.js',116)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.6/underscore.min.js', 'cf60130f04ef4c8db84851e917673b883f52a1728c1f228d0df09b2b85f93412','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.5.6.js',117)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.7/underscore.min.js', '6b56a1d06ab640c7b5be754f834a14985a0158292d4e3e2b77424a1ab3c2798c','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.5.7.js',118)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.5.8/underscore.min.js', 'cd59ec1995c8058820620f6c8648a1f4b61af2b65ce63d0fa70efa8576808c03','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.5.8.js',119)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('0.6.0/underscore.min.js', 'daef73caf247f00b990b30d57fe2e8961cc9f706bad627ae786d8536accd2590','C:\\UnderscoreJS\\0.0.0\\minified\\underscore-min-0.6.0.js',120)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.0/underscore.min.js', '84a3280c36567b81d7bbfc395704d410875f297fbf9e26564560ac8aabab496c','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.0.0.js',121)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.1/underscore.min.js', 'cb725f2712784873cb44915c807ca75522fb175eb81440198ee81555267852da','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.0.1.js',122)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.2/underscore.min.js', 'de12e081e16488205fb40849632c52de29e0fe0c8e771563f10af8f76e4958c0','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.0.2.js',123)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.3/underscore.min.js', '729ecd8f55e795f50fe5b1d757e9c82274d746e9977d24ee91451ef26091feb8','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.0.3.js',124)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.0.4/underscore.min.js', '0aa898048336d9c8983e3c63c282e7e3ff1a328ddbfa9fd7b44ea2d04e8b7ad2','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.0.4.js',125)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.0/underscore.min.js', '84b6fed71c0ffd48254f28cd21762849c78d837d07ce034c937a03efc7e2f83e','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.1.0.js',126)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.1/underscore.min.js', 'f25e76a45025e589976578cf27d22091f5d89d5e47a68372f6b3a521d371b04b','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.1.1.js',127)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.2/underscore.min.js', 'daa17b2aec40a550d1c0824ddfcc989fa607b4c4b4f115a7413df22b3b343f8f','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.1.2.js',128)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.3/underscore.min.js', '93f9f6be963fbb163722dbf17b0f916d68523506eaf36757ecce741dd0e41eaa','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.1.3.js',129)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.4/underscore.min.js', 'dd1890ef89f59d38b2478e76dc362e139f17af5bdc81c47bfc1110cdfc14c4d0','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.1.4.js',130)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.5/underscore.min.js', 'b47c3e3341e50192c433872310fef0a41bcfdcdd8d637fd7aa0a7f6bad40cbc8','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.1.5.js',131)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.6/underscore.min.js', '906c72aff6a58625cdc31d47df29d6f0adecbcad2a56b42876d660acb247aba5','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.1.6.js',132)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.1.7/underscore.min.js', 'efcb9871d25921b09b15b52196189a7efbe6ef01e67e3015bfd31c90537aa350','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.1.7.js',133)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.0/underscore.min.js', '0e9fe368d777cd4bc5580a1e570128c5f1564c09ae8b6ae0ef7fa7c8d6106a40','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.2.0.js',134)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.1/underscore.min.js', '5363c436871957e5b2a4dea399545feda648db13d0414910cc1acee12f05cdab','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.2.1.js',135)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.2/underscore.min.js', '42d6c56d8a983ca98112fdc9e75688c34bedd9d1308e5740deb71993d6c1ae3a','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.2.2.js',136)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.3/underscore.min.js', 'dd5a5741cf628f152ad39dadca9aeef15c19ac3de69ecf41b4321b577641c056','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.2.3.js',137)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.2.4/underscore.min.js', '5e88c8fd49ad0a719f6f2adc71d650e7c201bbcfbe46fdf532fbfce23fcc23b6','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.2.4.js',138)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.0/underscore.min.js', 'b832c2eccf70ade054d627651551196e016e9e3d6a35282afcceb7aa7ff99c41','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.3.0.js',139)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.1/underscore.min.js', '42d8fad13bc28fc726775196ec9ab953febf9bde175c5845128361c953fa17f4','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.3.1.js',140)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.1-amdjs/underscore.min.js', '97af66f1c8fc249ce40007680481e40e82aac62c14e06ee03907eb6a2316d01e','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.3.1-amdjs.js',172)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.2/underscore.min.js', 'f5300eb60743a9b5f5e015cfa3a29cc187051cb6c8097e821164c1cad2f86cc7','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.3.2.js',141)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.3.3/underscore.min.js', '0f201fe52208471c863c292da4990ca7bb7ca5d58b3f1ea2a57095ff764c6848','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.3.3.js',142)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.0/underscore.min.js', 'faab51654de7d65c0cab1e32c0403a7752e0e6a4cccb433d823d4a1de563c515','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.4.0.js',143)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.1/underscore.min.js', 'ab0d4345dc2801d2667ff3a0ae25926d20154ba7540f6797ad4baab4681e2fa8','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.4.1.js',144)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.2/underscore.min.js', '03ae3ad62082d4e7443de69006761d2e59b49e7f11bc209b8a5a01762d28d6b2','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.4.2.js',145)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.3/underscore.min.js', 'c53816234c2fd19da23c01faa3b01169a1c38bc466bcd9a282a019861a84bbb8','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.4.3.js',146)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.4.4/underscore.min.js', '27829b1d29e3fb532d761987d4057275d1e9ecdd3eaf4b4c40a29382590b820e','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.4.4.js',147)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.5.0/underscore.min.js', '817af2c86f48426d2756c83fbdf86bc2b4993e4f377d9e4b6c708aa669ab0dc5','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.5.0.js',148)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.5.1/underscore.min.js', '0b44e36460d066ba2e00a4f1a0adb193ca14a99ce5c2222099a4247ba6ee9f01','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.5.1.js',149)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.5.2/underscore.min.js', 'f205111f00aa36a51e6b312a74e58abc82394f207e48af4d596680b2a0125c2a','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.5.2.js',150)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.6.0/underscore.min.js', '163189ef69a3c210a04bb4cac2c336119d78b576fb84b4231977514419eb0faf','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.6.0.js',151)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.7.0/underscore.min.js', '7b6fbd8af1c538408f2fe7eef5f6c52b85db12ab91b63277287e5e9ea83a4931','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.7.0.js',152)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.8.0/underscore.min.js', '6e5582e8b2817eecbc135f2b1c312ec5e6a7217c7eafc658423c939b87c9134d','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.8.0.js',153)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.8.1/underscore.min.js', '8b7dbdfa7de515cdc794dfdef15b63c2cc3228f7ff26670494b0f7d089b86f38','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.8.1.js',154)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.8.2/underscore.min.js', '2de19ea3b85e03239dd9cbe30d9545a1b5a7ce2f0662feaeaf3d2d088179ea5c','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.8.2.js',155)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.8.3/underscore.min.js', 'a1b6400a21ddee090e93d8882ffa629963132785bfa41b0abbea199d278121e9','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.8.3.js',156)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.9.0/underscore.min.js', 'b6be05bd7559a7c9e45bb4ef5b83980392963acedf7369b907a2cdf803a7d552','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.9.0.js',157)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.9.1/underscore.min.js', '1bb03826b26326516a3f4c9a9b39f03e3000a4828f91a75e1dfc88c2269af5ed','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.9.1.js',158)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.9.2/underscore.min.js', '22b404d34700979e4c9746c855a72f38d926d317ca16336e1e24614664a6ff2e','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.9.2.js',159)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.10.0/underscore.min.js', '1e4b1c5d112131699d84de1eb61be01927f23ee11d5f6c6accca92063a75fa95','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.10.0.js',160)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.10.1/underscore.min.js', '2c00a9b27d8c5ea118596358bcd93e4ca765a97ba133e4106f9153ea58da9359','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.10.1.js',161)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.10.2/underscore.min.js', '6afd53bf2c2d67866ac828ffe8776d087489767f341c0cd380405326dfcef2e7','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.10.2.js',162)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.11.0/underscore.min.js', 'd62f9c89984ad059d574ae6b64c9134628041695c09290643e2d53238638bdda','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.11.0.js',163)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.12.0/underscore.min.js', '1bc0ea4e2fe66ac337fb1863bbdb4c8f044ee4e84dbe0f0f1b3959bebfa539c1','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.12.0.js',164)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.12.1/underscore.min.js', '326d2fe3bd8343f6167fdbcb4e3e83e1dfdb2cfa538c4e832c1b5948acecbe18','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.12.1.js',165)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.1/underscore.min.js', '218fb1c1fc72e9af6b866f430be2a67fa376392b4db2f4dbf32772671b6ae55c','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.13.1.js',166)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.2/underscore.min.js', '16ef4ffef8378d986b83eff6c680fdc90a76b525ce89a11280f814fc7f62302a','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.13.2.js',167)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.3/underscore.min.js', '1e8f79ce8eee1b5b04c6fb9130eae9e9d4ff042d28d82a6a154b36c06dd71dae','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.13.3.js',168)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.4/underscore.min.js', '640f1d5e961c8aab91b9338c816111a1e80b7ebbc5666f184e647306fd17e697','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.13.4.js',169)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.5/underscore.min.js', '6d2610a0242298f377adba0184469e2554a1ba07d5804119e245f3eb55fa3c3f','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.13.5.js',170)"),
	conn.execute("INSERT INTO variant (fileName, hashKey, content, versionID) \
			VALUES('1.13.6/underscore.min.js', '25f436e933246f279adc4967725a4d915e0fc7a6419d3b956a945bb5782dc6e5','C:\\UnderscoreJS\\1.0.0\\minified\\underscore-min-1.13.6.js',171)"),
			
	#inserting data in table 4 
	#jquery data entry - lib 1
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.js ', 1)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.js', 2)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.js', 3)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.js', 4)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.0/jquery.js', 5)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.js', 6)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.0/jquery.js', 7)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.js', 8)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.0/jquery.js', 9)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.js', 10)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.js', 11)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.js', 12)"),

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js', 13)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js', 14)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.min.js', 15)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js', 16)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.0/jquery.min.js', 17)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js', 18)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.0/jquery.min.js', 19)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js', 20)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.0/jquery.min.js', 21)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js', 22)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js', 23)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.min.js', 24)"),

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.slim.js', 25)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.slim.js', 26)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.slim.js', 27)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.slim.js', 28)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.0/jquery.slim.js', 29)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.slim.js', 30)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.0/jquery.slim.js', 31)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.slim.js', 32)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.0/jquery.slim.js', 33)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.slim.js', 34)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.slim.js', 35)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.slim.js', 36)"),

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.slim.min.js', 37)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.slim.min.js', 38)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.slim.min.js', 39)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.slim.min.js', 40)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.0/jquery.slim.min.js', 41)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.slim.min.js', 42)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.0/jquery.slim.min.js', 43)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.slim.min.js', 44)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.0/jquery.slim.min.js', 45)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.slim.min.js', 46)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.slim.min.js', 47)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.slim.min.js', 48)"),

		
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.js', 49)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.3/jquery.js', 50)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.2/jquery.js', 51)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.1/jquery.js', 52)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.0/jquery.js', 53)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.js', 54)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.js', 55)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.2/jquery.js', 56)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.js', 57)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.0/jquery.js', 58)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.js', 59)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.2/jquery.js', 60)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.1/jquery.js', 61)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.0/jquery.js', 62)"),

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js', 63)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.3/jquery.min.js', 64)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.2/jquery.min.js', 65)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.1/jquery.min.js', 66)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.2.0/jquery.min.js', 67)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js', 68)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js', 69)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.2/jquery.min.js', 70)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js', 71)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.0/jquery.min.js', 72)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js', 73)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.2/jquery.min.js', 74)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.1/jquery.min.js', 75)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.0/jquery.min.js', 76)"),

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.js', 77)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.3/jquery.js', 78)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.2/jquery.js', 79)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.js', 80)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.0/jquery.js', 81)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.js', 82)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.2/jquery.js', 83)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.js', 84)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.0/jquery.js', 85)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.2/jquery.js', 86)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.1/jquery.js', 87)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.0/jquery.js', 88)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.js', 89)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.0/jquery.js', 90)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.3/jquery.js', 91)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.2/jquery.js', 92)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.1/jquery.js', 93)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.0/jquery.js', 94)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.4/jquery.js', 98)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.3/jquery.js', 99)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.2/jquery.js', 100)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.1/jquery.js', 101)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.5.1/jquery.js', 104)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.4/jquery.js', 106)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.3/jquery.js', 107)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.2/jquery.js', 108)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.1/jquery.js', 109)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.0/jquery.js', 110)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.2/jquery.js', 111)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.1/jquery.js', 112)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.0/jquery.js', 113)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.2.6/jquery.js', 114)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.2.3/jquery.js', 117)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js', 131)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.3/jquery.min.js', 132)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.2/jquery.min.js', 133)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.min.j', 134)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.0/jquery.min.j', 135)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.min.j', 136)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.2/jquery.min.j', 137)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.min.j', 138)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.0/jquery.min.j', 139)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.2/jquery.min.j', 140)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.1/jquery.min.j', 141)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.0/jquery.min.j', 142)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.min.js', 143)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.0/jquery.min.js', 144)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.3/jquery.min.js', 145)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.2/jquery.min.js', 146)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.1/jquery.min.js', 147)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.0/jquery.min.js', 148)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.7.2/jquery.min.js', 149)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.7.1/jquery.min.js', 150)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.7.0/jquery.min.js', 151)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.4/jquery.min.js', 152)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.3/jquery.min.js', 153)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.2/jquery.min.js', 154)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.1/jquery.min.js', 155)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.5.1/jquery.min.js', 158)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.4/jquery.min.js', 160)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.3/jquery.min.js', 161)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.2/jquery.min.js', 162)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.1/jquery.min.js', 163)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.0/jquery.min.js', 164)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.2/jquery.min.js', 165)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.1/jquery.min.js', 166)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.0/jquery.min.js', 167)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.2.6/jquery.min.js', 168)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.2.3/jquery.min.js', 171)")

	# jquery-migrate -library 2
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.4.1/jquery-migrate.js',175)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.4.0/jquery-migrate.js',176)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.3.2/jquery-migrate.js',177)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.3.1/jquery-migrate.js',178)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.3.0/jquery-migrate.js',179)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.2.0/jquery-migrate.js',180)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.1.0/jquery-migrate.js',181)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.0.1/jquery-migrate.js',182)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.0.0/jquery-migrate.js',183)"),

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.4.1/jquery-migrate.min.js',184)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.4.0/jquery-migrate.min.js',185)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.3.2/jquery-migrate.min.js',186)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.3.1/jquery-migrate.min.js',187)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.3.0/jquery-migrate.min.js',188)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.2.0/jquery-migrate.min.js',189)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.1.0/jquery-migrate.min.js',190)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.0.1/jquery-migrate.min.js',191)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/3.0.0/jquery-migrate.min.js',192)"),

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.4.1/jquery-migrate.js',193)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.4.0/jquery-migrate.js',194)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.3.0/jquery-migrate.js',195)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.2.0/jquery-migrate.js',196)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.1.1/jquery-migrate.js',197)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.1.0/jquery-migrate.js',198)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.0.0/jquery-migrate.js',199)"),

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.4.1/jquery-migrate.min.js',200)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.4.0/jquery-migrate.min.js',201)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.3.0/jquery-migrate.min.js',202)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.2.0/jquery-migrate.min.js',203)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.1.1/jquery-migrate.min.js',204)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.1.0/jquery-migrate.min.js',205)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.0.0/jquery-migrate.min.js',206)"),

	#inserting data for table 3 - underscore.js
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.1.0/underscore.js',207)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.2.0/underscore.js',208)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.3.0/underscore.js',209)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.3.1/underscore.js',210)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.3.2/underscore.js',211)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.3.3/underscore.js',212)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.0/underscore.js',213)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.1/underscore.js',214)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.2/underscore.js',215)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.3/underscore.js',216)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.4/underscore.js',217)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.5/underscore.js',218)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.6/underscore.js',219)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.7/underscore.js',220)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.0/underscore.js',221)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.1/underscore.js',222)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.2/underscore.js',223)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.3/underscore.js',224)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.4/underscore.js',225)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.5/underscore.js',226)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.6/underscore.js',227)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.7/underscore.js',228)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.8/underscore.js',229)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.6.0/underscore.js',230)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.0.0/underscore.js',231)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.0.1/underscore.js',232)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.0.2/underscore.js',233)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.0.3/underscore.js',234)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.0.4/underscore.js',235)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.0/underscore.js',236)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.1/underscore.js',237)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.2/underscore.js',238)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.3/underscore.js',239)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.4/underscore.js',240)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.5/underscore.js',241)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.6/underscore.js',242)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.7/underscore.js',243)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.2.0/underscore.js',244)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.2.1/underscore.js',245)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.2.2/underscore.js',246)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.2.3/underscore.js',247)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.2.4/underscore.js',248)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.3.0/underscore.js',249)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.3.1/underscore.js',250)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.3.2/underscore.js',251)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.3.3/underscore.js',252)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.0/underscore.js',253)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.1/underscore.js',254)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.2/underscore.js',255)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.3/underscore.js',256)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.4/underscore.js',257)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.0/underscore.js',258)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.1/underscore.js',259)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.2/underscore.js',260)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.6.0/underscore.js',261)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.7.0/underscore.js',262)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.0/underscore.js',263)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.1/underscore.js',264)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.2/underscore.js',265)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore.js',266)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.0/underscore.js',267)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.1/underscore.js',268)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.2/underscore.js',269)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.10.0/underscore.js',270)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.10.1/underscore.js',271)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.10.2/underscore.js',272)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.11.0/underscore.js',273)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.12.0/underscore.js',274)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.12.1/underscore.js',275)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.1/underscore.js',276)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.2/underscore.js',277)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.3/underscore.js',278)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.4/underscore.js',279)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.5/underscore.js',280)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.6/underscore.js',281)"),

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.1.0/underscore-min.js',282)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.2.0/underscore-min.js',283)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.3.0/underscore-min.js',284)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.3.1/underscore-min.js',285)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.3.2/underscore-min.js',286)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.3.3/underscore-min.js',287)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.0/underscore-min.js',288)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.1/underscore-min.js',289)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.2/underscore-min.js',290)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.3/underscore-min.js',291)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.4/underscore-min.js',292)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.5/underscore-min.js',293)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.6/underscore-min.js',294)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.4.7/underscore-min.js',295)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.0/underscore-min.js',296)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.1/underscore-min.js',297)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.2/underscore-min.js',298)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.3/underscore-min.js',299)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.4/underscore-min.js',300)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.5/underscore-min.js',301)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.6/underscore-min.js',302)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.7/underscore-min.js',303)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.5.8/underscore-min.js',304)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/0.6.0/underscore-min.js',305)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.0.0/underscore-min.js',306)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.0.1/underscore-min.js',307)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.0.2/underscore-min.js',308)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.0.3/underscore-min.js',309)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.0.4/underscore-min.js',310)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.0/underscore-min.js',311)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.1/underscore-min.js',312)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.2/underscore-min.js',313)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.3/underscore-min.js',314)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.4/underscore-min.js',315)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.5/underscore-min.js',316)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.6/underscore-min.js',317)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.1.7/underscore-min.js',318)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.2.0/underscore-min.js',319)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.2.1/underscore-min.js',320)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.2.2/underscore-min.js',321)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.2.3/underscore-min.js',322)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.2.4/underscore-min.js',323)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.3.0/underscore-min.js',324)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.3.1/underscore-min.js',325)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.3.1-amdjs/underscore-amd-min.js',326)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.3.2/underscore-min.js',327)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.3.3/underscore-min.js',328)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.0/underscore-min.js',329)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.1/underscore-min.js',330)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.2/underscore-min.js',331)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.3/underscore-min.js',332)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.4/underscore-min.js',333)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.0/underscore-min.js',334)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.1/underscore-min.js',335)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.2/underscore-min.js',336)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.6.0/underscore-min.js',337)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.7.0/underscore-min.js',338)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.0/underscore-min.js',339)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.1/underscore-min.js',340)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.2/underscore-min.js',341)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js',342)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.0/underscore-min.js',343)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.1/underscore-min.js',344)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.9.2/underscore-min.js',345)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.10.0/underscore-min.js',346)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.10.1/underscore-min.js',347)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.10.2/underscore-min.js',348)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.11.0/underscore-min.js',349)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.12.0/underscore-min.js',350)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.12.1/underscore-min.js',351)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.1/underscore-min.js',352)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.2/underscore-min.js',353)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.3/underscore-min.js',354)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.4/underscore-min.js',355)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.5/underscore-min.js',356)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.13.6/underscore-min.js',357)"),


	for row1 in (conn.execute("SELECT * FROM variant")):
		print(row1)

	for row2 in (conn.execute("SELECT * FROM url")):
		print(row2)
	#conn.close())
	conn.commit()
	print("######################################################################################")
	for row1 in (conn.execute("SELECT * FROM version")):
		print(row1)
except Exception as e: 
	print(type(e))
	print(e) 
	print(traceback.print_exc()) 
else:
	print("SQL Creation is ready")
