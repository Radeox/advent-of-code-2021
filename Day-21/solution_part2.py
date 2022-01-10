# Solution by jonathanpaulson
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/21.py

# Brute force + Memoization.
# how many possible game states are there?
# 10 options for p1, 10 options for p2, 21 options for s1, 21 options for s2 -> 10*10*21*21 ~ 40,000
# total running time ~ state space * non-recursive time for one call ~ 40e3 * 27 ~ 120e4 = ~1M

# Game state
DP = {}


def read_input(filename: str) -> list:
    rv = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if "Player" in line:
                initial_position = int(line.split(' ')[-1]) - 1
                rv.append(initial_position)
    return rv


def count_win(player1, player2, state1, state2):
    # Given that A is at position p1 with score s1, and B is at position p2 with score s2, and A is to move,
    # return (# of universes where player A wins, # of universes where player B wins)
    if state1 >= 21:
        return (1, 0)
    if state2 >= 21:
        return (0, 1)
    if (player1, player2, state1, state2) in DP:
        return DP[(player1, player2, state1, state2)]
    ans = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                new_p1 = (player1+d1+d2+d3) % 10
                new_s1 = state1 + new_p1 + 1

                x1, y1 = count_win(player2, new_p1, state2, new_s1)
                ans = (ans[0]+y1, ans[1]+x1)
    DP[(player1, player2, state1, state2)] = ans
    return ans


def main():
    player1, player2 = read_input("input.txt")
    print(max(count_win(player1, player2, 0, 0)))


if __name__ == '__main__':
    main()
