class Submarine:
    def __init__(self, position, depth):
        self.position = int(position)
        self.depth = int(depth)

    def forward(self, distance):
        self.position += distance

    def dive(self, depth):
        self.depth += depth

    def surface(self, depth):
        self.depth -= depth


def main():
    submarine = Submarine(0, 0)

    with open('input.txt') as file:
        for line in file:
            command, distance = line.split()

            if command == 'forward':
                submarine.forward(int(distance))
            elif command == 'down':
                submarine.dive(int(distance))
            elif command == 'up':
                submarine.surface(int(distance))
            else:
                print('Invalid command!')
                break

    print(f"Solution: {submarine.position * submarine.depth}")


if __name__ == "__main__":
    main()
