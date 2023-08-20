from curses.panel import top_panel
from re import S
import pygame
import numpy as np
from point import Point
from game_engine import draw, process_points, draw_fruit, generate_fuit


class ScreenConfig:
    def __init__(self, width: int = 600, height: int = 600,
                 title: str = "Snake game", fps: int = 60,
                 side: int = 20) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.fps = fps
        self.black = (43, 43, 43)
        self.side = side
        self.foreground = (240, 240, 240)

    @property
    def screen_size(self) -> tuple[int, int]:
        return (self.width, self.height)

    @property
    def center(self) -> tuple[int, int]:
        return (self.width // 2, self.height // 2)

    @property
    def points_per_row(self) -> int:
        return self.width // self.side

    @property
    def points_per_col(self) -> int:
        return self.height // self.side


screen_config = ScreenConfig()
clock = pygame.time.Clock()
pygame.display.set_caption(screen_config.title)
screen = pygame.display.set_mode(screen_config.screen_size)

x = screen_config.points_per_row // 2
y = screen_config.points_per_row // 2
points = [Point(x, y)]
pointCount = 1

green_color = (193, 212, 60)

# 0 - stop
# 1 - up
# 2 - right
# 3 - down
# 4 - left
direction = 0
previous_direction = 0
snake_animation_tick = 0
fuit_tick = 0
is_fruit = False
fruit_point = generate_fuit(points, screen_config.points_per_row, screen_config.points_per_col)
speed = 20

while True:
    clock.tick(screen_config.fps)
    screen.fill(screen_config.black)
    snake_animation_tick += 1
    fuit_tick += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        direction = 4
        if previous_direction == 2:
            direction = 2
        previous_direction = direction
    if keys[pygame.K_s]:
        direction = 3
        if previous_direction == 1:
            direction = 1
        previous_direction = direction
    if keys[pygame.K_d]:
        direction = 2
        if previous_direction == 4:
            direction = 4
        previous_direction = direction
    if keys[pygame.K_w]:
        direction = 1
        if previous_direction == 3:
            direction = 3
        previous_direction = direction

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if snake_animation_tick % speed == 0:
        snake_animation_tick = 0
        points = process_points(
            points=points,
            direction=direction,
            max_col=screen_config.points_per_col,
            max_row=screen_config.points_per_row,
            max_points=pointCount)
        if points[-1].x == fruit_point.x and points[-1].y == fruit_point.y:
            pointCount += 1
            fruit_point = generate_fuit(points, screen_config.points_per_row, screen_config.points_per_col)
        if len(points) > 3:
            speed = 10
        elif len(points) > 30:
            speed = 5
        elif len(points) > 50:
            speed = 1

    if fuit_tick % 60 * 3 == 0 and not is_fruit:
        is_fruit = True

    if is_fruit:
        draw_fruit(screen, green_color, screen_config.side, point=fruit_point)

    draw(screen, screen_config.foreground, screen_config.side, points=points)

    pygame.display.update()
