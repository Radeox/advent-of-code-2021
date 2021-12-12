import math


class Consortium:
    def __init__(self, filename):
        self.population = self.read_input(filename)

    def __str__(self):
        rv = ""
        for line in self.population:
            for octopus in line:
                rv += f'{octopus} '
            rv += "\n"

        return rv

    def get_population(self):
        return len(self.population) * len(self.population[0])

    def read_input(self, filename):
        rv = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                rv.append([int(char) for char in line])
        return rv

    def next_step(self):
        counter = 0

        # Increase all energy levels by 1
        for x, row in enumerate(self.population):
            for y, octopus in enumerate(row):
                self.population[x][y] += 1

        # Check for octopuses with energy > 9 flash
        for x, row in enumerate(self.population):
            for y, octopus in enumerate(row):
                # If ready to flash but not already flashing
                if octopus > 9 and octopus != math.inf:
                    self.flash(x, y)

        # Set all octopuses that are flashing to 0 and return the number of octopuses that are still flashing
        for x, row in enumerate(self.population):
            for y, octopus in enumerate(row):
                if octopus == math.inf:
                    self.population[x][y] = 0
                    counter += 1

        return counter

    def flash(self, x, y):
        # Flash
        self.population[x][y] = math.inf

        # Increase the energy of all adjacent octopuses
        for xn, yn in self.get_neighbors(x, y):
            if self.population[xn][yn] <= 9:
                self.population[xn][yn] += 1

        for xn, yn in self.get_neighbors(x, y):
            # Recursively flash adjacent octopuses
            if self.population[xn][yn] > 9 and self.population[xn][yn] != math.inf:
                self.flash(xn, yn)

    def get_neighbors(self, x, y):
        rv = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i < 0 or x + i >= len(self.population):
                    continue
                if y + j < 0 or y + j >= len(self.population[x + i]):
                    continue
                rv.append((x + i, y + j))
        return rv


def main():
    consortium = Consortium('input.txt')
    counter = 0
    flashing = 0

    while flashing != consortium.get_population():
        flashing = consortium.next_step()
        counter += 1

    print(f'Solution: {counter}')


if __name__ == "__main__":
    main()
