import pygame

pygame.font.init()
SCREEN = pygame.display.set_mode((300, 300))
SCREEN.fill("blue")

font = pygame.font.SysFont("consolas", 30)
text = font.render("bonjour", False, "white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    SCREEN.blit(text, (10, 10))
    pygame.display.flip()
