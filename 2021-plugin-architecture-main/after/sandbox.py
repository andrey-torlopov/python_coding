# from typing import Any, Callable

# def foo(arguments: dict[str, Any], b: Callable[..., str]):
#     return b(**arguments)


# class Foo:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

# a = foo({"name": "BBB", "age": 11}, Foo)
# print(a.__dict__)


def function_start(func):
    def wrapper(*args, **kwargs):
        print(f"function [{ func.__name__}] start...")
        func(*args, **kwargs)
    return wrapper


@function_start
def add(x, y):
    print(x + y)

add(1, 2)