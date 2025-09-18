import pygame

COLOR_RED = (178, 34, 34)
C_WITHE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 1,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Level1Bg4': 1,
    'Level1Bg5': 1,
    'Level1Bg6': 1,
    'Player1': 5,
    'Enemy1': 2,
    'Enemy2': 3,
    'Player1Shot': 40,
    'Player1Shot1': 40,
    'Enemy1Shot': 20,
    'Enemy2Shot': 40
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 90,
    'Enemy1': 180,
    'Enemy2': 170,
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

ENTITY_SHOT_DELAY = {'Player1': 0,
                     'Enemy1': 80,
                     'Enemy2': 80}


ENTITY_DANO = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Player1Shot': 2,
    'Player1Shot1': 2,
    'Enemy1Shot': 30,
    'Enemy2Shot': 50
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Player1': 0,
    'Enemy1': 1000,
    'Enemy2': 1000,
    'Player1Shot': 0,
    'Player1Shot1': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0
}
