class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return f"Player('{self.name}', '{self.token}')"
    
    def __str__(self):
        return self.name

class Game:

    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]

    def __repr__(self):
        board_lines = ""
        for line in self.board:
            board_lines += '|'.join(line)
            board_lines += '\n'
        return board_lines

    def move(self, x, y, player):
        token = player.token
        if self.board[y][x] != " ":
            return print("Already taken")
        self.board[y][x] = token

    def calc_winner(self):
        # check horizontal
        for i in range(3):
            row = set(self.board[i])
            if row == {'X'}:
                return 'X'
            elif row == {'O'}:
                return 'O'

        # check vertical
        for i in range(3):
            col = []
            for j in range(3):
                col.append(self.board[j][i])
            col = set(col)
            if col == {'X'}:
                return 'X'
            elif col == {'O'}:
                return 'O'

        # check diagonal
        b = self.board
        if b[0][0] == 'X' and b[1][1] == 'X' and b[2][2] == 'X':
            return 'X'
        elif b[0][2] == 'X' and b[1][1] == 'X' and b[2][0] == 'X':
            return 'X'
        elif b[0][0] == 'O' and b[1][1] == 'O' and b[2][2] == 'O':
            return 'O'
        elif b[0][2] == 'O' and b[1][1] == 'O' and b[2][0] == 'O':
            return 'O'


    def is_full():
        ...

    def is_game_over():
        ...


if __name__ == '__main__':

    game = Game()
    player1 = Player('pete', 'X')
    player2 = Player('matt', 'O')
    print(game)
    game.move(0, 0, player1)
    print(game)
    game.move(0, 0, player2)
    print(game)

    print(game.calc_winner())


    print(player1)
    print(repr(player1))
    
    # user will first be asked if player 1 is x or o
    # then the same for player 2
    # then ask player 1 where they want to mark (0 - 8)
    #  | |O
    #  |X|
    # O| |
