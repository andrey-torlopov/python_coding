# def draw(screen, background, side: int, points: list[Point]) -> None:
#     '''
#     draw points on screen
#     '''
#     for point in points:
#         pygame.draw.rect(screen, background, (point.x * side, point.y * side, side, side))


# def draw_fruit(screen, background, side: int, point: Point) -> None:
#     pygame.draw.circle(screen, background, (point.x * side + side // 2, point.y * side + side // 2), side // 2)


# def process_points(
#     points: list[Point],
#     direction: int,
#     max_row: int,
#     max_col: int,
#     max_points: int
# ) -> list[Point]:
#     result = points
#     if direction == 1:
#         point = Point(points[-1].x, points[-1].y - 1)
#         if point.y < 0:
#             point.y = max_row - 1
#         result.append(point)
#     elif direction == 2:
#         point = Point(points[-1].x + 1, points[-1].y)
#         if point.x >= max_col:
#             point.x = 0
#         result.append(point)
#     elif direction == 3:
#         point = Point(points[-1].x, points[-1].y + 1)
#         if point.y >= max_row:
#             point.y = 0
#         result.append(point)
#     elif direction == 4:
#         point = Point(points[-1].x - 1, points[-1].y)
#         if point.x < 0:
#             point.x = max_col - 1
#         result.append(point)
#     remove_count = len(result) - max_points

#     if remove_count > 0:
#         result = result[remove_count:]

#     return result


# def generate_fuit(points: list[Point], max_row: int, max_col: int,) -> Point:
#     while True:
#         point = Point(random.randint(0, max_row - 1), random.randint(0, max_col - 1))
#         if point not in points:
#             return point
