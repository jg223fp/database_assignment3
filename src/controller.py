import os
import pandas as pd
import mysql.connector
from mysql.connector import errorcode
import view
import parser

#Connection
cnx = mysql.connector.connect(user="root", password="root123321", host="127.0.0.1")

# Tells what discs can be used to throw a given range
def throwRange():
    
    userData = view.getplayerAttributes()
    classification = userData[0]
    level = userData[1]
    distance = userData[2]
    
    getDiscs = "SELECT name, speed,glide,turn,fade "\
               "FROM disc_golf.discs "\
                "where classification = {} "\
                "and {} >= {};.format(classification, level,range )"\
                .format(classification, level, distance)
    
    #fetch Discs
    try:
        cursor.execute(getDiscs)
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
     
    #show discs in view    
    discs = cursor.fetchall()
    view.showDiscs(discs)

# Calculates the winner for a given competition
def whoIsWinner(cursor):
    #list competitions
    try:
        cursor.execute("SELECT DISTINCT name, year FROM disc_golf.competition_results;")
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
    
    competitions = cursor.fetchall()
    
    #present competitions and get users selection
    choice =view.presentCompetitions(competitions)
    
    getWinner = "SELECT name,"\
            "id,"\
            "nationality,"\
            "total "\
            "from disc_golf.players "\
            "JOIN "\
            "(SELECT "\
            "player_id, SUM(result) AS total "\
            "FROM "\
            "disc_golf.competition_results "\
            "WHERE "\
            "year = '2020' "\
            "AND competition_results.name = 'slottsskogen open' "\
            "GROUP BY player_id "\
            "ORDER by total "\
            "LIMIT 1 "\
            ") as winner ON players.id = winner.player_id;"    # add ´.format for year and competition name
    try:
        cursor.execute(getWinner)
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
    
    #fetch winner and present in view
    winner = cursor.fetchall()
    view.presentWinner(winner)

    #Lets you look in a selected players bag
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
                whoIsWinner(cursor)
            case 2:
                throwRange(cursor)
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