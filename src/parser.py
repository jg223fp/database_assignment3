import os
import pandas as pd
import mysql.connector
from mysql.connector import errorcode

global cnx

DB_NAME = "disc_golf"
PLAYERS = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\csv_files\players.csv"
DISCS = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\csv_files\discs.csv"
BAGS = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\csv_files\\bags.csv"
HOLES = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\csv_files\holes.csv"
COMPETITIONS = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\csv_files\competition_results.csv"
               
# Creates the database.
def create_database(cursor, DB_NAME):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Faild to create database {}".format(err))
        exit(1)

# Creates the table for the players.csv file
def createPlayersTable(cursor):
    createPlayers = "CREATE TABLE `players` (" \
                 "  `id` varchar(20) NOT NULL," \
                 "  `name` varchar(25)," \
                 "  `level` varchar(14)," \
                 "  `nationality` varchar(30)," \
                 "  PRIMARY KEY (`id`)" \
                 ") ENGINE=InnoDB"
    commitTable(cursor, "players", createPlayers) 

# Creates the table for the discs.csv file
def createDiscssTable(cursor):
    createDiscs = "CREATE TABLE `discs` (" \
                 "  `name` varchar(20) NOT NULL," \
                 "  `max_weigth` int," \
                 "  `speed` smallint," \
                 "  `glide` smallint," \
                 "  `turn` smallint signed," \
                 "  `fade` smallint signed," \
                 "  `classification` varchar(15)," \
                 "  `average_range_beginner` int," \
                 "  `average_range_advanced` int," \
                 "  `average_range_pro` int," \
                 "  PRIMARY KEY (`name`)" \
                 ") ENGINE=InnoDB"
    commitTable(cursor, "discs", createDiscs)                         

# Creates the table for the holes.csv file
def createHolesTable(cursor):
    createHoles = "CREATE TABLE `holes` (" \
                 "  `name` varchar(40) NOT NULL," \
                 "  `hole` int NOT NULL," \
                 "  `par` int," \
                 "  `distance` int," \
                 "  PRIMARY KEY (`name`,`hole`)" \
                 ") ENGINE=InnoDB"
    commitTable(cursor, "holes", createHoles)

# Creates the table for the competition_results.csv file
def createCompetitionResultsTable(cursor):
    createCompetitionResults = "CREATE TABLE `competition_results` (" \
                 "  `name` varchar(40) NOT NULL," \
                 "  `year` int NOT NULL," \
                 "  `course` varchar(40)," \
                 "  `hole` int NOT NULL," \
				 "  `player_id` varchar(10) NOT NULL," \
				 "  `result` int," \
				 "  `tee_pad_disc` varchar(40)," \
				 "  `finish_disc` varchar(40)," \
                 "  PRIMARY KEY (`name`, `year`, `player_id`,`hole`)" \
                 ") ENGINE=InnoDB"
    commitTable(cursor, "competition results", createCompetitionResults) 	 

# Creates the table for the bags.csv file
def createBagsTable(cursor):
    createBags = "CREATE TABLE `bags` (" \
                 "  `owner_id` varchar(10) NOT NULL," \
                 "  `disc_name` varchar(30) NOT NULL," \
                 "  `plastic_type` varchar(25) NOT NULL," \
                 "  `weigth` int NOT NULL," \
                 "  PRIMARY KEY (`owner_id`, `disc_name`, `plastic_type`, `weigth`)" \
                 ") ENGINE=InnoDB"
    commitTable(cursor, "bags", createBags) 

# Puts the table in the database
def commitTable(cursor, tableName, sqlCreate):    
    try:
        print("Creating table {}... ".format(tableName))
        cursor.execute(sqlCreate)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Reads data from players.csv and creates a list of sqlcommands to insert them in a table.
def addPlayers(cursor, path):
    players = pd.read_csv(path)
    insertSql = []
    for index, row in players.iterrows():
        command =  "INSERT INTO players (id, name, level, nationality) "\
                 "VALUES ('{}','{}','{}','{}');"\
                .format(
                row['id'],
                row['name'],
                row['level'],
                row['nationality'])
        insertSql.append(command)
    commitData(cursor, insertSql)

# Reads data from discs.csv and creates a list of sqlcommands to insert them in a table.
def addDiscs(cursor, path):
    discs = pd.read_csv(path)
    insertSql = []
    for index, row in discs.iterrows():
        command =  "INSERT INTO discs (name, max_weigth, speed, glide, turn,"\
         "fade, classification, average_range_beginner, average_range_advanced, average_range_pro) "\
                 "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');"\
                .format(
                row['name'],
                row['max_weigth'],
                row['speed'],
                row['glide'],
                row['turn'],
                row['fade'],
                row['classification'],
                row['average_range_beginner'],
                row['average_range_advanced'],
                row['average_range_pro'])
        insertSql.append(command)  
    commitData(cursor, insertSql)     

# Reads data from holes.csv and creates a list of sqlcommands to insert them in a table.
def addHoles(cursor, path):
    holes = pd.read_csv(path)
    insertSql = []
    for index, row in holes.iterrows():
        command =  "INSERT INTO holes (name, hole, par, distance) "\
                 "VALUES ('{}','{}','{}','{}');"\
                .format(
                row['name'],
                row['hole'],
                row['par'],
                row['distance'])
        insertSql.append(command)  
    commitData(cursor, insertSql)

# Reads data from competition_results.csv and creates a list of sqlcommands to insert them in a table.
def addResults(cursor, path):
    results = pd.read_csv(path)
    insertSql = []
    for index, row in results.iterrows():
        command =  "INSERT INTO competition_results (name, year, course, hole, player_id, result, tee_pad_disc, finish_disc) "\
                 "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');"\
                .format(
                row['name'],
                row['year'],
                row['course'],
                row['hole'],
				row['player_id'],
				row['result'],
				row['tee_pad_disc'],
				row['finish_disc'])
        insertSql.append(command)  
    commitData(cursor, insertSql)

# Reads data from bags.csv and creates a list of sqlcommands to insert them in a table.
def addBags(cursor, path):
    bags = pd.read_csv(path)
    insertSql = []
    for index, row in bags.iterrows():
        command =  "INSERT INTO bags (owner_id, disc_name, plastic_type, weigth) "\
                 "VALUES ('{}','{}','{}','{}');"\
                .format(
                row['owner_id'],
                row['disc_name'],
                row['plastic_type'],
                row['weigth'])
        insertSql.append(command)  
    commitData(cursor, insertSql)

# Executes a list of queries and commits them to the db.       
def commitData(cursor, insertSql):
    print("Adding data to table...")
    for query in insertSql:
        try:
            #print("SQL query {}: ".format(query), end='')
            cursor.execute(query)
        except mysql.connector.Error as err:
            print("An error occurred when adding data: {}".format(err.msg))
        else:
            cnx.commit()   # Make sure data is committed to the database
            print("Data was added")    


 

def parserBoot(recivedCNX, cursor):
    global cnx 
    cnx = recivedCNX

        # Confirm connection
    if cnx.is_connected():
        print("Connection to MySQL established.")
    else:
        print("Couldn't connect to server. Terminating...")
        quit()

    #Booleans used for the controll of what exists at boot 
    tablesExists = False
    datainTables = False


    # Check if db exist
    print("Controlling if database exists...")
    try:
        cursor.execute("USE {}".format(DB_NAME))
        print("Database {} already exists.".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exist".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, DB_NAME)
            print("Database {} created succesfully.".format(DB_NAME))
            cnx.database = DB_NAME
            createPlayersTable(cursor)
            createDiscssTable(cursor)
            createHolesTable(cursor)
            createCompetitionResultsTable(cursor)
            createBagsTable(cursor)
            tablesExists = True
            addPlayers(cursor,PLAYERS)
            addDiscs(cursor,DISCS)
            addHoles(cursor,HOLES)
            addResults(cursor,COMPETITIONS)
            addBags(cursor,BAGS)
            datainTables = True

    if not tablesExists:
        # check if tables exists
        try:
            print("Checking if table players exists...")
            cursor.execute("SHOW TABLES LIKE 'players'")
            if cursor.fetchone() == None:
                createPlayersTable(cursor)
            else:
                print("Table exists")

            print("Checking if table discs exists...")
            cursor.execute("SHOW TABLES LIKE 'discs'")
            if cursor.fetchone() == None:
                createDiscssTable(cursor)
            else:
                print("Table exists")

            print("Checking if table holes exists...")
            cursor.execute("SHOW TABLES LIKE 'holes'")
            if cursor.fetchone() == None:
                createHolesTable(cursor)
            else:
                print("Table exists")
            
            print("Checking if table competition_results exists...")
            cursor.execute("SHOW TABLES LIKE 'competition_results'")
            if cursor.fetchone() == None:
                createCompetitionResultsTable(cursor)
            else:
                print("Table exists")

            print("Checking if table bags exists...")
            cursor.execute("SHOW TABLES LIKE 'bags'")
            if cursor.fetchone() == None:
                createBagsTable(cursor)
            else:
                print("Table exists")

        except mysql.connector.Error as err:
            print("Problem when checking table existence".format(DB_NAME))

    if not datainTables:
        #check if data in tables
        try:
            print("Checking if table players is empty...")          
            cursor.execute("SELECT * from players")
            if len(cursor.fetchall()) < 1:
                addPlayers(cursor, PLAYERS)
            else:
                print("There is data in the table")
        except mysql.connector.Error as err:
            print("Something went wrong when performing query: {}".format(err))

        try:
            print("Checking if table discs is empty...")          
            cursor.execute("SELECT * from discs")
            if len(cursor.fetchall()) < 1:
                addDiscs(cursor, DISCS)
            else:
                print("There is data in the table")
        except mysql.connector.Error as err:
            print("Something went wrong when performing query: {}".format(err))

        try:
            print("Checking if table holes is empty...")          
            cursor.execute("SELECT * from holes")
            if len(cursor.fetchall()) < 1:
                addHoles(cursor,HOLES)
            else:
                print("There is data in the table")
        except mysql.connector.Error as err:
            print("Something went wrong when performing query: {}".format(err))

        try:
            print("Checking if table competition_results is empty...")          
            cursor.execute("SELECT * from competition_results")
            if len(cursor.fetchall()) < 1:
                addResults(cursor,COMPETITIONS)
            else:
                print("There is data in the table")
        except mysql.connector.Error as err:
            print("Something went wrong when performing query: {}".format(err))

        try:
            print("Checking if table bags is empty...")          
            cursor.execute("SELECT * from bags")
            if len(cursor.fetchall()) < 1:
                addBags(cursor,BAGS)
            else:
                print("There is data in the table")
        except mysql.connector.Error as err:
            print("Something went wrong when performing query: {}".format(err))
            
    return cursor

