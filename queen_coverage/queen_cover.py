#   queen_cover.py
#   by Alejandro Pascual San Roman
#   Student ID: 201255350
#
#  Specification of queen domination problem
#  In a queen domination puzzle, the minimum number of queens have to be placed in a m * n
#  chess board so that all rows, columns and diagonals are controlled or occupied by a queen

#  import print() and deepcopy() functions
from __future__ import print_function
from copy import deepcopy


# Representation of a state:
# (number_controlled_squares, list_controlled_squares, (current_x_pos, current_y_pos),  full_board_state)
# So on a 4x4 board after placing two queens we might have a state such as:
#
# (13, [(0, 0), (1, 0), (2, 0), (3, 0),
#       (0, 1), (1, 1), (2, 1), (3, 1),
#       (0, 2), (1, 2), (2, 2),
#       (0, 3)          (2, 3)          ], (1,0), [[0,0,1,0],
#                                                  [1,0,0,0],
#                                                  [0,0,0,0],
#                                                  [0,0,0,0]] )
#
# Since the queens are controlling 13 squares (the ones marked with an asterisk as follows):
#
# [*,*,*,*],
# [*,*,*,*],
# [*,*,*,0],
# [*,0,*,0]


# Defines the initial state: all values are empty
def qc_get_initial_state(x, y):
    global BOARD_X, BOARD_Y, qc_initial_state
    BOARD_X = x
    BOARD_Y = y
    return 0, [], (0, 0), matrix_of_zeros(x, y)


def matrix_of_zeros(x_value, y_value):
    return [[0 for x in range(x_value)] for y in range(y_value)]


# Goes through the array and counts all squares with a 0 on them
def qc_possible_actions(state):
    moves = []
    for x in range(BOARD_X):
        for y in range(BOARD_Y):
            if state[3][y][x] == 0:
                moves = moves + [(x, y)]
    return moves


def qc_successor_state(action, state):
    board = deepcopy(state[3])
    x_position = action[0]
    y_position = action[1]
    control_list = list(dict.fromkeys(state[1] + controlled_squares_list(x_position, y_position)))
    control_count = len(control_list)
    board[y_position][x_position] = 1
    return control_count, control_list, (x_position, y_position), board


# Outputs the list of controlled and occupied squares by a queen
def controlled_squares_list(x, y):
    row = queen_row(y)
    column = queen_column(x)
    diagonal = queen_diagonal(x, y)
    squares_list = list(dict.fromkeys(row + column + diagonal))  # To remove duplicate squares
    return squares_list


def queen_row(y):
    row = []
    for x in range(BOARD_X):
        row = row + [(x, y)]
    return row


def queen_column(x):
    column = []
    for y in range(BOARD_Y):
        column = column + [(x, y)]
    return column


# Calculate all squares controlled in diagonal by a queen in (x, y)
def queen_diagonal(x, y):
    diagonal_left_right = []  # Diagonal that goes from up left to down right
    diagonal_right_left = []  # Diagonal that goes from up right to down left

    # Initial position for left-to-right diagonal (as up and left as possible)
    min_left_right = min(x, y)
    x_left_right = x - min_left_right
    y_left_right = y - min_left_right

    # Initial position for right-to-left diagonal (as up and right as possible)
    x_difference = (BOARD_X - 1) - x  # Difference between x position of the queen and most right x border of the board
    min_right_left = min(x_difference, y)
    x_right_left = x + min_right_left
    y_right_left = y - min_right_left

    # Count squares in the left-to-right diagonal
    while x_left_right < BOARD_X and y_left_right < BOARD_Y:
        diagonal_left_right += [(x_left_right, y_left_right)]
        x_left_right += 1
        y_left_right += 1

    # Count squares in the right-to-left diagonal
    while x_right_left >= 0 and y_right_left < BOARD_Y:
        diagonal_right_left += [(x_right_left, y_right_left)]
        x_right_left += -1
        y_right_left += 1

    diagonal = list(dict.fromkeys(diagonal_left_right + diagonal_right_left))  # Remove duplicate squares
    return diagonal


def qc_test_goal_state(state):
    if state[0] == BOARD_X * BOARD_Y:
        print("\nGOAL STATE:")
        print_board_state(state)
        print("\nThe minimum number of queens to cover a ", BOARD_X, "*", BOARD_Y,
              " chessboard is equal to the \"Path Length\" below:")
        return True
    return False


def print_board_state(state):
    board = state[3]
    for row in board:
        for square in row:
            print(" %2i" % square, end='')
        print()


def qc_problem_info():
    print("\nQueen Domination Problem (", BOARD_X, "x", BOARD_Y, "board):")
    print("What is the minimum number of queens required to control this ", BOARD_X, "*", BOARD_Y, " board?\n")


# Heuristic
def empty_squares_heuristic(state):
    return BOARD_X * BOARD_Y - state[0]

def zero_heuristic(state):
    return 0

# Return the problem specification for a given board size
def make_qc_problem(x, y):
    global BOARD_X, BOARD_Y, qc_initial_state
    BOARD_X = x
    BOARD_Y = y
    qc_initial_state = qc_get_initial_state(x, y)
    return (None,
            qc_problem_info,
            qc_initial_state,
            qc_possible_actions,
            qc_successor_state,
            qc_test_goal_state
            )
