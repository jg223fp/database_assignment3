import os
import pandas as pd
import mysql.connector
from mysql.connector import errorcode
import view
import parser

#Connection
cnx = mysql.connector.connect(user="root", password="root", host="127.0.0.1")

def longestHole(cursor):
    #list competitions
    try:
        cursor.execute("SELECT DISTINCT name, year FROM disc_golf.competition_results;")
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
    
    competitions = cursor.fetchall()
    
    #present competitions and get users selection (name and year) in a list
    choice = view.presentCompetitions(competitions)
    
    getLongestHole = "select "\
        "competition_results.name,"\
        "year,course,"\
        "holes.hole,"\
        "par, distance "\
        "from disc_golf.competition_results "\
        "JOIN holes ON competition_results.course = holes.name "\
        "AND competition_results.hole = holes.hole " \
        "AND competition_results.name  = '{}' "\
        "AND year = {} "\
        "order by distance DESC "\
        "limit 1;".format(choice[0],choice[1])
      
    #fetch longest hole in competition
    try:
        cursor.execute(getLongestHole)
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
    hole = cursor.fetchone()
    
    #display hole in view
    view.showHoleInfo(hole)

def mostOwnedDiscFacts(cursor):
    getDisc = "SELECT "\
    "name,"\
    "classification, "\
    "speed,"\
    "glide, "\
    "turn, "\
    "fade, "\
    "average_range_beginner, "\
    "average_range_advanced, "\
    "average_range_pro " \
    "FROM "\
    "disc_golf.discs "\
    "WHERE "\
    "name = (SELECT "\
    "disc_name "\
    "FROM "\
    "(SELECT "\
    "disc_name, "\
    "COUNT(disc_name) AS discCount "\
    "FROM "\
    "disc_golf.bags "\
    "GROUP BY disc_name " \
    "ORDER BY discCount DESC LIMIT 1) AS mostOwned);"     
    
    #fetch disc
    try:
        cursor.execute(getDisc)
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
    
    #present disc in view
    disc = cursor.fetchall()
    view.presentMostOwnedDisc(disc)


def mostUsedDiscClass(cursor):
    #fetch courses
    try:
        cursor.execute("SELECT distinct name from disc_golf.holes;")
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
    courses = cursor.fetchall()
    
    choice = view.listCourses(courses)
    
    getDiscClass = "SELECT "\
                "classification "\
                "FROM "\
                "disc_golf.discs "\
                "WHERE "\
                "name = (SELECT "\
                "tee_pad_disc "\
                "FROM "\
                "(SELECT "\
                "tee_pad_disc, COUNT(tee_pad_disc) AS discCount "\
                "FROM "\
                "disc_golf.competition_results where competition_results.course = '{}' "\
                "GROUP BY tee_pad_disc "\
                "ORDER BY discCount DESC "\
                "LIMIT 1) AS mostUsed);".format(choice)                  

#fetch discclass
    try:
        cursor.execute(getDiscClass)
    except mysql.connector.Error as err:
        print("Something went wrong when performing query: {}".format(err))
    discClass = cursor.fetchall()
    
    view.presentDiscClass(choice, discClass)


# Tells what discs can be used to throw a given range
def throwRange(cursor):
    
    userData = view.getPlayerAttributes()
    print(userData)
    classification = userData[0]
    level = userData[1]
    distance = int(userData[2])
    
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
    
    #present competitions and get users selection (name and year) in a list
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
            "year = {} "\
            "AND competition_results.name = '{}' "\
            "GROUP BY player_id "\
            "ORDER by total "\
            "LIMIT 1 )"\
            " as winner ON players.id = winner.player_id;".format(int(choice[1]),choice[0]) 
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
        
    playerId = view.presentPlayers(cursor)
    if playerId ==None:   #return from method if no player id was provided
        return
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
                mostUsedDiscClass(cursor)
            case 4:
                mostOwnedDiscFacts(cursor)
            case 5:
                lookInsidePlayerBags(cursor)
            case 6:
                longestHole(cursor)
                
print("Terminating session...") 
# Close connection
cursor.close()
cnx.close()