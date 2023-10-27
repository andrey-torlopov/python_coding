import math


def foo():
    list = set()
    for i in range(300):
        for j in range(2, 1 + int(math.sqrt(i))):
            if not i % j:
                break
        else:
            list.add(i)
    return list


prime_numbers = foo()
print(prime_numbers)

p = 100_000_000


# def get_helper_number(p):
#     a = p
#     while True:
#         a += 2
#         if p % a != 0:
#             break

#     return a


# while p < 100_100_000:
#     p += 1
#     a = get_helper_number(p)

#     if a ** (p - 1) % p == 1:
#         print(f"Prime number: {p}")

# print("ok")
