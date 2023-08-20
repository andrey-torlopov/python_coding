from PIL import Image
import numpy as np

julia_set = [(-0.70176, -0.3842), (0, 0.8), (0.45, 0.1428), (-0.7269, 0.1889)]
ca = -0.70176
cb = -0.3842
julia_index = 1

n_max = 100


def process_color(x: int, y: int, width: int, height: int, ca: float, cb: float) -> tuple[int, int, int]:
    color = (0, 0, 0)
    a = np.interp(x, (0, width), (-1.5, 1.5))
    b = np.interp(y, (0, height), (-1.5, 1.5))

    n = 0
    while n < n_max:
        a_new = a**2 - b**2
        b_new = 2 * a * b

        if abs(a + b) > 4:
            break
        a = a_new + ca
        b = b_new + cb

        n += 1

    bright = int(np.interp(n, (0, n_max), (0, 255)))
    color = (bright, bright, bright)
    if n == n_max:
        color = (0, 0, 0)

    return color


def create_image(width, height) -> Image:
    image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            color = process_color(x, y, width, height, ca, cb)
            image.putpixel((x, y), color)

    return image


def main() -> None:
    image_width = 500
    image_height = 500
    image = create_image(image_width, image_height)

    image.show()


if __name__ == "__main__":
    main()
    # test()
