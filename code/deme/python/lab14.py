class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

# class Game:
#     def__init__(self, board):
#     self.board = board

    # __repr__(): #returns a string, similar to str method
    #     '''returns a pretty string representation of the game board'''pass
board2 = {
    " ": " ",
    " ": " ",
    " ": " "
}
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
for row in board:
    print(row)
# board[2][1].append("X")