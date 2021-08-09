class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Game:

    def __init__(self, board):
        self.board = [['X' for i in range(3)] for j in range(3)]

    def __repr__(self):
        board_lines = ""
        for line in self.board:
            board_lines += '|'.join(line)
            board_lines += '\n'
        print(board_lines)

    def move(self, x, y, player):
        # coordinate = input()
        self.board[y][x] = 'X'
        if self.board[y][x] != "":
            return "Already taken"

    def calc_winner(self):
        # for i in range(3):
        #     # check horizontal
        #     row = set(self.board[i])
        #     if row == {'X'}:
        #         return 'X'
        #     elif row == {'O'}:
        #         return 'O'
        # for i in range(3):
        #     col = []
        #     for j in range(3):
        #         col.append(self.board[j][i])
        #     col = set(col)
        #     if col == {'X'}:
        #         return 'X'
        #     elif col == {'O'}:
        #         return 'O'
        b = self.board
        if b[0][0] == 'X' and b[1][1] == 'X' and b[2][2] == 'X':
            return 'X'
        elif b[0][2] == 'X' and b[1][1] == 'X' and b[2][0] == 'X':
            return 'X'
        elif b[0][0] == 'O' and b[1][1] == 'O' and b[2][2] == 'O':
            return 'O'
        elif b[0][2] == 'O' and b[1][1] == 'O' and b[2][0] == 'O':
            return 'O'

            # check vertical
            # check diagonal

    def is_full():
        ...

    def is_game_over():
        ...


if __name__ == '__main__':

    game = Game(2)
    game.move(0, 0, 'player')
    game.move(1, 2, 'player')
    print(game.calc_winner())
    game.__repr__()
    # user will first be asked if player 1 is x or o
    # then the same for player 2
    # then ask player 1 where they want to mark (0 - 8)
    #  | |O
    #  |X|
    # O| |
