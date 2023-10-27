# def foo(x):
#     """
#     Тестируем метод
#     >>> a = 3
#     >>> b = 5
#     >>> a == b
#     False
#     >>> foo(3) == 3
#     True
#     """
#     return x

M = []


def add_element(x):
    """
    Добавляем элемент в кучу
             0
         1       2
     3    4   5     6
    7 8 9 10 11 12 13 14
    """
    M.append(x)
    p = len(M) - 1
    while (p > 0) and M[p] > M[(p - 1) // 2]:
        M[p], M[(p - 1) // 2] = M[(p - 1) // 2], M[p]
        p = (p - 1) // 2

def remove_first():
    M[0] = M.pop()
    p = 0
    while (2 * p + 1) < len(M):
        max = 2 * p + 1
        if 2 * p + 2 < len(M) and (M[2 * p + 2] > M[2 * p + 1]):
            max = 2 * p + 2

        if M[p] < M[max]:
            M[p], M[max] = M[max], M[p]
        p = max


# add_element(1)
# add_element(9)
# add_element(8)
# add_element(3)
# add_element(6)
# add_element(10)
# add_element(2)
# add_element(11)

M = [8, 7, 6, 3, 2, 4, 5]
# M = [5, 4, 6, 3, 2]
print(M)
remove_first()
print(M)
remove_first()
print(M)
remove_first()
print(M)
remove_first()
print(M)


def print_heap(arr):
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()


# a = M
# for i in a:
#     if 2 * i < len(a):
#         left_child = 2 * (i + 1) - 1
#         right_child = 2 * (i + 1)
#         print(
#             "For {}, children left {} and right {} ".format(i, left_child, right_child)
#         )

#     if (i + 1) // 2 > 0:
#         parent = (i + 1) // 2 - 1
#         print("For {}, parent  {}".format(i, parent))
