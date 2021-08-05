from os import truncate


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Game:
    def __init__(self, board=[], moves=0):
        self.board = board
        self.moves = moves

    def get_height(self, position):
        height = 0
        for row in self.board:
            if row[position] != ' ':
                height += 1
        return (5-height)

    def move(self, player, position):
        height = self.get_height(position)
        self.board[height][position] = player.color
        self.moves += 1

    def calc_winner(self):
        pass

    def is_full(self):
        if self.moves == 42:
            return True
        return False

    def is_game_over(self):
        if self.is_full() == True:
            return True
        return False

def initialize_players():
    color_options = ['R', 'Y']
    player_1_name = input("\nEnter the name of player 1: ")
    while True:
        token_selection = input("Select R or Y: ")
        if token_selection.capitalize() == color_options[0]:
            player_1_color = color_options.pop(0)
            break
        elif token_selection.capitalize() == color_options[1]:
            player_1_color = color_options.pop(1)
            break
        else:
            print("Please select either R or Y: ")
    player_2_name = input("\nEnter the name of player 2: ")
    player_2_color = color_options.pop(0)
    player_1 = Player(player_1_name, player_1_color)
    player_2 = Player(player_2_name, player_2_color)
    return player_1, player_2


board = [
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ']
        ]

game = Game(board)
        
def main():
    list_of_players = list(initialize_players())
    while True:
        print(f"\nIt is {list_of_players[game.moves%2].name}'s turn")
        while True:
            try:
                player_move = int(input("\nSelect a column to place a piece (1-7): "))
                if player_move > 7 or player_move < 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("That is not a valid entry.")
                continue


        game.move(list_of_players[game.moves%2], player_move-1)
        for line in game.board:
            print("|".join(line))
        if game.is_game_over() == True:
            break

main()

