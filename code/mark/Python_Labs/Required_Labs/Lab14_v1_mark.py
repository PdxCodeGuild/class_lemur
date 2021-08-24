class Player:
    def __init__(self, player_name, token):
        self.player_name = player_name
        self.token = token


class Game:
    def __init__(self, board=[], moves=0):
        self.board = board
        self.moves = moves
    
    def __repr__(self, player_input_dict):
        self.board = f"\n\t{player_input_dict['1']}|{player_input_dict['2']}|{player_input_dict['3']}\n\t-+-+-\n\t{player_input_dict['4']}|{player_input_dict['5']}|{player_input_dict['6']}\n\t-+-+-\n\t{player_input_dict['7']}|{player_input_dict['8']}|{player_input_dict['9']}\n\n"
        return self.board
    
    def move(self, x, y, player):
        moves_list_dict = [{1:'1', 2:'2', 3:'3'},{1:'4', 2:'5', 3:'6'},{1:'7', 2:'8', 3:'9'}]
        return moves_list_dict[x-1][y], player.token
        #return x, y, player.token

    def calc_winner(self, player_input_dict):
        row_1 = (player_input_dict['1'] == player_input_dict['2'] == player_input_dict ['3'] != ' ')
        row_2 = (player_input_dict['4'] == player_input_dict['5'] == player_input_dict ['6'] != ' ')
        row_3 = (player_input_dict['7'] == player_input_dict['8'] == player_input_dict ['9'] != ' ')
        column_1 = (player_input_dict['1'] == player_input_dict['4'] == player_input_dict ['7'] != ' ')
        column_2 = (player_input_dict['2'] == player_input_dict['5'] == player_input_dict ['8'] != ' ')
        column_3 = (player_input_dict['3'] == player_input_dict['6'] == player_input_dict ['9'] != ' ')
        diag_1 = (player_input_dict['1'] == player_input_dict['5'] == player_input_dict ['9'] != ' ')
        diag_2 = (player_input_dict['3'] == player_input_dict['5'] == player_input_dict ['7'] != ' ')
        if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or diag_1 or diag_2:
            return True
        return False

    def select_current_player(self):
        return self.moves % 2

    def check_if_valid_move(self, move_loction, player_input_dict):
        if player_input_dict[move_loction] == ' ':
            self.moves += 1
            return True
        else:
            return False;


    def is_full(self):
        if self.moves == 9:
            return True
        return False

    def is_game_over(self, player_input_dict):
        winner_result = self.calc_winner(player_input_dict)
        if self.is_full() is True or winner_result is True:
            return True, winner_result
        else:
            return False, winner_result


def initialize_game():
    token_options = ['X', 'O']
    player_1_name = input("\nEnter the name of player 1: ")
    while True:
        token_selection = input("Select X or O: ")
        if token_selection == token_options[0]:
            player_1_token = token_options.pop(0)
            break
        elif token_selection == token_options[1]:
            player_1_token = token_options.pop(1)
            break
        else:
            print("Please select either X or O: ")
    player_2_name = input("\nEnter the name of player 2: ")
    player_2_token = token_options.pop(0)
    player_1 = Player(player_1_name, player_1_token)
    player_2 = Player(player_2_name, player_2_token)
    return player_1, player_2

game = Game()

def main():
    player_input_dict = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
    # player_input_dict = {
    #     '1':{'1':' ', '2':' ', '3':' '},
    #     '2':{'1':' ', '2':' ', '3':' '},
    #     '3':{'1':' ', '2':' ', '3':' '}
    # }
    rows_and_columns = ['1','2','3']
    player_1, player_2 = initialize_game()
    players_list = [player_1, player_2]
    while True:
        active_player = players_list[game.select_current_player()]
        print(f"\nIt's {active_player.player_name}'s turn.\n\nYou will select a row(1-3) and column(1-3).")
        valid_check = False
        while valid_check is False:
            while True:
                x_coordinate = input("\nSelect a row: ")
                if x_coordinate in rows_and_columns:
                    x_coordinate = int(x_coordinate)
                    break
                else:
                    print("That is not a valid selection.  Select 1, 2, or 3.")
            while True:
                y_coordinate = input("\nSelect a column: ")
                if y_coordinate in rows_and_columns:
                    y_coordinate = int(y_coordinate)
                    break
                else:
                    print("That is not a valid selection.  Select 1, 2, or 3.")
            move_location, token = game.move(x_coordinate, y_coordinate, active_player)
            valid_check = game.check_if_valid_move(move_location, player_input_dict)
            if valid_check == False:
                print("\nThat location is already occupied.  Select another square.\n")

            
        player_input_dict[move_location] = token 
        print(game.__repr__(player_input_dict))
        game_over, winner_result = game.is_game_over(player_input_dict)
        if game_over == True:
            if winner_result == True:
                print(f"\n\n\tGame Over, {active_player.player_name} has won!\n\n")
                break
            print("\n\n\tGame Over\n\n")
            break


main()

             
            
        


