import math


def read_input(filename):
    with open(filename, 'r') as f:
        return [int(n) for n in f.readline().strip().split(',')]


def compute_minimal_distance(crabs):
    min = math.inf
    distance = 0
    max_distance = max(crabs)

    for distance in range(max_distance):
        cost = sum(abs(crab - distance) for crab in crabs)
        if cost < min:
            min = cost
    return min


def main():
    crabs = read_input('input.txt')
    print(f"Solution: {compute_minimal_distance(crabs)}")


if __name__ == '__main__':
    main()
