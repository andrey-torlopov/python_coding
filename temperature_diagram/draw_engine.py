from screen_config import ScreenConfig
import pygame
from styles import Styles
import math
from data_provider import DataProvider


class DrawEngine:
    def __init__(
        self,
        screen_config: ScreenConfig,
        styles: Styles,
        data: DataProvider
    ) -> None:
        self.screen_config = screen_config
        self.styles = styles
        self.data = data

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption(self.screen_config.title)
        self.screen = pygame.display.set_mode(self.screen_config.screen_size)

        self.circle_radius = 210
        self.small_circle_radius = self.circle_radius // 2
        self.medium_circle_radius = 3 * self.circle_radius // 4
        self.draw_temperature_points = []
        circle_center = self.screen_config.center

        angle_delta = 0
        event_tick = 0
        radius_delta = 0.5
        minute_tick = 0

        while True:
            clock.tick(self.screen_config.fps)
            self.screen.fill(self.styles.background)

            event_tick += 1
            if self.data.has_data:
                minute_tick += 1

            if event_tick >= 120:
                event_tick = 0
                radius_delta *= -1

            if minute_tick >= 15:
                minute_tick = 0
                self.data.next_year()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                print("a")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # self.circle_radius += radius_delta

            pygame.draw.circle(self.screen, self.styles.black, circle_center, self.circle_radius * 1.1)
            pygame.draw.circle(self.screen, self.styles.circle_color, circle_center, self.circle_radius, 3)
            pygame.draw.circle(self.screen, self.styles.circle_color, circle_center, self.medium_circle_radius, 2)
            pygame.draw.circle(self.screen, self.styles.circle_color, circle_center, self.small_circle_radius, 1)

            angle_delta += math.pi * 0.001

            for i, month in enumerate(self.data.months):
                angle = math.radians((i - 2) * (360 / len(self.data.months)))
                # angle += angle_delta
                x = circle_center[0] + self.circle_radius * 1.2 * math.cos(angle)
                y = circle_center[1] + self.circle_radius * 1.2 * math.sin(angle)

                # Отрисовываем круглый фон для текста
                font = pygame.font.SysFont(*self.styles.text_font)
                text = font.render(month, True, self.styles.text_color)
                text_rect = text.get_rect()
                text_rect.center = (x, y)
                text_radius = text_rect.width // 2  # Радиус круга фона
                pygame.draw.circle(self.screen, self.styles.background, text_rect.center, text_radius)

                # Отрисовываем текст поверх фона
                rotated_text = pygame.transform.rotate(text, -math.degrees(angle + (math.pi / 2)))
                rotated_rect = rotated_text.get_rect(center=text_rect.center)
                self.screen.blit(rotated_text, rotated_rect.topleft)

            self.draw_data()
            self.draw_text()

            pygame.display.update()

    def draw_text(self) -> None:
        font = pygame.font.SysFont(*self.styles.text_font)
        title_font = pygame.font.SysFont(*self.styles.title_font)
        title_text = title_font.render(
            f"Global temperature change ({self.data.boundDates[0]} - {self.data.boundDates[-1]})", True, self.styles.text_color)

        zero_percent = font.render("0°С ", True, self.styles.text_color)
        one_percent = font.render("1°С ", True, self.styles.text_color)
        two_percent = font.render("2°С ", True, self.styles.text_color)

        title_rect = title_text.get_rect()
        zero_rect = zero_percent.get_rect()
        one_rect = one_percent.get_rect()
        two_rect = two_percent.get_rect()

        title_rect.center = (self.screen_config.center[0], 30)
        zero_rect.center = (self.screen_config.center[0], self.screen_config.center[1] - (self.circle_radius // 2))
        one_rect.center = (self.screen_config.center[0], self.screen_config.center[1] - (3 * self.circle_radius // 4))
        two_rect.center = (self.screen_config.center[0], self.screen_config.center[1] - (self.circle_radius))

        self.screen.blit(title_text, title_rect)
        self.screen.blit(zero_percent, zero_rect)
        self.screen.blit(one_percent, one_rect)
        self.screen.blit(two_percent, two_rect)

    def draw_data(self) -> None:
        if not self.data.has_data:
            return

        font = pygame.font.SysFont(*self.styles.text_font)
        year_title_text = font.render(self.data.year_title, True, self.styles.text_color)
        year_title_rect = year_title_text.get_rect()
        year_title_rect.center = (self.screen_config.center[0], self.screen_config.center[1])
        self.screen.blit(year_title_text, year_title_rect)

        first_point = []
        current_point: list[list[float]] = []
        x = 0.0
        y = 0.0
        for i, month_value in enumerate(self.data.year_temperatures):
            angle = math.radians((i-2) * (360 / len(self.data.months)))

            r = self.map_value(month_value, 0, 1, self.small_circle_radius, self.circle_radius)
            if r > self.circle_radius:
                r = self.circle_radius

            x = self.screen_config.center[0] + r * math.cos(angle)
            y = self.screen_config.center[1] + r * math.sin(angle)

            if i == 0:
                pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 4)
            elif i == len(self.data.year_temperatures) - 1:
                pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 4)
            else:
                pygame.draw.circle(self.screen, (255, 0, 0), (x, y), 4)

            if i == 0:
                first_point = [x, y]
            if i > 0 and i <= len(self.data.year_temperatures) - 1:
                pygame.draw.line(self.screen, (255, 0, 0), (x, y), (current_point[-1][0], current_point[-1][1]), 1)
            current_point.append([x, y])
        pygame.draw.line(self.screen, (255, 0, 0), (x, y), (first_point[0], first_point[1]), 1)

    def map_value(self, value: float, from_min: float, from_max: float, to_min: float, to_max: float) -> float:
        # Преобразование значения из одного диапазона в другой
        from_range = from_max - from_min
        to_range = to_max - to_min
        scaled_value = (value - from_min) / from_range
        mapped_value = to_min + (scaled_value * to_range)
        return mapped_value
