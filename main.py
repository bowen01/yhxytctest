from BoardGrid import *
from BoardPiece import *
from WinningCond import *
from Movement import *
import numpy as np
from string import ascii_lowercase
from string import ascii_uppercase


# Converts the list of placed board pieces into a grid to be used by legal move checks and winner check
def list2grid(placed_pieces, board_length=12, board_width=8):

    # Reset the grid every time. When we implement recycling, list2grid should just work as a result
    new_grid = np.zeros((board_length, board_width), dtype=int)
    for piece in placed_pieces:
        # index numbering is reversed on the grid for legal check
        # grid numbering scheme was matched from check_winning
        if piece.side is 1:
            new_grid[board_length - piece.red_pos_y, piece.red_pos_x - 1] = 1
            new_grid[board_length - piece.white_pos_y, piece.white_pos_x - 1] = 4
        else:
            new_grid[board_length - piece.red_pos_y, piece.red_pos_x - 1] = 2
            new_grid[board_length - piece.white_pos_y, piece.white_pos_x - 1] = 3
    return new_grid


# Min max function can be separated similarly
def manual_entry(placed_pieces, recycle=False):
    # Dictionary simplifies conversion
    global alphabet2integer
    valid = False

    if recycle:
        while not valid:
            text_input = input("Recycle Input format: 'PosX PosY PosX PosY Type PosX PosY':")
            var_input = text_input.split()
            var_input[1], var_input[3], var_input[4], var_input[6] = int(var_input[1]), int(var_input[3]), int(var_input[4]), int(var_input[6])
            var_input[0], var_input[2], var_input[5] = alphabet2integer[var_input[0]], alphabet2integer[var_input[2]], alphabet2integer[var_input[5]]

            # LOGIC FOR RE-APPENDING SHOULD GO HERE

    else:
        while not valid:
            # Acquire entry, split and convert (where necessary)
            text_input = input("Input format: '0 Type PosX PosY':")
            var_input = text_input.split()
            var_input[1] = int(var_input[1])
            var_input[2] = alphabet2integer[var_input[2]]
            var_input[3] = int(var_input[3])

            # Note: Board pieces operate on a cartesian plane, (1, 1) is bottom left
            next_piece = BoardPiece(pos_x=var_input[2], pos_y=var_input[3], rot_type=var_input[1])
            placed_pieces.append(next_piece)
            new_grid = list2grid(placed_pieces)

            if isLegal(new_grid):
                valid = True
            else:
                valid = False
                del placed_pieces[-1]
                print("Invalid input")
        return placed_pieces, new_grid


# Global mapping via dictionary.
alphabet2integer = dict()
for index, letter in enumerate(ascii_lowercase):
    alphabet2integer[letter] = index + 1
for index, letter in enumerate(ascii_uppercase):
    alphabet2integer[letter] = index + 1


# "Controller" of players can be configured here via function name
entry_mode = {
    0: manual_entry,
    1: manual_entry
}


# Main loop, pretty self-explanatory
def __main__():
    cards_left = 24
    board_length = 12
    board_width = 8
    player_turn = 1
    game_over = False
    placed_pieces = list()

    #grid = np.zeros((board_length, board_width), dtype=int) #This line isn't necessary to initialize anymore

    visual_grid = BoardGrid(1280, 720, board_width, board_length)
    local_player_turn = 0

    while True:
        # player choice color is 0 and dot is 1
        player_choice = input('Player 1 will play colors(0) or dots(1)?')
        if player_choice.lower() in ("0", "colors"):
            player_choice = 0
            break
        elif player_choice.lower() in ("1", "dots"):
            player_choice = 1
            break
        else:
            print('You have entered wrong input! try colors or 0 or dots or 1')
    while not game_over or player_turn >= 60:
        local_player_turn = 1 if player_turn % 2 is 1 else 0
        
        print('player {}\'s turn'.format(1 if local_player_turn is 1 else 2))

        if cards_left <= 0:
            placed, grid = entry_mode[local_player_turn](placed_pieces, recycle=True)
        else:
            placed, grid = entry_mode[local_player_turn](placed_pieces, recycle=False)

        game_over, winner_list = check_winning(grid)
        cards_left -= 1
        player_turn += 1
        print (cards_left, player_turn)
        visual_grid.refresh(placed_pieces)

    print("Game Over")
    if player_turn >= 60:
        print('No one wins! it is a draw game!')
    elif (winner_list[0] + winner_list[1] > 0) and (winner_list[2] + winner_list[3] > 0):
        print('player {} won!'.format(1 if local_player_turn is 1 else 2))
    elif player_choice == 0 and (winner_list[0]==1 or winner_list[1]==1):
        print('player {} won! congratulation!'.format(1))
    elif player_choice == 1 and (winner_list[2]==1 or winner_list[3]==1):
        print('player {} won! congratulation!'.format(1))
    else:
        print('player {} won! congratulation!'.format(2))

    print(winner_list)


if __name__ == "__main__":
    __main__()
