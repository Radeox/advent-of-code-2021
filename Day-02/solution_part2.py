class Submarine:
    def __init__(self, position, depth, aim):
        self.position = int(position)
        self.depth = int(depth)
        self.aim = int(aim)

    def forward(self, distance):
        self.position += distance
        self.depth += distance * self.aim

    def dive(self, depth):
        self.aim += depth

    def surface(self, depth):
        self.aim -= depth


def main():
    submarine = Submarine(0, 0, 0)

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
