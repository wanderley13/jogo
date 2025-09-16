import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WITHE, WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.timeout = 2000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WITHE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps(): 0f}', C_WITHE, (10, WIN_WIDTH - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WITHE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewrite', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
