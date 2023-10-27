# В2.5.1.
import math
import random


def normalize_list(array):
    """
    Тестируем метод
    >>> a = [2, 4, 10, 6, 8, 4]
    >>> b = normalize_list([2, 4, 10, 6, 8, 4])
    >>> c = [0.0, 0.25, 1.0, 0.5, 0.75, 0.25]
    >>> b == c
    True
    >>> b == []
    False
    """
    min_value = min(array)
    max_value = max(array)
    return [(x - min_value) / (max_value - min_value) for x in array]


# В2.5.2.


def agm(x, y):
    """
    Написать цикл while для вычисления арифметико-геометрического среднего (АГС) двух
    положительных действительных чисел x и y,
    определяемо- го как предел последовательностей:
    >>> a = 5
    >>> b = 2
    >>> x = agm(a, b)
    >>> x == 2.01
    True
    """
    a = x
    b = y
    while a != b:
        a, b = round((a + b) / 2, 2), round(math.sqrt(a + b), 2)

    return a


# x = agm(5, 2)
# print(x)


# В2.5.3.


def convert_fizz_buzz_number(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x


def fizz_buzz(n):
    """
    % 3 => Fizz
    % 5 => Buzz
    % 3,5 => FizzBuzz
    >>> a = fizz_buzz(15)
    >>> a == '12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz'
    True
    """
    return "".join([str(convert_fizz_buzz_number(x)) for x in range(1, n + 1)])


# a = fizz_buzz(15)
# print(a)


# В2.5.4.
def make_alkan(n):
    """
    Неразветвленные молекулы алканов – это насыщенные углеводороды с общей
    стехиометрической формулой CnH2n+2, в которой атомы углерода обра- зуют
    простую
    цепочку, например бутан C4H10 описывается структурной форму- лой,
    которую можно представить в виде H3CCH2CH2CH3. Написать программу,
    выводящую структурную формулу таких алканов с заданной стехиометрией
    (предполагается, что n > 1). Например, при заданной стехиометрии
    stoich = 'C8H18' должен выводиться результат H3C-CH2-CH2-CH2-CH2-CH2-CH2-CH3.
    >>> s = make_alkan(3)
    >>> s == 'Error'
    True
    >>> s = make_alkan(4)
    >>> s == "H3C-CH2-CH2-CH2-CH3"
    True
    """
    if n % 2 != 0:
        return "Error"

    c = (n + 2 * n + 2 - 6) // 2
    result = ["H3C"]

    for i in range(c - 1):
        result.append("CH2")

    result.append("CH3")

    return "-".join(result)


# print(make_alkan(4))


# З2.5.2.


def weak_acid(TOL=1.0e-10):
    h = 0
    c = 0.01
    Ka = 1.78 * 10**-5

    while True:
        h1 = math.sqrt(Ka * (c - h))
        if abs(h1 - h) <= TOL:
            break
        h = h1

    return h


# print(weak_acid())

# З2.5.3.


def geron_method(num, x0=2000):
    x = x0

    while True:
        x_next = round((x + num / x) / 2, 2)
        if x_next == x:
            break

        x = x_next

    return x

# print(geron_method(2117519.73))

# З2.5.5.


def is_leap_year(year):
    """
    Определяем высокосный год:
    1 Если год не делится на 4, значит он обычный.
    2 Иначе надо проверить не делится ли год на 100.
    3 Если не делится, значит это не столетие и можно сделать вывод, что год високосный.
    4 Если делится на 100, значит это столетие и его следует проверить его делимость на 400.
    5 Если год делится на 400, то он високосный.
    6 Иначе год обычны
    """
    if year % 4 == 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 == 0:
        return True

    return False


def next_date(str_date, date_us=False):
    date_components = [int(x) for x in str_date.split("/")]
    is_leap_date = is_leap_year(date_components[-1])
    # if date_us and is_leap_date and date_components[0] == 2:
    d = date_components[1] if date_us else date_components[0]
    m = date_components[0] if date_us else date_components[1]
    y = date_components[2]

    d += 1
    if d == 29 and m == 2 and is_leap_date == False:
        d = 1
        m += 1
    elif d == 31 and m in [4, 6, 9, 11]:
        d = 1
        m += 1
    elif d > 31 and m != 12:
        d = 1
        m += 1
    elif d > 31 and m == 12:
        d = 1
        m = 1
        y += 1
    else:
        pass

    return f"{m}/{d}/{y}" if date_us else f"{d}/{m}/{y}"


# print(next_date("31/12/2014"))

# З2.5.6.


def calc_polinyak(n):
    """
    Формула Полиньяка.
    Подсчет нулей в числе факториала
    """
    s = 0
    for i in range(1, n + 1):
        a = n / 5**i
        s += int(a)

    return s


# print(calc_polinyak(10))
# print(math.factorial(10))


# З2.5.7.
def collatz_sequense(n):
    """
      Последовательность чисел-градин (hailstone sequence; гипотеза Коллат- ца – Collatz conjecture), начинающаяся с целого числа n > 0, генерируется с по- мощью многократно повторяющегося применения следующих трех правил:
     если n = 1, то последовательность завершается;
     если n четное, то следующее число последовательности равно n/2;
     если n нечетное, то следующее число последовательности равно 3n + 1.
    """
    result = []
    if n < 1:
        return result

    if n == 1:
        return [1]

    # start element
    x = n
    while True:
        if x == 1:
            break

        x = x / 2 if x % 2 == 0 else 3 * x + 1

        result.append(x)

    return result


# print(collatz_sequense(27))

# З2.5.10.


def monte_carlo_pi(n=10_000):
    """
    Метод вычисления числа PI с помощью случайных значений
    """
    s = 0
    for i in range(n):
        x = random.random()
        s += math.sqrt(1 - x**2)

    return (s / n) * 4


# print(monte_carlo_pi())

# З2.5.11.
def randomize_words(text):
    """
    Перемешать буквы внутри слов, сохраняя пунктуацию
    """
    pass


a: float = 1
print(a)


def foo(n: int = 1) -> int:
    return 1


print(foo(n=2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
