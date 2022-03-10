from ntpath import join
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
    x = name
    for discname,plastic,weigth,speed,glide,turn,fade,classification in cursor:
        players_arry.append([discname,plastic,weigth,speed,glide,turn,fade,classification])
    players_arry_layout = [[sg.Text("{}s bag".format(x))],
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
    for c in competitions:
        competitions_list.append("{}, {}".format(c[0],c[1]))
    competitions_arry_layout = [ [[sg.Text("select a competition and a year")],
        [sg.Listbox(values=competitions_list, size=(40, 5), select_mode='single', key='-competitionsslected-')],
        [sg.Button('show the winner'),sg.Exit()],
        ]]
    competitions_arry_window = sg.Window("Contact Information Window", 
    competitions_arry_layout, modal=True)
    event, values = competitions_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        competitions_arry_window.close()
    elif event == 'show the winner':
        competitions_arry_window.close()
        vals = values['-competitionsslected-'][0]
        splittedVals = vals.split(", ")
        print(splittedVals)
        return splittedVals



def presentWinner(winner):
    winner = winner[0]
    winner = list(winner)
    winner_arry_layout =[[sg.Text("The winner name is : {}".format(winner[0]))],
                        [sg.Text("The winner id is : {}".format(winner[1]))],
                        [sg.Text("The winner nationality is : {}".format(winner[2]))],
                        [sg.Text("The winner total is : {}".format(winner[3]))],
                        [sg.Button('return to main menu')]]
    winner_arry_window = sg.Window("The winner is", 
    winner_arry_layout, modal=True)
    event, values = winner_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        winner_arry_window.close()
    elif event == 'return to main menu':
        winner_arry_window.close()

# returns a list with collected data [classification,level,distance]  
def getPlayerAttributes():
    classifications = [ "putt", "midrange", "fairwaydriver", "driver"]
    Levels = ["beginner" , "advanced", "pro"]
    # distance, any int number
    players_arry_layout = [
        [sg.Text("Choose a classification and a Level and enter a distance")],
        [sg.Listbox(values=classifications, size=(40, 5), select_mode='single', key='classifications')],
        [sg.Listbox(values=Levels, size=(40, 5), select_mode='single', key='Levels')],
        [sg.Text("Enter a distance"), sg.Input(key='distance', do_not_clear=True, size=(10, 1))],
        [sg.Button('show the disc'),sg.Exit()],
        ]
    
    players_arry_window = sg.Window("Contact Information Window", 
    players_arry_layout, modal=True)
    event, values = players_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        players_arry_window.close()
    elif event == 'show the disc':
        players_arry_window.close()
        x = ""
        if values['Levels'][0] == "beginner":
            x = "average_range_beginner"
        elif values['Levels'][0] == "advanced":
            x = "average_range_advanced"
        elif values['Levels'][0] == "pro":
            x = "average_range_pro"
        return [values['classifications'][0],x,values['distance']]

    #avregae_range_beginner


#lists the following attributes from the discs provided: name, speed, glide, turn, fade 
def showDiscs(discs):
    discs_arry_layout =[[sg.Text(discs)],
                        [sg.Button('return to main menu')]]
    discs_arry_window = sg.Window("The discs is", 
    discs_arry_layout, modal=True)
    event, values = discs_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        discs_arry_window.close()
    elif event == 'return to main menu':
        discs_arry_window.close()

#lists all the courses from the provided list and return the one that the user selects
def listCourses(courses):
    g = []
    for c in courses:
        x = ",".join(c)
        g.append(x)
    players_arry_layout = [
        [sg.Text("Choose a course")],
        [sg.Listbox(values=g, size=(40, 5), select_mode='single', key='classifications')],
        [sg.Button('show the disc'),sg.Exit()],
        ]
    
    players_arry_window = sg.Window("Contact Information Window", 
    players_arry_layout, modal=True)
    event, values = players_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        players_arry_window.close()
    elif event == 'show the disc':
        players_arry_window.close()
        return values['classifications'][0]

#presents the provided disc class as the most used on tee pads for the provided course
def presentDiscClass(course, discClass):
    headings = ["course", "Disc Class"]
    valuess = []
    valuess.append(course)
    discClass = discClass[0]
    print(discClass)
    x =",".join(discClass)
    valuess.append(x)
    print(valuess)
    players_arry_layout =[[sg.Text("On the course: {}".format(valuess[0]))],
                        [sg.Text("The most used disc is : {}".format(valuess[1]))],
        [sg.Button('return to main menu')],
        ]
    players_arry_window = sg.Window("Contact Information Window", 
    players_arry_layout, modal=True)
    event, values = players_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        players_arry_window.close()
    elif event == 'return to main menu':
        players_arry_window.close()


#presents all the attributes of the provided most owned disc
def presentMostOwnedDisc(disc):
    disc = disc[0]
    disc = list(disc)
    players_arry_layout =[[sg.Text("The most owned disc is : {}".format(disc[0]))],
                        [sg.Text("The disc classification is : {}".format(disc[1]))],
                        [sg.Text("The disc speed glide is : {}".format(disc[2]))],
                        [sg.Text("The disc glide is : {}".format(disc[3]))],
                        [sg.Text("The disc turn is : {}".format(disc[4]))],
                        [sg.Text("The disc fade is : {}".format(disc[5]))],
                        [sg.Text("The disc average range for a beginner is : {}".format(disc[6]))],
                        [sg.Text("The disc average range for a advanced is : {}".format(disc[7]))],
                        [sg.Text("The disc average range for a pro is : {}".format(disc[8]))],
        [sg.Button('return to main menu')],
        ]
    players_arry_window = sg.Window("Contact Information Window", 
    players_arry_layout, modal=True)
    event, values = players_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        players_arry_window.close()
    elif event == 'return to main menu':
        players_arry_window.close()
#present the longest hole from recived list[competition_name, year, course, hole_number,distance ]
def showHoleInfo(hole):
    hole_arry_layout =[[sg.Text("In the competition {} {}".format(hole[0], hole[1]))],
                        [sg.Text("The longest hole was on the course {} ".format(hole[2]))],
                        [sg.Text("The hole number was: {} ".format(hole[3]))],
                        [sg.Text("The par of the hole was: {} ".format(hole[4]))],
                        [sg.Text("The distance of the hole was: {} ".format(hole[5]))],
                        [sg.Button('return to main menu')]]
    hole_arry_window = sg.Window("The hole is", 
    hole_arry_layout, modal=True)
    event, values = hole_arry_window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        hole_arry_window.close()
    elif event == 'return to main menu':
        hole_arry_window.close()
