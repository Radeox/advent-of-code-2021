from collections import defaultdict


class Polymer:
    def __init__(self, polymer, grow_template):
        self.template = grow_template

        # Separate polymer into pairs
        self.polymer = {}
        for i in range(1, len(polymer)):
            reaction = polymer[i-1] + polymer[i]
            if reaction in self.polymer:
                self.polymer[reaction] += 1
            else:
                self.polymer[reaction] = 1

        # Init counters
        self.element_counter = defaultdict(int)
        for char in polymer:
            self.element_counter[char] += 1

    def __str__(self):
        return self.polymer

    def show_template(self):
        for ingredient in self.template:
            print(f"{ingredient} -> {self.template[ingredient]}")

    def trigger_reaction(self):
        # Thanks to 'zatoichi49' on reddit for this solution
        new_polymer = defaultdict(int)
        for pair, total in self.polymer.items():
            element = self.template[pair]
            pair1 = pair[0] + element
            pair2 = element + pair[1]

            self.element_counter[element] += total
            new_polymer[pair1] += total
            new_polymer[pair2] += total
        self.polymer = new_polymer.copy()

    def get_solution(self):
        mcp = max(self.element_counter.values())
        lcp = min(i for i in self.element_counter.values() if i > 0)
        return mcp - lcp


def read_input(filename):
    polymer, template = None, {}

    with open(filename) as file:
        polymer = file.readline().strip()
        for line in file.readlines():
            if line != '\n':
                ingredient, reaction = line.strip().split(' -> ')
                template[ingredient] = reaction
    return polymer, template


def main():
    polymer = Polymer(*read_input('input.txt'))
    for _ in range(40):
        polymer.trigger_reaction()
    print(f"Solution: {polymer.get_solution()}")


if __name__ == '__main__':
    main()
