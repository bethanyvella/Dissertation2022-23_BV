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
	for row in (conn.execute("SELECT * FROM library")):
		print(row)

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
	conn.execute("INSERT INTO version (versionName, isVulnerable, libraryID) VALUES ('1.0.0', 1 , 1)")

	for row1 in (conn.execute("SELECT * FROM version")):
		print(row1)

	#inserting in table 3
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
		
	#inserting data in table 4
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

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.js ', 77)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.3/jquery.js ', 78)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.2/jquery.js ', 79)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.js ', 80)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.0/jquery.js ', 81)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.js ', 82)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.2/jquery.js ', 83)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.js ', 84)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.0/jquery.js ', 85)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.2/jquery.js ', 86)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.1/jquery.js ', 87)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.0/jquery.js ', 88)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.js ', 89)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.0/jquery.js ', 90)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.3/jquery.js ', 91)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.2/jquery.js ', 92)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.1/jquery.js ', 93)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.0/jquery.js ', 94)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.4/jquery.js ', 98)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.3/jquery.js ', 99)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.2/jquery.js ', 100)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.1/jquery.js ', 101)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.5.1/jquery.js ', 104)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.4/jquery.js ', 106)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.3/jquery.js ', 107)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.2/jquery.js ', 108)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.1/jquery.js ', 109)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.0/jquery.js ', 110)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.2/jquery.js ', 111)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.1/jquery.js ', 112)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.0/jquery.js ', 113)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.2.6/jquery.js ', 114)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.2.3/jquery.js ', 117)"),

	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js ', 131)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.3/jquery.min.js ', 132)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.2/jquery.min.js ', 133)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.1/jquery.min.js ', 134)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.0/jquery.min.js ', 135)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.min.js ', 136)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.2/jquery.min.js ', 137)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.min.js ', 138)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.0/jquery.min.js ', 139)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.2/jquery.min.js ', 140)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.1/jquery.min.js ', 141)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.0/jquery.min.js ', 142)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.min.js ', 143)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.0/jquery.min.js ', 144)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.3/jquery.min.js ', 145)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.2/jquery.min.js ', 146)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.1/jquery.min.js ', 147)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.8.0/jquery.min.js ', 148)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.7.2/jquery.min.js ', 149)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.7.1/jquery.min.js ', 150)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.7.0/jquery.min.js ', 151)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.4/jquery.min.js ', 152)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.3/jquery.min.js ', 153)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.2/jquery.min.js ', 154)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.6.1/jquery.min.js ', 155)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.5.1/jquery.min.js ', 158)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.4/jquery.min.js ', 160)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.3/jquery.min.js ', 161)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.2/jquery.min.js ', 162)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.1/jquery.min.js ', 163)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.4.0/jquery.min.js ', 164)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.2/jquery.min.js ', 165)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.1/jquery.min.js ', 166)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.3.0/jquery.min.js ', 167)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.2.6/jquery.min.js ', 168)"),
	conn.execute("INSERT INTO url (url, variantID) VALUES ('https://cdnjs.cloudflare.com/ajax/libs/jquery/1.2.3/jquery.min.js ', 171)")

	for row1 in (conn.execute("SELECT * FROM variant")):
		print(row1)

	#conn.close())
	conn.commit()

except Exception as e: 
	print(type(e))
	print(e) 
	print(traceback.print_exc()) 
else:
	print("SQL Creation is ready")
