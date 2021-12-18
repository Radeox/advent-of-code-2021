from os import read


class Probe:
    def __init__(self, initial_vx, initial_vy):
        self.x = 0
        self.y = 0
        self.vx = initial_vx
        self.vy = initial_vy

    @property
    def position(self):
        return (self.x, self.y)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.vx > 0:
            self.vx -= 1
        elif self.vx < 0:
            self.vx += 1

        self.vy -= 1


def is_in_area(probe, x1, y1, x2, y2):
    return probe.x >= x1 and probe.x <= x2 and probe.y >= y1 and probe.y <= y2


def read_input(filename):
    with open(filename) as f:
        line = f.readline()
        x, y = line.split()[2:4]
        x1, x2 = x.replace('x=', '').replace(',', '').split('..')
        y1, y2 = y.replace('y=', '').replace(',', '').split('..')

        return (int(x1), int(y1), int(x2), int(y2))


def main():
    area = read_input('input.txt')
    hits = []
    for vx in range(1000):
        for vy in range(-1000, 1000):
            probe = Probe(vx, vy)

            for _ in range(1000):
                probe.move()
                if probe.vx == 0 and probe.x < area[0] or probe.x > area[2]:
                    break

                if is_in_area(probe, *area):
                    hits.append((vx, vy))
                    break

    print("Hits:", len(hits))


if __name__ == '__main__':
    main()
