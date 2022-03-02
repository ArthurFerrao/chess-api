import re

TWO_SQUARES_MOVE = [
    {'direction': 'h', 'col': 2, 'row': 0},
    {'direction': 'v', 'col': 0, 'row': 2},
    {'direction': 'h', 'col': -2, 'row': 0},
    {'direction': 'v', 'col': 0, 'row': -2},
]
ONE_SQUARE_H_MOVE = [
    {'col': 1, 'row': 0},
    {'col': -1, 'row': 0},
]
ONE_SQUARE_V_MOVE = [
    {'col': 0, 'row': 1},
    {'col': 0, 'row': -1},
]

BASE_UNICODE_VALUE = 96


def move_position(pos, move):
    new_row = pos['row'] + move['row']
    new_col = pos['col'] + move['col']

    return {'row': new_row, 'col': new_col}


def valid_position(pos, board):
    return pos['col'] <= board.columns and pos['col'] >= 1 and pos['row'] <= board.rows and pos['row'] >= 1


def valid_coordinate_format(coordinate, board):
    valid = re.search('^[a-z][0-9]+$', coordinate)

    if valid:
        formatted = convert_coordinate_to_object(coordinate)
        valid = valid_position(formatted, board)

    return valid


def convert_algebraic_notation(pos):
    return chr(pos['col'] + BASE_UNICODE_VALUE) + str(pos['row'])


def convert_coordinate_to_object(coordinate):
    col = ord(coordinate[0]) - BASE_UNICODE_VALUE
    return {'col': col, 'row': int(coordinate[1])}


def remove_repetitions(coordinates):
    return list(dict.fromkeys(coordinates))


def moves_by_coodinate(coordinate, board):
    coordinates = []
    pos = convert_coordinate_to_object(coordinate)

    for two_squares in TWO_SQUARES_MOVE:
        two_squares_pos = move_position(pos, two_squares)

        if(two_squares['direction'] == 'h'):
            one_square_move = ONE_SQUARE_V_MOVE
        else:
            one_square_move = ONE_SQUARE_H_MOVE

        for one_square in one_square_move:
            new_pos = move_position(two_squares_pos, one_square)
            if(valid_position(new_pos, board)):
                coordinates.append(
                    convert_algebraic_notation(new_pos))

    return coordinates


def get_two_turns_moves(coordinate, board):
    coordinates = moves_by_coodinate(coordinate, board)
    possible_moves = []

    for new_coordinate in coordinates:
        possible_moves = possible_moves + \
            moves_by_coodinate(new_coordinate, board)

    return remove_repetitions(possible_moves)
