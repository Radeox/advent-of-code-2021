def read_input(filename):
    with open(filename) as file:
        return [int(b) for b in file.read().splitlines()]


def check_depth_change(input):
    return sum(
        index > 0 and input[index] > input[index - 1]
        for index, _ in enumerate(input)
    )


def main():
    input = read_input("input.txt")
    print(f"Solution: {check_depth_change(input)}")


if __name__ == "__main__":
    main()
