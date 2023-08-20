from re import I
import pygame
from julia_set import process_color
import numpy as np


class ScreenConfig:
    def __init__(self, width: int = 600, height: int = 600,
                 title: str = "Julia set animation", fps: int = 10) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.fps = fps
        self.black = (43, 43, 43)

    @property
    def screen_size(self) -> tuple[int, int]:
        return (self.width, self.height)

    @property
    def center(self) -> tuple[int, int]:
        return (self.width // 2, self.height // 2)


screen_config = ScreenConfig()
clock = pygame.time.Clock()
pygame.display.set_caption(screen_config.title)
screen = pygame.display.set_mode(screen_config.screen_size)

ca = -0.70176
cb = -0.3842
is_need_reload = True
while True:
    clock.tick(screen_config.fps)
    width = screen_config.screen_size[0]
    height = screen_config.screen_size[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            ca = np.interp(x, (0, width), (-1, 1))
            cb = np.interp(y, (0, height), (-1, 1))
            is_need_reload = True

    if is_need_reload:
        screen.fill(screen_config.black)
        for x in range(width):
            for y in range(height):
                color = process_color(x, y, width, height, ca, cb)
                pygame.draw.circle(screen, color, (x, y), 1)
        is_need_reload = False

    pygame.display.update()
