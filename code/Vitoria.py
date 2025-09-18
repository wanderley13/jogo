import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_WITHE, COLOR_YELLOW

def victory_screen(window):
    font = pygame.font.SysFont("Arial", 60, bold=True)
    text = font.render("VOCÊ VENCEU!", True, COLOR_YELLOW)

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:  # qualquer tecla sai
                running = False

        window.fill(C_WITHE)
        text_rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        window.blit(text, text_rect)

        pygame.display.flip()
