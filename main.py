import pygame
import pygameMenu
from game import Game
from GUI import MainMenu
import sys



def exit():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def local():
    game = Game()
    game.run_DUO()

def multi():
    game = Game()
    game.run_LAN()

m = MainMenu()
m.add_option_wrapper('Local', local)
m.add_option_wrapper('Multi', multi)
m.add_option_wrapper('Exit', exit)

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    m.run()
