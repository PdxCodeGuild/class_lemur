class Player:
    def __init__(self, player_name, token):
        self.player_name = player_name
        self.token = token

class Game:
    def __init__(self, board, moves=1):
        self.board = board
        self.moves = moves
    
    def __repr__(self, player_input_dict):
        self.board = [
            [player_input_dict['1'], '|', player_input_dict['2'], '|', player_input_dict['3']],
            ['-', '+', '-', '+', '-'],  
            [player_input_dict['4'], '|', player_input_dict['5'], '|', player_input_dict['6']],
            ['-', '+', '-', '+', '-'], 
            [player_input_dict['7'], '|', player_input_dict['8'], '|', player_input_dict['9']],
        ]
        return self.board
    
    def move(self, x, y, player):
        self.moves += 1
        return x*y, player.token

    def calc_winner(self):
        pass

    def select_current_player(self):
        pass

    def is_full(self):
        if self.moves == 9:
            """board is full, game over"""
            pass

    def is_game_over(self):
        pass


player_1 = Player
player_2 = Player
game = Game

def main():
    token_options = ['X', 'O']
    rows_and_columns = ['1','2','3']
    player_list = [player_2, player_1]
    current_player1 = True
    player_1.player_name = input("\nEnter the name of player 1: ")
    while True:
        token_selection = input("Select X or O")
        if token_selection == token_options[0]:
            player_1.token = token_options.pop(0)
            break
        elif token_selection == token_options[1]:
            player_1.token = token_options.pop(1)
            break
        else:
            print("Please select either X or O")
    player_2.player_name = input("\nEnter the name of player 2: ")
    player_2.token = token_options.pop(0)
    while True:
        print(f"It's {player_list[game.moves%2]}'s turn.\n\tYou will select a row(1-3) and column(1-3).")
        
        while True:
            x_coordinate = input("\nSelect a row: ")
            if x_coordinate in rows_and_columns:
                x_coordinate = int(x_coordinate)
                break
        while True:
            y_coordinate = input("\nSelect a column: ")
            if y_coordinate in rows_and_columns:
                y_coordinate = int(y_coordinate)
                break
             
            
        


