import pygame

from code.Menu import Menu


class Game:

    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(1000, 600))



    def run(self):

            while True:
                menu = Menu(self.window)
                menu.run()
                pass


                # checar eventos
                #  for event in pygame.event.get():
                 #   if event.type == pygame.QUIT:
                  #      pygame.quit()  # fechar a janela
                   #     quit()  # FIM PYGAME



