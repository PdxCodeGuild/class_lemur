from time import sleep

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __str__(self):
        return f'{self.name}: {self.token}'
    
    def __repr__(self):
        return f"Player('{self.name}', '{self.token}')"

class Game:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '], # self.board[0]
            [' ', ' ', ' '], # self.board[1]
            [' ', ' ', ' '], # self.board[2]
        ]


    def move(self, x, y, player):
        """Place a player's token character string at a given coordinate
        (top-left is 0, 0), x is horizontal position, y is vertical position.
        Returns True if the player needs to make a different move"""
        # token = player.token
        # b = self.board
        # b[x][y] = token
        if self.board[x][y] == ' ':
            self.board[x][y] = player.token
        else:
            print('nice try cheater')
            return True

        # print(token)
    
    def calc_winner(self):
        """return the string of the winning token or None if no winner"""
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                print(f"{self.board[i][0]} is the winner!")
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                print(f"{self.board[0][i]} is the winner!")
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":
            print(f"{self.board[1][1]} is the winner!")
            return True
    
    def is_full(self):
        """return True if game board is full, else return False"""
        for row in self.board:
            for position in row:
                if position == ' ':
                    return False
        print("The board is full.")
        return True

    
    def is_game_over(self):
        """return True if game board is full or a player has won"""
        if self.is_full() or self.calc_winner():
            print("Game Over")
            return True


    def __repr__(self):
        b = self.board
        return f"""
{b[0][0]}|{b[0][1]}|{b[0][2]}
{b[1][0]}|{b[1][1]}|{b[1][2]}
{b[2][0]}|{b[2][1]}|{b[2][2]}
"""

def main():
    game = Game()

    player1 = Player('bob', 'X')
    player2 = Player('gary', 'O')

    players = [player1, player2]

    index = 0
    while True:
        print(game)
        player = players[index % len(players)]
        print(player)
        # x = int(input('x: '))
        # y = int(input('y: '))
        grid_coord = {1:(0,0), 2:(1,0), 3:(2,0),
                  4:(0,1), 5:(1,1), 6:(2,1),
                  7:(0,2), 8:(1,2), 9:(2,2)}
        move = int(input("Pick a square 1-9: "))
        y,x = grid_coord[move]
        go_again = game.move(x, y, player)
        if go_again != True:
            index += 1
        game_over = game.is_game_over()
        if game_over:
            print(game.__repr__())
            break


if __name__ == '__main__':
    main()
    # player1 = Player('bob', 'X')
    # player2 = Player('gary', 'O')
    # print(player1)
    # print(player2)

    # game = Game()

    # print(game)

    # game.move(1, 1, player1)

    # print(game)
    
    # game.move(1, 1, player2)

    # print(game)

    # game.move(1, 2, player1)

    # print(game)