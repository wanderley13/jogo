import pygame

COLOR_RED = (178, 34, 34)
C_WITHE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Level1Bg4': 1,
    'Level1Bg5': 1,
    'Level1Bg6': 1,
    'Player1': 3,
    'Enemy1': 2,
    'Enemy2': 3,
    'Player1Shot': 30,
    'Player1Shot1': 40,
    'Enemy1Shot': 10,
    'Enemy2Shot': 15
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Enemy1': 50,
    'Enemy2': 30,
    'Player1Shot': 1,
    'Player1Shot1': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1
}

MENU_OPTION = ('JOGAR',
               'SAIR')

WIN_WIDTH = 1820
WIN_HEIGHT = 920

PLAYER_SHOOT = {'Player1': pygame.K_KP_ENTER}

ENTITY_SHOT_DELAY = {'Player1': 90,
                     'Enemy1': 125,
                     'Enemy2': 125}
