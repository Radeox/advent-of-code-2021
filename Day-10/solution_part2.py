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


def get_incomplete_lines(lines):
    rv = []

    for line in lines:
        corrupted = False
        stack = []

        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif char in [')', ']', '}', '>']:
                if not stack or is_corrupted(stack.pop(), char):
                    corrupted = True

        if not corrupted:
            rv.append(line)
    return rv


def get_autocomplete_score(lines):
    score_map = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    scores = []

    for line in lines:
        score = 0
        stack = []

        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif char in [')', ']', '}', '>']:
                stack.pop()

        stack.reverse()
        for char in stack:
            score = (score * 5) + score_map[char]
        scores.append(score)

    return sorted(scores)[int(len(scores)/2)]


def main():
    system_message = read_input('input.txt')
    incomplete_lines = get_incomplete_lines(system_message)
    print(f"Solution: {get_autocomplete_score(incomplete_lines)}")


if __name__ == "__main__":
    main()
