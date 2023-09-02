from PIL import Image
import numpy as np


def process_color(x: int, y: int) -> tuple[int, int, int, int]:
    return (0, 0, 0, 0)


def create_image(width, height):
    image = Image.new("RGB", (width, height))
    n_max = 100

    for x in range(width):
        for y in range(height):
            color = (0, 0, 0)
            a = np.interp(x, (0, width), (-1.5, 1.5))
            b = np.interp(y, (0, height), (-1.5, 1.5))

            n = 0
            z = 0
            ca = a
            cb = b

            while n < n_max:
                a_new = a**2 - b**2
                b_new = 2 * a * b

                a = a_new + ca
                b = b_new + cb

                if abs(a + b) > 16:
                    break

                n += 1

            bright = int(np.interp(n, (0, n_max), (0, 255)))
            color = (bright, bright, bright)
            if n == n_max:
                color = (0, 0, 0)

            image.putpixel((x, y), color)

    return image


def main():
    image_width = 500
    image_height = 500

    image = create_image(image_width, image_height)

    image.show()


if __name__ == "__main__":
    main()
    # test()
