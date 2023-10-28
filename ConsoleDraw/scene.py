import curses


class Scene:
    '''
    stdscr - содержит набор символов который мы задали вначале и можем 
    по x-y теперь рисовать элементы (если они корректно заданы в массиве)
    '''

    def __init__(self, stdscr, height: int, width: int) -> None:
        self.stdscr = stdscr
        self.height = height
        self.width = width
        self.screen_aspect = width / height
        self.letter_aspect = 58 / 126  # 1 / 2
        self.gradient = " .:!/r(l1Z4H9W8$@"
        self.gradient_size = len(self.gradient)  # возможно надо будет 2 вычесть

    def normalize(self, x: float, y: float) -> tuple[int, int]:
        rx = 2.0 * x / float(self.width) - 1
        ry = 2.0 * y / float(self.height) - 1
        return (rx, ry)

    def draw(self, x: int, y: int, char: str) -> None:
        self.stdscr.addch(y, x, char)

    # def draw_circle(self) -> None:
    #     for i in range(self.height):
    #         for j in range(self.width):
    #             x, y = self.normalize(j, i)
    #             x *= self.screen_aspect
    #             x *= self.letter_aspect
    #             if x * x + y * y < 0.3:
    #                 self.draw(j, i, '@')

    def get_char(self, distance_to_center: float, radius: float) -> str:
        normalized_distance = 1 - distance_to_center / radius
        char_index = int(normalized_distance * self.gradient_size)
        char_index = self.clamp(char_index, 0, self.gradient_size - 1)
        return self.gradient[char_index]

    def clamp(self, value: float, min_value: float, max_value: float) -> float:
        return max(min(value, max_value), min_value)
