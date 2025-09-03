import pygame

print('setup start')
pygame.init()
window = pygame.display.set_mode(size=(1000, 600))
print('setup end')

print('loop start')
while True:
    # checar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # fechar a janela
            quit()  # FIM PYGAME
