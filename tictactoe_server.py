import socket
import threading

class TicTacToeServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.connections = []
        self.players = {}
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_player = 0

    def start(self):
        self.server_socket.listen(2)
        print(f"Server started on {self.host}:{self.port}")

        # accept client connections
        while len(self.connections) < 2:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")
            self.connections.append(client_socket)
            client_socket.send(str(len(self.connections)-1).encode())

        # start the game
        self.send_board()
        self.current_player = 0
        self.connections[self.current_player].send(b'start')
        while True:
            data = self.connections[self.current_player].recv(1024).decode()
            if not data:
                break
            if not self.make_move(int(data)):
                self.connections[self.current_player].send(b'invalid')
                continue

            winner = self.check_winner()
            if winner is not None:
                self.send_message(f"Player {winner+1} wins!")
                self.send_board()
                self.close()
                break

            if ' ' not in self.board:
                self.send_message("Tie!")
                self.send_board()
                self.close()
                break

            self.current_player = (self.current_player + 1) % 2
            self.connections[self.current_player].send(b'opponent_move')
            self.send_board()

    def make_move(self, cell):
        if self.board[cell] != ' ':
            return False
        self.board[cell] = 'X' if self.current_player == 0 else 'O'
        return True

    def check_winner(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return i//3
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return i
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return 0
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return 1
        return None

    def send_board(self):
        for i in range(2):
            self.connections[i].send(''.join(self.board).encode())

    def send_message(self, message):
        for i in range(2):
            self.connections[i].send(message.encode())

    def close(self):
        for conn in self.connections:
            conn.close()
        self.connections = []

if __name__ == '__main__':
    hostname = socket.gethostname()
    IP_ADDRESS = socket.gethostbyname(hostname)

    print("IPv4 address:", IP_ADDRESS)
    server = TicTacToeServer(IP_ADDRESS, 1234)
    server.start()
