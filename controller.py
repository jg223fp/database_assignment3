import os
import pandas as pd
import mysql.connector
from mysql.connector import errorcode
import view
import parser


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


print("Terminating session...") 
# Close connection
cursor.close()
cnx.close()