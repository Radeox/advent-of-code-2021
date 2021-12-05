class Field:
    def __init__(self, size):
        self.matrix = [[0 for x in range(size)] for y in range(size)]

    def __str__(self):
        # Print matrix in correct format
        rv = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                rv += str(self.matrix[j][i]) + ' '
            rv += '\n'
        return rv

    def add_line(self, x1, y1, x2, y2):

        # Check if line is horizontal
        if x1 == x2:
            for i in range(min(y1, y2), (max(y1, y2) + 1)):
                self.matrix[x1][i] += 1
        # Check if line is vertical
        elif y1 == y2:
            for i in range(min(x1, x2), (max(x1, x2) + 1)):
                self.matrix[i][y1] += 1
        # Line must be diagonal
        else:
            x_step = -1 if x1 > x2 else 1
            y_step = -1 if y1 > y2 else 1
            while x1 != x2 and y1 != y2:
                self.matrix[x1][y1] += 1
                x1 += x_step
                y1 += y_step
            self.matrix[x1][y1] += 1

    def count_dangerous_spots(self):
        rv = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] > 1:
                    rv += 1
        return rv


def read_input(filename):
    lines = []
    with open(filename) as f:
        for line in f.readlines():
            x1, tmp, y2 = line.strip().split(',')
            y1, x2 = tmp.strip().split('->')
            lines.append([int(x1), int(y1), int(x2), int(y2)])
    return lines


def main():
    lines = read_input('input.txt')
    field = Field(1000)

    for line in lines:
        field.add_line(*line)

    print(f"Solution: {field.count_dangerous_spots()}")


if __name__ == "__main__":
    main()
