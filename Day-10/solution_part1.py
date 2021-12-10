def read_input(filename):
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]


def is_corrupted(char1, char2):
    return (
        (char1 != '(' or char2 != ')')
        and (char1 != '[' or char2 != ']')
        and (char1 != '{' or char2 != '}')
        and (char1 != '<' or char2 != '>')
    )


def get_syntax_score(lines):
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    score = 0

    for line in lines:
        stack = []

        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif char in [')', ']', '}', '>']:
                if not stack or is_corrupted(stack.pop(), char):
                    score += score_map[char]

    return score


def main():
    system_message = read_input('input.txt')
    print(f"Solution: {get_syntax_score(system_message)}")


if __name__ == "__main__":
    main()
