class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Game:
    def __init__(self, moves=0):
        self.board = [
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ']
        ]
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

    def check_if_valid_move(self, position):
        if self.board[0][position-1] == ' ':
            return True
        else:
            return False

    def calc_winner(self):
        directions = ['across', 'vertical', 'diagonal_up', 'diagonal_down']
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                for direction in directions:
                    match_count, pos_1, pos_2 = self.check_recursion(i,j,direction)
                    if match_count >= 3:
                        return True, pos_1, pos_2
        return False 

    def check_recursion(self,pos_1, pos_2, direction,match_count=0):
        if self.check_for_match(pos_1,pos_2, direction, match_count+1) == True:
            return self.check_recursion(pos_1, pos_2, direction, match_count+1)
        else:
            return match_count, pos_1, pos_2


    def check_for_match(self, pos_1, pos_2, direction, match_count):
        if direction == 'across':
            position_list = [pos_1, pos_2, pos_1, pos_2+match_count]
        elif direction == 'vertical':
            position_list = [pos_1, pos_2, pos_1+match_count, pos_2]
        elif direction == 'diagonal_up':
            position_list = [pos_1, pos_2, pos_1+match_count, pos_2+match_count]
        elif direction == 'diagonal_up':
            position_list = [pos_1, pos_2, pos_1-match_count, pos_2+match_count]
        try:
            if self.board[position_list[0]][position_list[1]] == self.board[position_list[2]][position_list[3]]:
                return True
        except:
            return False
        else:
            return False

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

game = Game()
        
if __name__ == '__main__':
    list_of_players = list(initialize_players())
    while True:
        print(f"\nIt is {list_of_players[game.moves%2].name}'s turn")
        while True:
            try:
                player_move = int(input("\nSelect a column to place a piece (1-7): "))
                if player_move > 7 or player_move < 1:
                    raise ValueError
                #else:
                    #break
            except ValueError:
                print("That is not a valid entry.")
                continue
            if game.check_if_valid_move(player_move) == True:
                game.move(list_of_players[game.moves%2], player_move-1)
                break
            else:
                print("\nThat column is full.  Select another column.")
                continue

        for line in game.board:
            print("|".join(line))
        if game.is_game_over() == True:
            result, pos_1, pos_2 = game.calc_winner()
            if result == True:
                print(f"You win!\nWinning connect 4 starting at {pos_1},{pos_2}")
            else:
                print("No winner!")
            break


