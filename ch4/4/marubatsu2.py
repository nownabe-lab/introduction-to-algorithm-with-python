import random

goals = [
    0b111000000, 0b000111000, 0b000000111,
    0b100100100, 0b010010010, 0b001001001,
    0b100010001, 0b001010100,
]

def check(board):
    for goal in goals:
        if board & goal == goal:
            return True
    return False


def print_board(p1, p2):
    for i in range(9):
        if p1.board & (1 << i) != 0:
            print(p1.char, end="")
        elif p2.board & (1 << i) != 0:
            print(p2.char, end="")
        else:
            print(" ", end="")

        if i % 3 == 2:
            print("")

class Player:
    def __init__(self, char):
        self.board = 0
        self.char = char

    def do(self, place):
        self.board |= place

    def is_winner(self):
        return check(self.board)


def minmax(next_player_board, prev_player_board, is_prev_player_self):
    if check(prev_player_board):
        if is_prev_player_self:
            return 1
        else:
            return -1

    board = next_player_board | prev_player_board
    if board == 0b111111111:
        return 0

    w = [i for i in range(9) if (board & (1 << i)) == 0]

    if is_prev_player_self:
        return min([minmax(prev_player_board, next_player_board | (1 << i), False) for i in w])
    else:
        return max([minmax(prev_player_board, next_player_board | (1 << i), True) for i in w])


def play(next_player, prev_player):
    if prev_player.is_winner():
        print(f'winner is {prev_player.char}')
        return

    board = next_player.board | prev_player.board
    if board == 0b111111111:
        print("no winner")
        return

    w = [i for i in range(9) if (board & (1 << i)) == 0]
    r = [minmax(prev_player.board, next_player.board | (1 << i), True) for i in w]
    i = [i for i, x in enumerate(r) if x == max(r)]
    j = w[random.choice(i)]
    next_player.do(1 << j)
    print_board(next_player, prev_player)
    print("---")
    play(prev_player, next_player)

p1 = Player("o")
p2 = Player("x")
play(p1, p2)

