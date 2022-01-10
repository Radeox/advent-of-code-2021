class DeterministicDice:
    def __init__(self, value: int):
        self.value = value

    def roll(self) -> int:
        rv = self.value
        self.value += 1
        if self.value > 100:
            self.value = 1
        return rv

class Player:
    def __init__(self, name: str, initial_position: int):
        self.name = name
        self.position = initial_position
        self.score = 0

    def __repr__(self) -> str:
        return f"Player{self.name} - {self.position}"
        
    @property
    def is_winner(self) -> bool:
        return self.score >= 1000
    
    def move(self, dice: DeterministicDice):
        total_roll = sum(dice.roll() for _ in range(3))

        self.position += total_roll
        while self.position > 10:
            self.position = self.position - 10
        self.score += self.position

def read_input(filename: str) -> list:
    rv = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if "Player" in line:
                _, name, _, _, initial_position = line.split(" ")
                initial_position = int(initial_position)
                rv.append(Player(name, initial_position))
    return rv

def main():
    players = read_input("input.txt")
    dice = DeterministicDice(1)
    roll_counter = 0
    
    playing, waiting = players

    while True:
        playing.move(dice)
        roll_counter += 3
        if playing.is_winner:
            print(f"Solution: {waiting.score * roll_counter}")
            return
        else:
            playing, waiting = waiting, playing

if __name__ == "__main__":
    main()