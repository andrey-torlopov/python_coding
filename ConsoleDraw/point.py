class Point:

    def __init__(self, x: float, y: float = 0, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    # Определение оператора сложения
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    # Определение оператора вычитания
    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

     # Определение оператора умножения
    def __mul__(self, other: 'Point') -> 'Point':
        return Point(self.x * other.x, self.y * other.y, self.z * other.z)

    # Определение оператора деления
    def __truediv__(self, other: 'Point') -> 'Point':
        return Point(self.x / other.x, self.y / other.y, self.z / other.z)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})"
