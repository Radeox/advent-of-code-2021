def read_input(filename):
    with open(filename) as f:
        return [int(i) for i in f.readline().strip().split(',')]


def go_to_next_day(state):
    tmp = [0 for _ in range(9)]

    for index, day in enumerate(state):
        tmp[index - 1] += day
        tmp[index] = 0

    if state[0] > 0:
        tmp[6] += state[0]
        tmp[8] += state[0]

    return tmp


def main():
    days = 256
    state = [0 for _ in range(9)]

    for value in read_input('input.txt'):
        state[value] += 1

    for _ in range(days):
        state = go_to_next_day(state)

    print(f"Elements: {sum(state)}")


if __name__ == '__main__':
    main()
