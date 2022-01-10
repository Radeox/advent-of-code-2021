from copy import deepcopy


class Player:
    def __init__(self, name: str, initial_position: int):
        self.name = name
        self.position = initial_position
        self.score = 0

    def __repr__(self) -> str:
        return f"Player{self.name} - {self.position}"

    @property
    def is_winner(self) -> bool:
        return self.score >= 21

    def move(self, roll: int) -> None:
        self.position += roll
        while self.position > 10:
            self.position = self.position - 10
        self.score += self.position
        return


class Match:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.playing = self.player1
        self.waiting = self.player2

        self.move = 0
        self.remaining_rolls = 3

    @property
    def is_finished(self) -> bool:
        return self.player1.is_winner or self.player2.is_winner

    @property
    def winner(self) -> Player:
        if not self.is_finished:
            return None
        elif self.player1.is_winner:
            return self.player1
        else:
            return self.player2

    def roll(self, roll: int) -> None:
        self.remaining_rolls -= 1
        self.move += roll
        if self.remaining_rolls == 0:
            self.playing.move(self.move)
            self.remaining_rolls = 3
            self.move = 0
            self.playing, self.waiting = self.waiting, self.playing
        return


class Multiverse:
    def __init__(self, universe: list):
        self.evolving_universes = universe
        self.player1_wins = 0
        self.player2_wins = 0

    @property
    def is_finished(self) -> bool:
        return len(self.evolving_universes) == 0

    def play_turn(self) -> None:
        match = self.evolving_universes.pop()

        for i in range(1, 4):
            new_reality = deepcopy(match)
            new_reality.roll(i)
            if new_reality.is_finished:
                if new_reality.winner == new_reality.player1:
                    self.player1_wins += 1
                else:
                    self.player2_wins += 1
            else:
                self.evolving_universes.append(new_reality)
        return


def read_input(filename: str) -> list:
    rv = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if "Player" in line:
                name = line.split(' ')[1]
                initial_position = int(line.split(' ')[-1])
                rv.append(Player(name, initial_position))
    return rv


def main():
    players = read_input("input.txt")
    multiverse = Multiverse([Match(*players)])

    while not multiverse.is_finished:
        multiverse.play_turn()

    print("Solution:")
    if multiverse.player1_wins > multiverse.player2_wins:
        print(f"Player1 wins with {multiverse.player1_wins} points")
    else:
        print(f"Player2 wins with {multiverse.player2_wins} points")


if __name__ == "__main__":
    main()
