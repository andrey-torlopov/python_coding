from curses.panel import top_panel
from operator import ge
from re import S
import pygame
import numpy as np
from point import Point
from game_engine import GameEngine
from screen_config import ScreenConfig
from score import Score

pygame.init()

screen_config = ScreenConfig()
clock = pygame.time.Clock()
pygame.display.set_caption(screen_config.title)
screen = pygame.display.set_mode(screen_config.screen_size)
game_engine = GameEngine(screen_config, screen)

points = [game_engine.create_first_point()]
pointCount = 1
score = Score()
font = pygame.font.Font(None, 36)

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
fruit_point = game_engine.generate_fuit(points)
fruit_color = game_engine.generate_random_color()
speed = 20

isGame = True

while True:
    clock.tick(screen_config.fps)
    screen.fill(screen_config.black)
    snake_animation_tick += 1
    fuit_tick += 1

    score_text = font.render(f"Score: {score.score}", True, (230, 230, 230))
    score_rect = score_text.get_rect()
    score_rect.center = (100, 30)

    # вывод height_score
    heigh_score_text = font.render(f"HighScore: {score.high_score}", True, (255, 255, 255))
    heigh_score_rect = score_text.get_rect()
    heigh_score_rect.center = (screen_config.width - 200, 30)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        direction = 4
        if previous_direction == 2:
            direction = 2
        previous_direction = direction
        isGame = True
    if keys[pygame.K_s]:
        direction = 3
        if previous_direction == 1:
            direction = 1
        previous_direction = direction
        isGame = True
    if keys[pygame.K_d]:
        direction = 2
        if previous_direction == 4:
            direction = 4
        previous_direction = direction
        isGame = True
    if keys[pygame.K_w]:
        direction = 1
        if previous_direction == 3:
            direction = 3
        previous_direction = direction
        isGame = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score.save_score()
            pygame.quit()
            exit()

    if isGame:
        if snake_animation_tick % speed == 0:
            snake_animation_tick = 0
            points = game_engine.process_points(
                points=points,
                direction=direction,
                max_points=pointCount)
            if points[-1].x == fruit_point.x and points[-1].y == fruit_point.y:
                pointCount += 1
                fruit_point = game_engine.generate_fuit(points)
                fruit_color = game_engine.generate_random_color()
                score.update_score()
            if len(points) > 3:
                speed = 10
            elif len(points) > 30:
                speed = 5
            elif len(points) > 50:
                speed = 1

            if game_engine.check_game_over(points=points):
                score.save_score()
                score.game_over()
                direction = 0
                previous_direction = 0
                points = [game_engine.create_first_point()]
                pointCount = 1
                speed = 20
                is_fruit = False
                isGame = False
                game_ove_text = font.render(f"Game Over", True, (255, 0, 0))
                game_ove_rect = score_text.get_rect()
                game_ove_rect.center = ((screen_config.width // 2) - 200, (screen_config.height // 2) - 30)

        if fuit_tick % 60 * 3 == 0 and not is_fruit:
            is_fruit = True

        if is_fruit:
            game_engine.draw_fruit(color=fruit_color, point=fruit_point)

        game_engine.draw(points=points)
        screen.blit(score_text, score_rect)
        screen.blit(heigh_score_text, heigh_score_rect)
    else:
        screen.blit(game_ove_text, game_ove_rect)

    pygame.display.update()
