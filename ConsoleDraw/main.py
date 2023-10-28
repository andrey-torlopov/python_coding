import curses
import time
from math import sin, sqrt

from scene import Scene


def main(stdscr) -> None:
    scene = configure_screen(stdscr)
    t = 0
    while True:
        time.sleep(0.01)
        t += 1
        for i in range(scene.height):
            for j in range(scene.width):
                x, y = scene.normalize(j, i)
                x *= scene.screen_aspect
                x *= scene.letter_aspect
                x += sin(t * 0.01)

                distance_to_center = sqrt(x*x + y*y)
                radius = 0.6
                if distance_to_center <= radius:
                    char = scene.get_char(distance_to_center, radius)
                    scene.draw(j, i, char)
                else:
                    scene.draw(j, i, scene.gradient[0])

        # ---
        stdscr.refresh()


def configure_screen(stdscr) -> Scene:
    # Отключение автоматического вывода символов на экран и включение режима работы с клавишами
    curses.noecho()
    curses.curs_set(False)
    curses.cbreak()
    stdscr.keypad(True)

    # Получение размеров терминала
    height, width = stdscr.getmaxyx()
    height -= 1
    canvasArray = [' ' for _ in range(height * width)]

    # Заполнение массива и вывод его на экран
    for i in range(len(canvasArray)):
        x = i // width
        y = i % width
        stdscr.addch(x, y, canvasArray[i])

    return Scene(stdscr=stdscr, height=height, width=width)


if __name__ == '__main__':
    curses.wrapper(main)
    curses.wrapper(main)
