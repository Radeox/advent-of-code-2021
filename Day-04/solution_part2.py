class BingoBoard:
    def __init__(self, rows):
        self.rows = rows

    def mark_number(self, number):
        for row in self.rows:
            if number in row:
                row[row.index(number)] = 'X'

    def check_win_condition(self):
        # Check rows for winning condition
        for row in self.rows:
            if row == (['X'] * len(row)):
                return True

        # Check columns for winning condition
        for index, _ in enumerate(self.rows):
            column = [row[index] for row in self.rows]
            if column == (['X'] * len(column)):
                return True

    def get_board_score(self):
        sum = 0
        for row in self.rows:
            for number in row:
                if number != 'X':
                    sum += number
        return sum
    
    def __repr__(self):
        rv = '====================\n'
        for row in self.rows:
            rv += " ".join([str(n) for n in row]) + '\n'
        rv += '====================\n'
        return rv


def read_input(filename):
    draw_numbers = []
    bingo_boards = []

    with open(filename) as f:
        tmp = []
        counter = 0

        # Read first line and extract number to draw
        draw_numbers = [int(x) for x in f.readline().split(',')]

        # Read 5 lines and create bingo board
        for line in f.readlines():
            row = [int(num) for num in line.strip().split()]
            if row != []:
                tmp.append(row)
                counter += 1

            if counter == 5:
                bingo_boards.append(BingoBoard(tmp))
                tmp = []
                counter = 0

        return draw_numbers, bingo_boards


def main():
    draw_numbers, bingo_boards = read_input('input.txt')
    last_winning_num = 0
    last_winning_board = None
    
    for number in draw_numbers:
        for index, bingo_board in enumerate(bingo_boards):
            bingo_board.mark_number(number)
            
            if bingo_board.check_win_condition():
                # Remove completed board
                bingo_boards[index] = BingoBoard([[0] * 5 for _ in range(5)])

                last_winning_num = number
                last_winning_board = bingo_board

        if len(bingo_boards) == 0:
            break

    print(f"Draw: {last_winning_num}")
    print(f"Score: {last_winning_board.get_board_score()}")
    print(f"Solution: {last_winning_board.get_board_score() * last_winning_num}")

if __name__ == "__main__":
    main()
