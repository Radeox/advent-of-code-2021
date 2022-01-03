def read_input(filename: str) -> list:
    enhancement_algorithm = ""
    input_image = []

    with open(filename) as f:
        enhancement_algorithm = f.readline().strip()
        f.readline()
        for line in f.readlines():
            input_image.append(line.strip())
    return enhancement_algorithm, input_image


def convert_subimage_to_number(subimage: list) -> int:
    num = "".join(["".join(row) for row in subimage])
    num = num.replace("#", "1").replace(".", "0")
    return int(num, 2)


def add_border(image: list) -> list:
    # Add 2 pixel border to each side
    rv = ['.' * (len(image[0]) + 4)] * 2
    rv += [
        ".." + row + ".."
        for row in image
    ]
    rv += ['.' * (len(image[0]) + 4)] * 2
    return rv


def get_neighbors(image: list, x: int, y: int) -> list:
    rv = ['.'] * 9
    k = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or j < 0:
                continue
            if i >= len(image) or j >= len(image[0]):
                continue
            rv[k] = image[i][j]
            k += 1
    return rv


def enhance_image(input_image: list, enhancement_algorithm: str) -> list:
    rv = []
    for x in range(len(input_image)):
        new_row = []
        for y in range(len(input_image[x])):
            enhance_index = convert_subimage_to_number(
                get_neighbors(input_image, x, y))
            new_row.append(enhancement_algorithm[enhance_index])
        rv.append("".join(new_row))
    return rv


def main() -> None:
    enhancement_algorithm, input_image = read_input("input.txt")

    for _ in range(2):
        input_image = add_border(input_image)

    for _ in range(2):
        input_image = enhance_image(input_image, enhancement_algorithm)

    counter = sum(
        len([pixel for pixel in row if pixel == "#"]) for row in input_image
    )
    print(f"Solution: {counter}")


if __name__ == "__main__":
    main()
