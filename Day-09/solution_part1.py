class HeightMap:
    def __init__(self, filename):
        self.map = self.read_input(filename)
        self.max_x = len(self.map[0])
        self.max_y = len(self.map)

    def __str__(self):
        rv = ""
        for row in self.map:
            for num in row:
                rv += f'{num} '
            rv += "\n"
        return rv

    def read_input(self, filename):
        rv = []
        with open(filename) as f:
            for line in f.readlines():
                rv.append([int(num) for num in list(line.strip())])
        return rv

    def solve(self):
        count = 0

        for x in range(self.max_y):
            for y in range(self.max_x):
                if self.is_mimimum(x, y):
                    count += (self.map[x][y] + 1)
        return count

    def is_mimimum(self, x, y):
        return self.map[x][y] < min(self.get_neighbors(x, y))

    def get_neighbors(self, x, y):
        rv = []

        # Get the neighbors in the four cardinal directions
        if x > 0:
            rv.append(self.map[x-1][y])
        if x < self.max_y - 1:
            rv.append(self.map[x+1][y])
        if y > 0:
            rv.append(self.map[x][y-1])
        if y < self.max_x - 1:
            rv.append(self.map[x][y+1])
        return rv


def main():
    heightmap = HeightMap('input.txt')
    print(f"Solution: {heightmap.solve()}")


if __name__ == '__main__':
    main()
