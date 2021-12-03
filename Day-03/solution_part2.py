def read_input(filename):
    with open(filename) as file:
        return [f for f in file.read().splitlines()]


def extract_oxygen_rating(data, index):
    # Exit condition
    if len(data) == 1:
        return data[0]

    bit_counter = 0

    for row in data:
        if row[index] == '1':
            bit_counter += 1
        else:
            bit_counter -= 1

    most_common_bit = int(bit_counter >= 0)
    data = [row for row in data if row[index] == str(most_common_bit)]

    # Recursive call
    return extract_oxygen_rating(data, index + 1)


def extract_co2_rating(data, index):
    # Exit condition
    if len(data) == 1:
        return data[0]

    bit_counter = 0

    for row in data:
        if row[index] == '1':
            bit_counter += 1
        else:
            bit_counter -= 1

    least_common_bit = int(bit_counter < 0)
    data = [row for row in data if row[index] == str(least_common_bit)]

    # Recursive call
    return extract_co2_rating(data, index + 1)


def main():
    input = read_input("input.txt")

    oxygen = int(extract_oxygen_rating(input, 0), 2)
    co2 = int(extract_co2_rating(input, 0), 2)

    print(f"Oxygen: {oxygen}")
    print(f"CO2: {co2}")
    print(f"Solution: {oxygen * co2}")


if __name__ == '__main__':
    main()
