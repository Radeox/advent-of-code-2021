def read_input(filename):
    rv = []
    with open(filename) as f:
        for line in f.readlines():
            input, output = line.split('|')
            rv.append([input.strip().split(), output.strip().split()])
    return rv


def main():
    display_output = read_input('input.txt')
    counter = 0

    for _, output in display_output:
        for digit in output:
            if len(digit) not in [5, 6]:
                counter += 1

    print(counter)


if __name__ == '__main__':
    main()
