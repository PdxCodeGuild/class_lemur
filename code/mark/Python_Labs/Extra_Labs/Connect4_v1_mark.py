from time import sleep

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Game:
    def __init__(self, board=[]):
        self.board = board

    # def __str__(self):
    #     return self.board

    def get_height(self, position):
        height = 0
        for row in self.board:
            if row[position] != ' ':
                height += 1
        return (5-height)

    def move(self, player, position):
        # self.board = [
        #     [' ',' ',' ',' ',' ',' ',' '],
        #     [' ',' ',' ',' ',' ',' ',' '],
        #     [' ',' ',' ',' ',' ',' ',' '],
        #     [' ',' ',' ',' ',' ',' ',' '],
        #     [' ',' ',' ',' ',' ',' ',' '],
        #     [' ',' ',' ',' ',' ',' ',' ']
        # ]
        height = self.get_height(position)
        self.board[height][position] = player

        

    def calc_winner(self):
        pass

    def is_full(self):
        pass

    def is_game_over():
        pass



board = [
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ']
        ]

path = r"C:\Users\Mark\Desktop\pdx_code\class_lemur\code\mark\connect-four-moves.txt"


def read_file(path):
    with open(path, 'r', encoding="UTF8") as file:
        return file.read()

def convert_to_list(path):
    lines = read_file(path).split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
    return lines

player_1 = Player('player_1', 'Y')
player_2 = Player('player_2', 'R')
game = Game(board)
        
def main(path):
    moves_list = convert_to_list(path)
    for this_move in moves_list:
        game.move(this_move[1], int(this_move[2])-1)
        for line in game.board:
            print("|".join(line))
        sleep(1.5)
        print("\n\n")

main(path)

#convert_to_list(path)