# Tic Tac Toe Game
Tic Tac Toe is a classic two-player game that challenges you to place your symbol in a 3x3 grid to achieve three in a row, either horizontally, vertically, or diagonally. This implementation of the game was written in Python and includes a graphical user interface (GUI) for easy gameplay. The game also supports remote gameplay over a network using socket-based architecture.

## Requirements
The following Python modules are required to run the Tic Tac Toe game:

+ tkinter
+ socket
+ threading
## Running the Game
 To run the game, follow these steps:

1. Clone or download the repository to your local machine.

2. Open the command prompt or terminal and navigate to the project directory.

3. To start Player 1, run the following command:
```
python player1.py
```
4. Player 1 will start and prompt you to enter the IP address and port number of Player 2.

5. To start Player 2, run the following command:

```
python player2.py
```

6. Player 2 will display their IP address and port number on the console. 

7. Once Player 1 has entered the required information, both players will be prompted to enter their names.

8. The game will start and you can begin playing against your opponent.

## Game Rules
The game follows the standard Tic Tac Toe rules:

1. The game is played on a 3x3 board.
2. Each player takes turns placing their symbol (either X or O) in an empty cell of the board.
3. The first player to get three of their symbols in a row, column, or diagonal wins the game.
4. If all spaces on the board are filled without either player achieving three in a row, the game is a tie.