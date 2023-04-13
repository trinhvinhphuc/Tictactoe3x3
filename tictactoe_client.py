import socket
import threading
import sys
import tkinter as tk

class TicTacToeClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.player = None
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 20), width=3, height=1, command=lambda j=i: self.button_click(j))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.message_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.message_label.grid(row=3, column=0, columnspan=3)

        self.connect()

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.host, self.port))
        except:
            self.message_label.config(text="Could not connect to server")
            return
        self.player = int(self.client_socket.recv(1024).decode())
        self.message_label.config(text=f"You are player {self.player+1}")

        threading.Thread(target=self.receive_messages).start()

    def receive_messages(self):
        for button in self.buttons:
            button['state'] = "disable"
        while True:
            data = self.client_socket.recv(1024).decode()
            if data == 'start':
                for button in self.buttons:
                    button['state'] = "normal"
                continue
            if data == 'invalid':
                self.message_label.config(text="Invalid move")
                continue
            if data == 'opponent_move':
                self.message_label.config(text="Your turn!!")
                for button in self.buttons:
                    button['state'] = "normal"
                continue
            if data.startswith('Player '):
                # messagebox.showinfo("Message", data)
                self.message_label.config(text=data)
                break
            if data.startswith('Tie!'):
                self.message_label.config(text=data)
                break

            self.update_board(data)

        data = self.client_socket.recv(1024).decode()
        self.update_board(data)

        for button in self.buttons:
            button['state'] = "disable"

        self.client_socket.close()

    def update_board(self, board_str):
        self.board = list(board_str)
        for i, val in enumerate(self.board):
            if i < 9:
                self.buttons[i].configure(text=val)

    def button_click(self, cell):
        if self.board[cell] != ' ':
            self.message_label.config(text="Invalid move")
            return
        self.client_socket.send(str(cell).encode())

        self.message_label.config(text="Opponent's turn!!")
        for button in self.buttons:
            button['state'] = "disable"

    def start(self):
        self.root.mainloop()

if __name__ == '__main__':

    print(f"{sys.argv[1]}, {sys.argv[2]}")
    client = TicTacToeClient(sys.argv[1], int(sys.argv[2]))
    client.start()
