import pygame
from screen_config import ScreenConfig

pygame.init()
screen_config = ScreenConfig()
clock = pygame.time.Clock()
pygame.display.set_caption(screen_config.title)
screen = pygame.display.set_mode(screen_config.screen_size)
font = pygame.font.Font(None, 30)

while True:
    clock.tick(screen_config.fps)
    screen.fill(screen_config.black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    test_text = font.render("Hello world! Превед мир!", True, (230, 230, 230))
    test_text_rect = test_text.get_rect()
    test_text_rect.center = (150, 30)

    screen.blit(test_text, test_text_rect)

    pygame.display.update()
