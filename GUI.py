import pygame
import numpy as np
import pygameMenu
import sys



class graphic_client():
    def __init__(self, board):
        pygame.init()
        self.board = board
        self.win = pygame.display.set_mode((500,500))
        self.win.fill((255, 255, 255))
        pygame.display.set_caption("Connect 4")


        self.offset = 85
        self.x = 50
        self.y= 100

    def waitscreen(self):

        font = pygame.font.Font('freesansbold.ttf', 28)
        text = font.render("Waiting for opponnent...Please wait",
                        True,
                        (0, 0, 0),
                        (125, 76, 255)
                        )

        text_rect = text.get_rect()
        w, h = pygame.display.get_surface().get_size()
        text_rect.center = (w//2, h//2)

        x = 300
        y = 200

        pygame.time.delay(100)
        self.win.blit(text, text_rect)
        pygame.display.update()

    def redraw(self):
        pygame.draw.rect(self.win,
                        (0, 0, 255),
                        (self.x, self.y,400,350)
                        )

        for raw in range(6):
            for col in range(7):
                pygame.draw.circle(self.win,
                            (255, 255, 255),
                            (self.offset+55*col,self.offset+50+55*raw),
                            25
                            )



        pygame.display.update()


    def update_board(self):

        for raw in range(6):
            for col in range(7):
                if self.board[raw, col] == 1:
                    pygame.draw.circle(self.win,
                                    (255, 0, 0),
                                    (self.offset+55*col,self.offset+50+55*raw),
                                    25
                                    )

                    pygame.display.update()

                if self.board[raw, col] == 2:
                    pygame.draw.circle(self.win,
                                    (255, 255, 0),
                                    (self.offset+55*col, self.offset+50+55*raw),
                                    25
                                    )

                    pygame.display.update()

    def chose_pos(self, color):

        self.pos = 3
        run = True
        while run:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("quit")
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                if 0 < self.pos:
                    self.pos -= 1
            if keys[pygame.K_RIGHT]:
                if self.pos < 6:
                    self.pos += 1
            if keys[pygame.K_RETURN]:
                pygame.draw.rect(self.win , (255, 255, 255), (50, 25, 400, 50))
                return self.pos

            pygame.draw.rect(self.win ,
                            (255, 255, 255),
                            (50, 25, 400, 50)
                            )
            pygame.draw.circle(self.win,
                            color,
                            (self.offset+55*self.pos, 50),
                            25
                            )
            pygame.display.update()

    def winner_is(self, winner):

        pygame.time.delay(100)
        pygame.event.clear()

        font = pygame.font.Font('freesansbold.ttf', 32)
        font2 = pygame.font.Font('freesansbold.ttf', 24)
        info_text = font.render(f"{winner}",
                        False,
                        (0, 0, 0),
                        (255, 255, 255)
                        )
        instruction_text = font2.render("Press ENTER to go back to menu",
                            False,
                            (0, 0, 0),
                            (255, 255, 255)
                            )
        info_text_rect = info_text.get_rect()
        instruction_text_rect = instruction_text.get_rect()
        w, h = pygame.display.get_surface().get_size()
        info_text_rect.center = (w//2, 50)
        instruction_text_rect.center = (w//2, h-25)


        pygame.time.delay(100)
        self.win.blit(info_text, info_text_rect)
        self.win.blit(instruction_text, instruction_text_rect)
        pygame.display.update()


        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:
                run = False
            pygame.display.update()


class MainMenu():
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((500,500))
        self.win.fill((255, 255, 255))
        H_SIZE = 500
        W_SIZE = 500
        pygame.display.set_caption("Connect 4 Main menu")
        self.main_menu = pygameMenu.Menu(self.win,
                             dopause=False,
                             font=pygameMenu.fonts.FONT_NEVIS,
                             menu_alpha=85,
                             menu_color=(125, 76, 255),
                             menu_color_title=(0, 0, 0),
                             menu_height=int(H_SIZE),
                             menu_width=500,
                             onclose=self.donothing,
                             rect_width=4,
                             title='Main menu',
                             title_offsety=5,
                             window_height=H_SIZE,
                             window_width=W_SIZE
                             )

    def add_option_wrapper(self, title, func):
        self.main_menu.add_option(title, func)

    def run(self):
        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    print('quit')
                    run = False
            self.main_menu.mainloop(events)
    @staticmethod
    def donothing():
        print("do nothing")



# class Lobby():

#     def __init__(self):
#         pass

#     def ask_nick(self):
#         textinput = pygame_textinput.TextInput()
#         textboxscreen = pygame.display.set_mode((200, 50))
#         pygame.display.set_caption("Enter a nickname")

#         run = True
#         while run:
#             textboxscreen.fill((255, 255, 255))

#             events = pygame.event.get()
#             for event in events:
#                 if event.type == pygame.QUIT:
#                     run = False

#             if textinput.update(events):
#                 string = textinput.get_text()
#                 run = False
#             textboxscreen.blit(textinput.get_surface(), (10,10))


#             pygame.display.update()
#         return string

#     def screen(self):
#         pygame.init()
#         win = pygame.display.set_mode((500,500))
#         win.fill((0, 0, 0))
#         w, h = pygame.display.get_surface().get_size()
#         pygame.display.set_caption("Lobby")
#         for i in range(10):
#             pygame.draw.rect(win, (20, 20, 20), (0, 100+50*i ,500,45))
#             pygame.draw.rect(win, (200, 200, 200), (0, 100+50*1 ,500,45), 2)

#         font = pygame.font.Font('freesansbold.ttf', 32)
#         font2 = pygame.font.Font('freesansbold.ttf', 24)
#         title = font.render("Play multiplayer", False, (255, 0, 255), (0, 0, 0))
#         instruction_text = font2.render("Select an opponent !", False, (255, 0, 255), (0, 0, 0))
#         instruction_text_rect = instruction_text.get_rect()
#         title_rect = title.get_rect()
#         title_rect.center = (w//2, 20)
#         instruction_text_rect.center = (w//2, 70)
#         win.blit(title, title_rect)
#         win.blit(instruction_text, instruction_text_rect)

#         self.pos = 0
#         run = True
#         while run:
#             pygame.time.delay(100)
#             events = pygame.event.get()
#             for event in events:
#                 if event.type == pygame.QUIT:
#                     run = False


#             pygame.draw.rect(win, (200, 200, 200), (0, 100+50*self.pos ,500,45), 2)

#             keys = pygame.key.get_pressed()

#             if keys[pygame.K_UP]:
#                 if 0 < self.pos:
#                     pygame.draw.rect(win, (20, 20, 20), (0, 100+50*self.pos ,500,45), 2)
#                     self.pos -= 1
#             if keys[pygame.K_DOWN]:
#                 if self.pos < 6:
#                     pygame.draw.rect(win, (20, 20, 20), (0, 100+50*self.pos ,500,45), 2)
#                     self.pos += 1
#             if keys[pygame.K_RETURN]:
#                 return self.pos
#             pygame.display.update()



