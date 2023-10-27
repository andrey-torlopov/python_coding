# 2.4.1:

# s = "hello"
# a = [4, 10, 2]
# print(s, sep="-")
# print(*s, sep="-")
# print(a)
# print(*a, sep="")
# r = range(*a)
# for i in r:
#     print(i)
# print(r)
# print(list(r))
# print(list(range(*a)))

# 2.4.2:

# Дифференцирование

# P = [4, 5, 0, 2]
# dPdx = []
# for i, c in enumerate(P[:]):
#     dPdx.append(i * c)
# print(dPdx)  # [0, 0, 4] Ответ неправильный.


# 2.4.3.

#  [87, 75, 75, 50, 32, 32] -> [1,2,2,3,4,4]


# def make_categories(marks):
#     """
#     Тестируем метод
#     >>> a = [87, 75, 75, 50, 32, 32]
#     >>> b = [1,2,2,3,4,4]
#     >>> c = make_categories(a)
#     >>> c == b
#     True
#     """
#     result = [1]
#     for i in range(1, len(marks)):
#         if marks[i] != marks[i - 1]:
#             result.append(result[-1] + 1)
#         else:
#             result.append(result[-1])
#     return result


# 2.4.4
# метод Мадхавы–Лейбница для вычисления PI

from math import sqrt
from unittest import result


def calc_pi():
    """
    # >>> calc_pi()
    """
    a = 1 - 1 / 9
    for i in range(19):
        b = 3 + 2 * (i + 1)
        a += 1 / (b * 3**2)
    return sqrt(12) * a


# p = calc_pi()
# print(p)


# З2.4.1.

import numpy


def task_1(arr):
    """
    Написать небольшую программу на Python, которая
    по заданному мас- сиву a вычисляет массив того же размера p,
    в котором каждый элемент p[i] яв- ляется произведением всех
    целых чисел в массиве a, за исключением элемента a[i].
    Например, если
    >>> a = [1, 2, 3]
    >>> b = task_1(a)
    >>> t1 = [6, 3, 2]
    >>> b == t1
    True
    """
    result = []
    for i in range(len(arr)):
        m = 1
        for j in range(len(arr)):
            if i != j:
                m *= arr[j]
        result.append(m)
    return result


# a = task_1([1, 2, 3])


# З2.4.2.


def hamming_distance(string_1: str, string_2: str):
    """
    Расстояние Хэмминга (Hamming distance) между двумя строками рав- ной длины –
    это количество позиций, в которых символы различны. Написать небольшую программу
    на Python для вычисления расстояния Хэмминга между двумя строками s1 и s2.

    Например, в строке «ABCB» на четвертой позиции стоит буква «B», а в строке «ABCD» на
    той же позиции — буква «D». Расстояние Хэмминга между этими строками — 1.
    """
    distance = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            distance += 1
    return distance


# print(hamming_distance("abcde", "bcdef"))  # ➞ 5
# print(hamming_distance("abcde", "abcde"))  # ➞ 0
# print(hamming_distance("strong", "strung"))  # ➞ 1
# print(hamming_distance("ABBA", "abba"))  #  ➞ 4


# 32.4.4
def make_pascal_treangle(n):
    """
    Написать программу для вывода правильно
    отформатированного пред- ставления первых восьми строк треугольника Паскаля.
    """
    t = []
    for i in range(n):
        raw = [1] * (i + 1)

        for j in range(i + 1):
            if j != 0 and j != i:
                raw[j] = t[i - 1][j - 1] + t[i - 1][j]

        t.append(raw)

    return t


# t = make_pascal_treangle(5)
# for i in t:
#     print(i)


# З2.4.5.


def extract_triplete(secquense, frame):
    result = []
    for i in range(frame, len(secquense) - 2, 3):
        result.append(secquense[i : i + 3])

    return result


sec = "AGTCTTATATCT"
# print(extract_triplete(sec, 0))
# print(extract_triplete(sec, 1))
# print(extract_triplete(sec, 2))

# З2.4.6.
def double_factorial(n):
    result = 1

    if n % 2 == 0:
        return 1
    for i in range(1, n + 2, 2):
        result *= i

    return result


# print(double_factorial(5))
# for i in range(5):
#     print(i, end="")

# print()
# for i in range(5):
#     print(i)

#  ----------------

if __name__ == "__main__":
    import doctest

    doctest.testmod()
