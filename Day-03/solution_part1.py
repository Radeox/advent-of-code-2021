def read_input(filename):
    with open(filename) as file:
        return [f for f in file.read().splitlines()]


def compute_consumption_rates(data):
    bit_counter = [0] * len(data[0])

    for row in data:
        for index, bit in enumerate(row):
            if bit == '1':
                bit_counter[index] += 1
            else:
                bit_counter[index] -= 1
    gamma = [int(a > 0) for a in bit_counter]
    epsilon = [int(a < 0) for a in bit_counter]

    gamma_decimal = int(''.join(map(str, gamma)), 2)
    epislon_decimal = int(''.join(map(str, epsilon)), 2)

    print(f"Gamma: {gamma_decimal}")
    print(f"Epsilon: {epislon_decimal}")
    print(f"Power consumption: {gamma_decimal * epislon_decimal}")


def main():
    input = read_input("input.txt")
    compute_consumption_rates(input)


if __name__ == '__main__':
    main()
