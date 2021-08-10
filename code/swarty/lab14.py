'''
Lab 14: Tic-Tac-Toe –– Mob
Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

The Player class has the following properties:

name = player name
token = 'X' or 'O'
The Game class has the following properties:

board = your representation of the board
You can represent the board however you like, such as a 2D list, tuples, or dictionary.
'''
# imports
from time import sleep
#Classes
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
    def __str__(self):
        return f'{name}: {self.token}''

class Game:
    def __init__(self):         #start board
        self.board =[
            [' ', ' ', ' '],        
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        
        def move(self, x, y, player):
            """Place a player's token character string at a given coordinate (top-left is 0, 0), 
                x is horizontal position, y is vertical position."""
            if x == ' ':

        
        def calc_winner(self):
            """return the string of the winning token"""
        
        def is_full(self):
            """return true if the game board is full"""

        def is_game_over(self):
            """return true if game is full or has ben won"""
            if self.is_full() or self.calc_winner:
                return True
        def __str__(self):
            b=self.board
            return str("""
 {b[0][0]} | {b[0][1]} | {b[0][2]}
 {b[1][0]} | {b[1][1]} | {b[1][2]}
 {b[2][0]} | {b[2][1]} | {b[2][2]}
""")
        
def main():
    player1 = player('Bob', 'X')
    player2 = player('Sue', 'O')
    index = 0
    players=[player1,player2]
    while True:
        player = players[index % len(players)]
        print(player)
        x = input()
        index+=1
        x=input('row: ')
        y=input('comlumn: ')
        





if __name__ == '__main__':
    player1 = player('Bob', 'X')
    player2 = player('Sue', 'O')
    print(player1)
    print(player2)

    game = Game()

    print(game)

    game.move





#methods




