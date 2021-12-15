class Polymer:
    def __init__(self, polymer, grow_template):
        self.polymer = polymer
        self.polymer_length = len(polymer)
        self.template = grow_template

    def __str__(self):
        return self.polymer

    def show_template(self):
        for ingredient in self.template:
            print(f"{ingredient} -> {self.template[ingredient]}")

    def trigger_reaction(self):
        new_polymer = ""
        previous_reacted = False
        for i, _ in enumerate(self.polymer[1:], start=1):
            reaction = self.polymer[i-1] + self.polymer[i]

            if reaction in self.template:

                if not previous_reacted:
                    new_polymer += self.polymer[i-1]

                new_polymer += self.template[reaction]
                new_polymer += self.polymer[i]
                previous_reacted = True
            else:
                previous_reacted = False
        self.polymer = new_polymer

    def most_common_polymer(self):
        most_common = "#"
        for i in range(65, 90):
            polymer = chr(i)
            if polymer in self.polymer and self.polymer.count(
                most_common
            ) < self.polymer.count(polymer):
                most_common = polymer
        return most_common

    def least_common_polymer(self):
        least_common = ""
        for i in range(65, 90):
            polymer = chr(i)
            if polymer in self.polymer and self.polymer.count(
                least_common
            ) > self.polymer.count(polymer):
                least_common = polymer
        return least_common

    def get_solution(self):
        mcp = self.polymer.count(self.most_common_polymer())
        lcp = self.polymer.count(self.least_common_polymer())
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
    polymer = Polymer(*read_input('input_example.txt'))
    for _ in range(10):
        polymer.trigger_reaction()
    print(f"Solution: {polymer.get_solution()}")


if __name__ == '__main__':
    main()
