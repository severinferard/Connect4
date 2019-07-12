import numpy as np
import socket
from _thread import *
from network import Network
import time
import pygame
from GUI import graphic_client



class Game:

    def __init__(self):
        pygame.init()
        self.board = np.zeros(shape=(6, 7))
        self.pawns_color = {"1": (255, 0, 0),
                            "2": (255, 255, 0)}

    def __str__(self):
        return(np.array_repr(self.board))

    def place_pawn(self, player, col):
        for raw in range(5, -1, -1):
            if self.board[raw][int(col)] == 0:
                self.board[raw][int(col)] = player
                return True
        print("full")
        return False

    def check(self):
        # check for raw of 4
        for raw in self.board:
            for i in range(len(raw) - 3):
                if list(raw[i:i + 4]) == [1, 1, 1, 1]:
                    return(1)
                if list(raw[i:i + 4]) == [2, 2, 2, 2]:
                    return(2)
        # check for column of 4
        for i in range(len(self.board[0])):
            column = [self.board[j][i] for j in range(len(self.board))]
            for i in range(len(column) - 3):
                if list(column[i:i + 4]) == [1, 1, 1, 1]:
                    return(1)
                if list(column[i:i + 4]) == [2, 2, 2, 2]:
                    return(2)

        # check for diagonals
        for i in range(len(self.board) - 3):
            for j in range(len(self.board[0]) - 3):
                diag = [self.board[i][j],
                        self.board[i + 1][j + 1],
                        self.board[i + 2][j + 2],
                        self.board[i + 3][j + 3]
                        ]
                if diag == [1, 1, 1, 1]:
                    return(1)
                if diag == [2, 2, 2, 2]:
                    return(2)

            for j in range(len(self.board[0]) - 1, 2, -1):
                diag = [self.board[i][j],
                        self.board[i + 1][j - 1],
                        self.board[i + 2][j - 2],
                        self.board[i + 3][j - 3]
                        ]
                if diag == [1, 1, 1, 1]:
                    return(1)
                if diag == [2, 2, 2, 2]:
                    return(2)
        return(0)

    def opponent_id(self):
        if self.player_id == str(1):
            return 2
        return 1


    def run_LAN(self):
        self.nw = Network()
        self.gui = graphic_client(self.board)

        print("Waiting for opponent")
        self.gui.waitscreen()
        while int(self.nw.n_connected()) != 2:
            self.gui.waitscreen()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    break

        self.gui.win.fill((255, 255, 255))
        print("Opponent connected")
        print("Starting game")
        self.player_id = self.nw.id
        print("player_id", self.player_id)
        self.color = self.pawns_color[str(self.player_id)]

        self.gui.redraw()

        if self.player_id == str(1):
            choice = self.gui.chose_pos(self.color)
            self.place_pawn(1, int(choice))
            self.nw.send(f"{1}-{choice}")
            self.gui.update_board()

        self.run = True
        while self.run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("quit")
                    self.run = False

            status = self.nw.request()
            if str(self.player_id) != status[0] and len(status) > 1:
                opponent_choice = status[2]
                self.place_pawn(self.opponent_id(), opponent_choice)
                self.gui.update_board()

                check = self.check()
                if check:
                    print(f"You lose !")
                    self.gui.winner_is(f"You lose !")
                    self.run = False
                    break

                success = False
                while not success:
                    choice = self.gui.chose_pos(self.color)
                    success = self.place_pawn(self.player_id, choice)
                self.nw.send(f"{self.player_id}-{choice}")
                self.gui.update_board()

                check = self.check()
                if check:
                    print(f"You win !")
                    self.gui.winner_is(f"You win !")
                    self.run = False
                    break

    def run_DUO(self):

        pygame.time.delay(1000)
        pygame.event.clear()

        self.gui = graphic_client(self.board)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.gui.redraw()

        self.run = True
        while self.run:

            success = False
            while not success:
                choice = self.gui.chose_pos(self.red)
                success = self.place_pawn(1, choice)
            self.gui.update_board()

            check = self.check()
            if check:
                print(f"Player {check} won")
                self.gui.winner_is(f"Player {check} won !")
                self.run = False
                break

            pygame.time.delay(100)

            success = False
            while not success:
                choice = self.gui.chose_pos(self.yellow)
                success = self.place_pawn(2, choice)
            self.gui.update_board()

            check = self.check()
            if check:
                print(f"Player {check} won")
                self.gui.winner_is(f"Player {check} won !")
                self.run = False
                break



if __name__ == "__main__":
    game = Game()
    game.run_LAN()

