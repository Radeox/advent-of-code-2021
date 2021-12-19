import ast
from copy import deepcopy

def read_input(filename):
    with open(filename) as f:
        return [ast.literal_eval(line.strip()) for line in f.readlines()]


def add(a, b):
    return reduce([a, b])


def reduce(root):
    root = deepcopy(root)

    while explode_and_split(root):
        pass

    return root


def explode_and_split(root):
    # Solution by 'immmun'
    # https://gist.github.com/mmun/1dcbffa39a948c7b4d6a8275177e7efa

    # We'll keep track of the relevant nodes for exploding and splitting while walking
    # through the tree. Since we don't have pointers to primitives in python we'll have
    # to store the parent pair and index pair so that we can perform updates.
    pair_left, i_left = None, None
    pair_right, i_right = None, None
    pair_split, i_split = None, None

    stack = [(0, [root, None], 0)]

    while stack:
        depth, pair, i = stack.pop()

        if isinstance(pair[i], int):
            # Keep track of where to split if we don't end up exploding
            if not pair_split and pair[i] >= 10:
                pair_split, i_split = pair, i

            # Keep track of most recent regular number (i.e. left of exploded number)
            pair_left, i_left = pair, i
        elif depth >= 4:
            # Keep iterating until the next regular number (i.e. right of exploded number)
            if stack:
                _, pair_right, i_right = stack.pop()
                while isinstance(pair_right[i_right], list):
                    pair_right, i_right = pair_right[i_right], 0

            # Perform explode
            if pair_left:
                pair_left[i_left] += pair[i][0]
            if pair_right:
                pair_right[i_right] += pair[i][1]
            pair[i] = 0

            return True
        else:
            # Push child numbers onto the stack
            stack.append((depth + 1, pair[i], 1))
            stack.append((depth + 1, pair[i], 0))

    # Perform split
    if pair_split:
        pair_split[i_split] = [pair_split[i_split] //
                               2, (pair_split[i_split] + 1) // 2]
        return True

    return False


def magnitude(pair):
    if isinstance(pair, int):
        return pair
    else:
        return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])


def main():
    numbers = read_input('input.txt')
    x = numbers[0]

    for number in numbers[1:]:
        x = add(x, number)

    print(magnitude(x))


if __name__ == '__main__':
    main()
