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
        basins = []

        for x in range(self.max_y):
            for y in range(self.max_x):
                if self.is_mimimum(x, y):
                    basins.append(set(self.explore_basin(x, y)))

        rv = 1
        for size in sorted([len((basin)) for basin in basins], reverse=True)[:3]:
            rv *= size
        return rv

    def explore_basin(self, x, y):
        rv = [(x, y)]
        neighbors, positions = self.get_neighbors(x, y)
        for index, neighbor in enumerate(neighbors):
            if neighbor < 9 and neighbor >= self.map[x][y] + 1:
                rv += self.explore_basin(positions[index]
                                         [0], positions[index][1])
        return rv

    def is_mimimum(self, x, y):
        return self.map[x][y] < min(self.get_neighbors(x, y)[0])

    def get_neighbors(self, x, y):
        neighbors = []
        positions = []

        # Get the neighbors in the four cardinal directions
        if x > 0:
            neighbors.append(self.map[x-1][y])
            positions.append((x-1, y))
        if x < self.max_y - 1:
            neighbors.append(self.map[x+1][y])
            positions.append((x+1, y))
        if y > 0:
            neighbors.append(self.map[x][y-1])
            positions.append((x, y-1))
        if y < self.max_x - 1:
            neighbors.append(self.map[x][y+1])
            positions.append((x, y+1))
        return neighbors, positions


def main():
    heightmap = HeightMap('input.txt')
    print(f"Solution: {heightmap.solve()}")


if __name__ == '__main__':
    main()
