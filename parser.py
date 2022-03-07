import os
from random import choices
import pandas as pd
import mysql.connector
from mysql.connector import errorcode

#Connection
cnx = mysql.connector.connect(user="root", password="root123321", host="127.0.0.1")
DB_NAME = "disc_golf"
PLAYERS = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\csv_files\players.csv"
DISCS = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\csv_files\discs.csv"
BAGS = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\csv_files\bags.csv"
HOLES = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\csv_files\holes.csv"
COMPETITIONS = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "\csv_files\competitions.csv"

  
def printMenu():
    print('''\n         MAIN MENU 
    Choose one option:
    1: -----
    2: ----
    3: ----
    4: ------
    5: ----
    6: Quit
          ''')

# Returns a user input for a menu selection.    
def getMenuChoise():
    while True:
        try:    
            selection = int(input("Selection: "))
            if selection >= 1 and selection <= 6:
                return int(selection)
            print("Value must be inside range.")
        except ValueError:
            print("Value must be an integer.") 
            selection = -1
               
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
                 "  `nationality` varchar(10)," \
                 "  PRIMARY KEY (`id`)" \
                 ") ENGINE=InnoDB"
    commitTable(cursor, "players", createPlayers)                          
                   

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

# Confirm connection
if cnx.is_connected():
	print("Connection to MySQL established.")
else:
    print("Couldn't connect to server. Terminating...")
    quit() 

# Creating cursor to execute commands  
cursor = cnx.cursor(buffered=True) 

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
        tablesExists = True
        addPlayers(cursor,PLAYERS)
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
	
# launch menu system
choice = 0
while choice != 6:
	printMenu()
	choice = getMenuChoise()     # collect choice from user.
 

print("Terminating session...") 
# Close connection
cursor.close()
cnx.close()
