def read_input(filename):
    rv = []
    with open(filename) as f:
        for line in f.readlines():
            input, output = line.split('|')
            rv.append([input.strip().split(), output.strip().split()])
    return rv


def contains(array1, array2):
    return all(i in array2 for i in array1)


def prepare_input(digit_input):
    return ["".join(sorted(digit)) for digit in digit_input]


def clean_segments(digit_input, decode_map):
    rv = []
    for digit in digit_input:
        digit = "".join(sorted(digit))
        if digit not in decode_map.values():
            rv.append(digit)
    return rv


def decode_input(digit_input):
    decode_map = {i: "" for i in range(10)}

    # 8 is always the same
    decode_map[8] = "abcdefg"

    # Sort the input
    digit_input = prepare_input(digit_input)

    # Get well known digits
    for digit in digit_input:
        if len(digit) == 2:
            decode_map[1] = digit
        elif len(digit) == 3:
            decode_map[7] = digit
        elif len(digit) == 4:
            decode_map[4] = digit

    digit_input = clean_segments(digit_input, decode_map)

    # Get 3 and 6 digit segments
    for digit in digit_input:
        if len(digit) == 5 and contains(decode_map[1], digit):
            decode_map[3] = digit
        elif len(digit) == 6 and not contains(decode_map[1], digit):
            decode_map[6] = digit

    digit_input = clean_segments(digit_input, decode_map)

    # Get the rest of the digits
    for digit in digit_input:
        # Could be 2 or 5
        if len(digit) == 5:
            if contains(digit, decode_map[6]):
                decode_map[5] = digit
            elif not contains(digit, decode_map[6]):
                decode_map[2] = digit
        # Could be 0 or 9
        elif len(digit) == 6:
            if contains(decode_map[3], digit):
                decode_map[9] = digit
            elif not contains(decode_map[3], digit):
                decode_map[0] = digit

    return {v: k for k, v in decode_map.items()}


def main():
    display_output = read_input('input.txt')
    counter = 0

    for line in display_output:
        decoder = decode_input(line[0])
        result = [decoder["".join(sorted(digit))] for digit in line[1]]
        counter += int("".join(map(str, result)))

    print("Solution: {}".format(counter))


if __name__ == '__main__':
    main()
