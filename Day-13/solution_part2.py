class PaperSheet:
    def __init__(self, x, y, dots):
        x = x+1
        y = y+1
        self.max_x = x
        self.max_y = y
        self.area = [[' ' for _ in range(x)] for _ in range(y)]

        for dot in dots:
            self.area[dot[1]][dot[0]] = '#'

    def __str__(self):
        return "".join("".join(row) + "\n" for row in self.area)

    def count_dots(self):
        return sum(row.count('#') for row in self.area)

    def fold_horizontal(self, y):
        new_paper = self.area[:y].copy()
        fold = list(reversed(self.area[y+1:self.max_y]))

        for x, row in enumerate(fold):
            for y, old_dot in enumerate(row):
                if old_dot == '#':
                    new_paper[x][y] = '#'

        self.area = new_paper

    def fold_vertical(self, x):
        new_paper = []
        fold = []
        for row in self.area:
            new_paper.append(row[:x].copy())
            fold.append(list(reversed(row[x+1:])))

        for x, row in enumerate(fold):
            for y, old_dot in enumerate(row):
                if old_dot == '#':
                    new_paper[x][y] = '#'

        self.area = new_paper


def read_input(filename):
    dots = []
    folds = []

    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('fold'):
                folds.append(line)
            elif line.count(',') == 1:
                dots.append([int(i) for i in line.split(',')])
            else:
                continue

    return dots, folds


def main():
    dots, folds = read_input('input.txt')

    # Find paper sheet dimensions
    max_x = max(i[0] for i in dots)
    max_y = max(i[1] for i in dots)

    paper = PaperSheet(max_x, max_y, dots)
    for fold in folds:
        if fold.count('y') == 1:
            y = int(fold.split('=')[-1])
            paper.fold_horizontal(y)
        elif fold.count('x') == 1:
            x = int(fold.split('=')[-1])
            paper.fold_vertical(x)

    print(f"Solution: \n{paper}")


if __name__ == '__main__':
    main()
