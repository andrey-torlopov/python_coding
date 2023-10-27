import curses
import time

from draw_engine import DrawEngine


def main(stdscr):
    engine = DrawEngine()
    run(stdscr)

    x = 0
    y = 0

    while True:
        time.sleep(0.02)
        stdscr.addch(x, y, "S")
        x += 1
        y += 1
        if x > 10:
            x = 00
        if y > 10:
            y = 0
        stdscr.refresh()

    stdscr.getch()


def run(stdscr):
    # Отключение автоматического вывода символов на экран и включение режима работы с клавишами
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    # Получение размеров терминала
    height, width = stdscr.getmaxyx()
    height -= 1
    width -= 1

    arr = [[' ' for _ in range(height)] for _ in range(width)]

    # Заполнение массива и вывод его на экран
    for i in range(height):
        for j in range(width):
            stdscr.addch(i, j, arr[j][i])

    # # Замена конкретного элемента в терминале
    # arr[90][25] = '0'
    # stdscr.addch(25, 90, arr[90][25])
    # stdscr.addstr(0, 0, f"Width: {width}, Height: {height}")

    stdscr.refresh()


if __name__ == '__main__':
    curses.wrapper(main)
    curses.wrapper(main)
