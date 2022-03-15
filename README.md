# database_assignment3
### Instructions on installing dependencies:
You need the following dependencies:
- pandas 
- pysimpleGui
- mysql.connector

To install them run the command "pip install Example" replacing "Example" with the  libraries you are missing.

</BR>

### You will also need a python version => 3.10

- For windows users folllow the instructions on this link:

    https://docs.python.org/3/using/windows.html

</BR>

- For linux:
 
  Ubuntu: use the command "sudo apt install python3.10"

   Arch: run the command " sudo Pacman install python3.10"

</BR>

### Build database:
- Option 1: Open the database_installation_script.sql inside MySQL workbench and run it.
- Option 2: There is a parser included in the source code whitch will build the database automaticlly.

</BR>

### To run the program:
   - Open controller.py and edit line 9 to your own MySQL server details.
   
   user = "Your_MySQL_User"

   password = "Your_MySQL_Users_password"

   host = "the host where server runs" 
   If you are running a local server use 127.0.0.1 


   - Use the command " python .../database_assignment/src/controller.py"
on a terminal thats opened in the directory of the repository