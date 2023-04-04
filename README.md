#Tic Tac Toe Game
This is a simple Tic Tac Toe game written in Python. It allows two players to play against each other on the same machine using a GUI. The game also includes a client-server architecture, allowing two players to play remotely over a network.

##Requirements
The following Python modules are required to run the Tic Tac Toe game:

+ tkinter
+ socket
+ threading
+ Running the Game
##To run the game, follow these steps:

1. Clone or download the repository to your local machine.

2. Open the command prompt or terminal and navigate to the project directory.

3. To start the server, run the following command:
```
python server.py
```
4. The server will automatically get the IP address of the machine and display it on the console.

5. To start the client, run the following command:

```
python client.py
```
6. A GUI window will appear prompting you to enter the IP address of the server. Enter the IP address and click the "Connect" button.

7. The game will start and you can begin playing against your opponent.

##Game Rules
The game is played on a 3x3 board. The first player to get three of their marks in a row, column, or diagonal wins. If all spaces on the board are filled without either player achieving three in a row, the game is a tie.

##Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

##License
This project is licensed under the MIT License - see the LICENSE file for details.
