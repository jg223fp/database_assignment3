import PySimpleGUI as sg

def printMenu():
    layout = [[sg.Text("Choose one option:")],     # Part 2 - The Layout
            [sg.Text("1: Who is the winner of a specific competition")],
            [sg.Text("2: Which discs of a specified class can be thrown longer than a specified range?")],
            [sg.Text("3: Classification of the most used tee pad disc in a given competition")],
            [sg.Text("4: Facts about the most owned disc")],
            [sg.Text("5: Look inside player bags")],
            [sg.Text("6: Longest hole in a specific competition")],
            [sg.Input(key='-INPUT-')],
            [sg.Button('Ok'), sg.Button('Quit')]]
    # Create the window
    window = sg.Window('Disc factz', layout)      # Part 3 - Window Defintion
    # Display and interact with the Window
    event, values = window.read()                   # Part 4 - Event loop or Window.read call
    window.close()
    
    # Do something with the information gathered
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        return 7
    else:
        return int(values['-INPUT-'])
    

# Returns a user input for a menu selection.    
def getMenuChoise(top):
    while True:
        try:    
            selection = int(input("Selection: "))
            if selection >= 1 and selection <= top:
                return int(selection)
            print("Value must be inside range.")
        except ValueError:
            print("Value must be an integer.") 
            selection = -1
            
def promptForPlayerId(): 
    while True:
        try:    
            selection = int(input("Enter ID of the player which bag you want to look in: "))
            return selection
        except ValueError:
            print("Value must be an integer.") 
            
            
def presentPlayers(cursor):
    print("| {:<15} | {:<20} | {:<15} | {:<15} |".format(\
     "ID",
     "Name",
     "Level",
     "Nationality"))
    print("-"*80)
    
    for id,name,nationality,level in cursor:
        print("| {:<15} | {:<20} | {:<15} | {:<15} |".format(\
     id,
     name,
     nationality,
     level))

def showBag(cursor,name):
    print("\n {}s bag".format(name))
    print("| {:<15} | {:<15} | {:<7} | {:<5} | {:<5} | {:<5} | {:<5} | {:<15} |".format(\
     "Disc name",
     "plastic",
     "weigth(g)",
     "speed",
     "glide",
     "turn",
     "fade",
     "classification"))
    print("-"*80)
    
    for name,plastic,weigth,speed,glide,turn,fade,classification in cursor:
        print("| {:<15} | {:<15} | {:<7}   | {:<5} | {:<5} | {:<5} | {:<5} | {:<15} |".format(\
     name,
     plastic,
     weigth,
     speed,
     glide,
     turn,
     fade,
     classification))