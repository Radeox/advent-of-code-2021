def read_input(filename):
    with open(filename) as f:
        return [int(i) for i in f.readline().strip().split(',')]
    
def go_to_next_day(state):
    rv = []

    for fish in state:
        fish -= 1
        if fish < 0:
            rv.append(8)
            rv.append(6)
        else:
            rv.append(fish)
    return rv
            

def main():
    school_state = read_input('input.txt')
    days = 80

    for _ in range(days):
        school_state = go_to_next_day(school_state)

    print(f"Solution: {len(school_state)}")

if __name__ == '__main__':
    main()