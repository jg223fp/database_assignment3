import os
import pandas as pd
import mysql.connector
from mysql.connector import errorcode
import view
import parser

#Connection
cnx = mysql.connector.connect(user="root", password="root123321", host="127.0.0.1")

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
        
    view.showBag(cursor,playerName)


# Creating cursor to execute commands  
cursor = cnx.cursor(buffered=True) 

#parse data into db
parser.parserBoot(cnx,cursor)

# launch menu system
choice = 0
while choice != 7:
    choice = view.printMenu()
    if choice != 7:
        match choice:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                lookInsidePlayerBags(cursor)
            case 6:
                pass
        input("Press enter to continue...")
                
                
print("Terminating session...") 
# Close connection
cursor.close()
cnx.close()