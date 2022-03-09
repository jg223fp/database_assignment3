import PySimpleGUI as sg

#prints main menu and prompts for a choice
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


# Prints out player data          
def presentPlayers(cursor):
    headings = ['ID','Name','Level','Nationality']
    player_ids= []
    players_arry=[]
    for id,name,nationality,level in cursor:
        players_arry.append([id,name,nationality,level])
        player_ids.append(id)
    players_arry_layout = [
        [sg.Table(values=players_arry, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    justification='right',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35,
                    tooltip='Reservations Table')],
        [sg.Text("Choose a player id from the list")],
        [sg.Listbox(values=player_ids, size=(40, 5), select_mode='single', key='-playeslected-')],
        [sg.Button('show the bag'),sg.Exit()],
        ]
    players_arry_window = sg.Window("Contact Information Window", 
    players_arry_layout, modal=True)
    event, values = players_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        players_arry_window.close()
    elif event == 'show the bag':
        players_arry_window.close()
        return values['-playeslected-'][0]

# prints the bag of a player
def showBag(cursor,name):
    headings = ["Disc name","plastic","weigth(g)","speed","glide","turn","fade","classification"]
    players_arry=[]
    for name,plastic,weigth,speed,glide,turn,fade,classification in cursor:
        players_arry.append([name,plastic,weigth,speed,glide,turn,fade,classification])
    players_arry_layout = [[sg.Text("{}s bag".format(name))],
        [sg.Table(values=players_arry, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    justification='right',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35,
                    tooltip='Reservations Table')],
        [sg.Button('return to main menu')],
        ]
    players_arry_window = sg.Window("Contact Information Window", 
    players_arry_layout, modal=True)
    event, values = players_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        players_arry_window.close()
    elif event == 'return to main menu':
        players_arry_window.close()


#present competitions and returns a list with the name and year of the competition       
def presentCompetitions(competitions):
    competitions_list = []
    competitions_year = []
    for c in competitions:
        competitions_list.append(c[0])
        competitions_year.append(c[1])
    competitions_arry_layout = [ [[sg.Text("select a competition to view the winner")],
        [sg.Listbox(values=competitions_list, size=(40, 5), select_mode='single', key='-competitionsslected-')],
        [sg.Listbox(values=competitions_year, size=(40, 5), select_mode='single', key='-yearslected-')]],
        [sg.Button('show the winner'),sg.Exit()],
        ]
    competitions_arry_window = sg.Window("Contact Information Window", 
    competitions_arry_layout, modal=True)
    event, values = competitions_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        competitions_arry_window.close()
    elif event == 'show the winner':
        competitions_arry_window.close()
        print([values['-competitionsslected-'][0],values['-yearslected-'][0]])
        return [values['-competitionsslected-'][0],values['-yearslected-'][0]]



def presentWinner(winner):
    print(winner)

# returns a list with collected data [classification,level,distance]  
def getPlayerAttributes():
    pass

#lists the following attributes from the discs provided: name, speed, glide, turn, fade 
def showDiscs(discs):
    pass

#lists all the courses from the provided list and return the one that the user selects
def listCourses(courses):
    pass

#presents the provided disc class as the most used on tee pads for the provided course
def presentDiscClass(course, discClass):
    pass

#presents all the attributes of the provided most owned disc
def presentMostOwnedDisc(disc):
    pass

#present the longest hole from recived list[competition_name, year, course, hole_number,distance ]
def showHoleInfo(hole):
    #In the COMPETITION_NAME from YEAR played on COURSE
    # it was HOLE_NUMBER that was the longest. It has a distance of DISTANCE
    pass