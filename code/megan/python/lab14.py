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
            print("Already taken")
            return True
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


    def is_full(self):
        for i in range(3):
            for j in range(3):
                space = self.board[i][j]
                if space == ' ':
                    return False
        return True
        

    def is_game_over(self):
        if self.calc_winner() or self.is_full():
            if self.calc_winner() is not None:
                print(self.calc_winner() + " wins")
            elif self.is_full(): 
                print("Cats game!")
            return True
        else: 
            return False

if __name__ == '__main__':

    game = Game()

    player1 = Player(input("Please enter your name, Player One: "), "X")

    player2 = Player(input("Please enter your name, Player Two: "), "O")


index = 0
players = [player1, player2]

while game.is_game_over() == False:

    player = players[index % len(players)]
    print(player)

    player_x =  int(input("Please enter the x coordinate where you'd like to place your token: "))
    player_y =  int(input("Please enter the y coordinate where you'd like to place your token: "))


    go_again = game.move(player_x, player_y, player)
    if go_again != True:
        index += 1
    game.is_game_over()

    
    # game.move(player_x, player_y, player2)
    # game.is_game_over()


    print(game)
