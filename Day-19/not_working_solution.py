import math


class Scanner:
    def __init__(self, name: str, beacons: list) -> None:
        self.beacons = beacons
        self.name = name
        self.x = 0
        self.y = 0
        self.z = 0

    def __repr__(self):
        return self.name

    def compute_pattern(self, index) -> list:
        return [
            compute_distance(self.beacons[index], beacon)
            for i, beacon in enumerate(self.beacons)
            if i != index
        ]

    def shift(self, coordinates: list) -> None:
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

        for beacon in self.beacons:
            beacon[0] += coordinates[0]
            beacon[1] += coordinates[1]
            beacon[2] += coordinates[2]


def compute_distance(beacon1: list, beacon2: list) -> list:
    return math.sqrt(
        math.pow((beacon1[0] - beacon2[0]), 2) +
        math.pow((beacon1[1] - beacon2[1]), 2) +
        math.pow((beacon1[2] - beacon2[2]), 2)
    )


def read_input(filename: str) -> list:
    rv = []

    with open(filename, 'r') as f:
        beacons = []
        name = ""
        for line in f.readlines():
            line = line.strip()
            if "scanner" in line:
                name = "".join(line.split(" ")[1:3])
            if len(line.split(',')) == 3:
                x, y, z = line.split(',')
                beacons.append([int(x), int(y), int(z)])
            elif beacons != []:
                rv.append(Scanner(name, beacons))
                name = ""
                beacons = []
        rv.append(Scanner(name, beacons))
    return rv


def common(lst1, lst2) -> list:
    return [x for x in lst1 if x in lst2]


def unique(lst) -> list:
    rv = []
    for element in lst:
        new = not any(
            element[0] == old[0] and
            element[1] == old[1] and
            element[2] == old[2] for old in rv
        )
        if new:
            rv.append(element)
    return rv


def find_correct_orientation(beacons1: list, beacons2: list) -> list:
    rotation = [
        [+1, +1, +1],
        [+1, +1, -1],
        [+1, -1, +1],
        [+1, -1, -1],
        [-1, +1, +1],
        [-1, +1, -1],
        [-1, -1, +1],
        [-1, -1, -1],
    ]

    for r in rotation:
        x, y, z = set(), set(), set()

        for i in range(len(max(beacons1, beacons2))):
            x.add(beacons1[i][0] + (beacons2[i][0] * r[0]))
            y.add(beacons1[i][1] + (beacons2[i][1] * r[1]))
            z.add(beacons1[i][2] + (beacons2[i][2] * r[2]))

        if len(x) == 1 and len(y) == 1 and len(z) == 1:
            break
    return [x.pop(), y.pop(), z.pop()]


def get_common_beacons(scanner1: Scanner, scanner2: Scanner) -> list:
    common_beacons_1 = []
    common_beacons_2 = []

    for index1 in range(len(scanner1.beacons)):
        distance_s1 = scanner1.compute_pattern(index1)

        for index2 in range(len(scanner2.beacons)):
            distance_s2 = scanner2.compute_pattern(index2)

            # That 10 is totally random :D
            if len(common(distance_s1, distance_s2)) >= 10:
                common_beacons_1.append(scanner1.beacons[index1])
                common_beacons_2.append(scanner2.beacons[index2])

    return common_beacons_1, common_beacons_2


def get_overlaps(scanners: list) -> list:
    overlaps = []
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i != j and (i, j) not in overlaps and (j, i) not in overlaps:
                cbi, cbj = get_common_beacons(scanners[i], scanners[j])

                if len(cbi) > 0 and len(cbj) > 0:
                    overlaps.append((i, j))
    return overlaps


def main():
    scanners = read_input("input_example.txt")
    overlaps = get_overlaps(scanners)

    while overlaps != []:
        i, j = overlaps.pop()
        cbi, cbj = get_common_beacons(scanners[i], scanners[j])

        if i > j:
            scanners[i].beacons = [
                b for b in scanners[i].beacons if b not in cbi
            ]
        else:
            scanners[j].beacons = [
                b for b in scanners[j].beacons if b not in cbj
            ]

        if len(cbi) > 0 and len(cbj) > 0:
            scanners[j].shift(find_correct_orientation(cbi, cbj))

    for scanner in scanners:
        print(scanner, scanner.x, scanner.y, scanner.z, len(scanner.beacons))
    total_beacons = sum(len(x.beacons) for x in scanners)

    print(f"Solution: {total_beacons}")

    print("==========================")
    print("NOT SOLVED")
    print("The first scanner seems okay but the rest are not")
    print("Need more thinking to solve it correctly")



if __name__ == '__main__':
    main()
