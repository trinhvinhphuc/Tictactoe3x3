import tkinter as tk


class BoardClass():
    username = []
    p1name = ""
    p2name = ""
    movep1 = True
    mvcnt = 0
    gamesPlayed = 0
    p1win = 0
    p2win = 0
    numtie = 0
    p1loss = 0
    p2loss = 0
    bttnnum = 0
    currentmove = 0

    def __inti__(self):
        self.p1name = ""
        self.p2name = ""
        self.gamesPlayed = 0
        self.p1win = 0
        self.p2win = 0
        self.numtie = 0
        self.p1loss = 0
        self.p2loss = 0
        self.movep1 = None
        self.mvcnt = 0
        self.bttnnum = 0
        self.currentmove = 0

    def getusernames(self, p1name, p2name, window):
        self.player1 = tk.Label(window, text="Player 1:\n{}".format(p1name), font=("Verdana", "9")).grid(row=1, column=1)
        self.player2 = tk.Label(window, text="Player 2:\n{}".format(p2name), font=("Verdana", "9")).grid(row=1, column=3)

    def updateGamesPlayed(self):
        self.gamesPlayed = self.gamesPlayed + 1
        return self.gamesPlayed

    def resetGameBoard(self, playerval, fullbuttonlst):
        if playerval == "X":
            for button in fullbuttonlst:
                if button["state"] == "disabled":
                    button.config(text="", state="normal")
        if playerval == "O":
            for button in fullbuttonlst:
                if button["state"] == "disabled":
                    button.config(text="")
                if button["state"] == "normal":
                    button.config(text="", state="disabled")
        self.movep1 = True

    def manageTurns(self, p1turn, movecount, playervar, fullbuttonlst):
        self.mvcnt = movecount + 1
        if p1turn == True:
            if playervar == "O":
                self.enableBttn(fullbuttonlst)
            elif playervar == "X":
                self.disableBttn(fullbuttonlst)
        elif p1turn == False:
            if playervar == "X":
                self.enableBttn(fullbuttonlst)
            elif playervar == "O":
                self.disableBttn(fullbuttonlst)

        if p1turn == True:
            p1turn = False
        else:
            p1turn = True

        return [p1turn, self.mvcnt]

    def disableBttn(self, fullbuttonlst):
        for button in fullbuttonlst:
            if button["text"] == "" and button["state"] == "normal":
                button.config(state="disabled")

    def enableBttn(self, fullbuttonlst):
        for button in fullbuttonlst:
            if button["text"] == "" and button["state"] == "disabled":
                button.config(state="normal")

    def updateGameBoard(self, opponentbttnset, fullbuttonlst, bttnsendlst):
        for oppbutton in opponentbttnset:
            for button in fullbuttonlst:
                if (oppbutton == bttnsendlst[fullbuttonlst.index(button)]):
                    if {"Player1"}.issubset(opponentbttnset) == True:
                        button.config(text="X", bg="MistyRose3", fg="MistyRose2", state="disabled")
                    if {"Player2"}.issubset(opponentbttnset) == True:
                        button.config(text="O", bg="MistyRose3", fg="MistyRose2", state="disabled")

    def endgame(self, fullbuttonlst):
        for button in fullbuttonlst:
            if button["state"] == "normal":
                button.config(state="disabled")


    def isWinner(self, buttonset, winset, fullbuttonlst, pwin, bttnsendnum, button=None):
        if button != None:
            self.index = fullbuttonlst.index(button)
            self.bttnnum = bttnsendnum[self.index]
            buttonset.add(self.bttnnum)

        for setToWin in winset:
            if setToWin.issubset(buttonset) == True:
                self.endgame(fullbuttonlst)
                if {"Player2"}.issubset(buttonset) == True:
                    self.p2win = 1
                    self.p1loss = 1
                    self.movep1 = False

                elif {"Player1"}.issubset(buttonset) == True:
                    self.p1win = 1
                    self.p2loss = 1
                    self.movep1 = True
                pwin = True
        return [pwin, self.bttnnum, self.p1win, self.p1loss, self.p2win, self.p2loss]


    def boardIsFull(self):
        if self.mvcnt == 9:
            self.numtie = self.numtie + 1
        return self.numtie

    def printStats(self, playerval, window, lst_names, lst_stats, p1turn, tie):
        if playerval == "X":
            self.p1stat = tk.Label(window, text="Wins: {}\n\nLosses: {}\n\nTies: {}".format(lst_stats[0], lst_stats[1], lst_stats[4]), font=("Verdana", "12"))
            self.p1stat.grid(row=2, column=4, rowspan=2, columnspan=2)
        elif playerval == "O":
            self.p2stat = tk.Label(window, text="Wins: {}\n\nLosses: {}\n\nTies: {}".format(lst_stats[2], lst_stats[3], lst_stats[4]), font=("Verdana", "12"))
            self.p2stat.grid(row=2, column=4, rowspan=2, columnspan=2)

        if tie != True:
            if p1turn == True:
                self.lastmove = tk.Label(window, text="Last Winning Move By:\n{}".format(lst_names[1]),font=("Verdana", "10"))
            else:
                self.lastmove = tk.Label(window, text="Last Winning Move By:\n{}".format(lst_names[0]), font=("Verdana", "10"))
            self.lastmove.grid(row=4, column=4, columnspan=2)