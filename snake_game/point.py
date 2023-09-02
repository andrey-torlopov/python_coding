class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    # def __eq__(self, __value: object) -> bool:
    #     return self.x == __value.x and self.y == __value.y

    # def __hash__(self) -> int:
    #     return hash((self.x, self.y))
