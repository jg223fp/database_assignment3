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