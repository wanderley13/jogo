import pygame.key

from code.Const import ENTITY_SPEED, WIN_WIDTH, PLAYER_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 500:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_DOWN] and self.rect.bottom < 900:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]


        if pressed_key[pygame.K_w] and self.rect.top > 500:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_s] and self.rect.bottom < 900:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_d] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_SHOOT[self.name]]:
            return PlayerShot(name=f'{self.name}Shot1', position=(self.rect.centerx, self.rect.centery))
