import os
import pandas as pd
import mysql.connector
from mysql.connector import errorcode
import view
import parser

def lookInsidePlayerBags(cursor):
    #list players
    try:
        cursor.execute("SELECT * from disc_golf.players;")
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
        
    view.presentPlayers(cursor)
    playerId = view.promptForPlayerId()
    
    #fetch name
    try:
        cursor.execute("SELECT name from disc_golf.players where id = {}".format(playerId))
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
    playerName = cursor.fetchone()[0]
  
    fetchBag = "SELECT disc_name,"\
    "plastic_type,"\
    "weigth,"\
    "speed,"\
    "glide,"\
    "turn,"\
    "fade,"\
    "classification"\
    " FROM disc_golf.bags"\
    " JOIN disc_golf.discs ON discs.name = bags.disc_name"\
    " and bags.owner_id = {}"\
    " order by classification;".format(playerId)
    
    #fetch bag
    try:
        cursor.execute(fetchBag)
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
        
    


#Connection
cnx = mysql.connector.connect(user="root", password="root123321", host="127.0.0.1")

# Creating cursor to execute commands  
cursor = cnx.cursor(buffered=True) 

#parse data into db and recive cursor
cursor = parser.parserBoot(cnx,cursor)

# launch menu system
choice = 0
while choice != 7:
    choice = view.printMenu()
    if choice != 7:
        match choice:
            case 1:
                print("asas")
            case 2:
                print("asas")
            case 3:
                print("asas")
            case 4:
                print("asas")
            case 5:
                lookInsidePlayerBags(cursor)
            case 6:
                print("asas")
                
                
print("Terminating session...") 
# Close connection
cursor.close()
cnx.close()