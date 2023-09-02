from point import Point
import pygame
import random
from screen_config import ScreenConfig


class GameEngine:
    def __init__(self, screen_config: ScreenConfig, screen: pygame.Surface):
        self.screen_config = screen_config
        self.screen = screen
        self.point_count = 1

    @property
    def side(self) -> int:
        return self.screen_config.side

    @property
    def max_col(self) -> int:
        return self.screen_config.points_per_col

    @property
    def max_row(self) -> int:
        return self.screen_config.points_per_row

    def generate_random_color(self) -> tuple[int, int, int]:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        while abs(r - 240) < 40 and abs(g - 240) < 40 and abs(b - 240) < 40:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

        return (r, g, b)

    def draw(self, points: list[Point]) -> None:
        for point in points:
            point_y = point.y * self.side + self.screen_config.top_offset
            pygame.draw.rect(self.screen, self.screen_config.foreground, (point.x * self.side, point_y, self.side, self.side))

    def process_points(self,
                       points: list[Point],
                       direction: int,
                       max_points: int
                       ) -> list[Point]:
        result = points
        if direction == 1:
            point = Point(points[-1].x, points[-1].y - 1)
            if point.y < 0:
                point.y = self.max_row - 1
            result.append(point)
        elif direction == 2:
            point = Point(points[-1].x + 1, points[-1].y)
            if point.x >= self.max_col:
                point.x = 0
            result.append(point)
        elif direction == 3:
            point = Point(points[-1].x, points[-1].y + 1)
            if point.y >= self.max_row:
                point.y = 0
            result.append(point)
        elif direction == 4:
            point = Point(points[-1].x - 1, points[-1].y)
            if point.x < 0:
                point.x = self.max_col - 1
            result.append(point)
        remove_count = len(result) - max_points

        if remove_count > 0:
            result = result[remove_count:]

        return result

    def generate_fuit(self, points: list[Point]) -> Point:
        while True:
            point = Point(random.randint(0, self.max_col - 1), random.randint(0, self.max_row - 1))
            if point not in points:
                return point

    def draw_fruit(self, color: (int, int, int), point: Point) -> None:
        point_y = point.y * self.side + self.screen_config.top_offset
        pygame.draw.circle(self.screen, color, (point.x * self.side + self.side // 2, point_y + self.side // 2), self.side // 2)

    def create_first_point(self) -> Point:
        return Point(self.max_col // 2, self.max_row // 2)

    def check_game_over(self, points: list[Point]) -> bool:
        point_tuples = list(map(lambda point: (point.x, point.y), points))
        if len(point_tuples) != len(set(point_tuples)):
            return True
        return False
