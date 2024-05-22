from copy import deepcopy

# Representation of a state:
# (move_number, list_controlled_squares, (current_x_pos, current_y_pos),  full_board_state)
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

def maze_problem_info():
    pass

def get_initial_state(maze_initial_state):
    initial_position = find_initial_position(maze_initial_state)
    return 0, initial_position, maze_initial_state # Starting at the top-left corner

def find_initial_position(maze_initial_state):
    for i in range(len(maze_initial_state)):
        for j in range(len(maze_initial_state[i])):
            if maze_initial_state[i][j] == -1:
                return i, j

def possible_actions(state):
    surrounding_squares = get_surrounding_squares(state[1])

    if state[0] == 0:
        return knight_initial_moves()
    return knight_following_moves(state)

def get_surrounding_squares(position):
    x, y = position

    for x, y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if x >= 0 and y >= 0:
            yield x, y

def successor_state(action, state):
    # Returns new state after applying action
    pass

def is_goal_state(state):
    return state == (9, 9)  # Goal is bottom-right corner

# Return the problem specification for a given maze
def create_maze_problem(maze_initial_state):
    return (None,
            maze_problem_info,
            get_initial_state(maze_initial_state),
            possible_actions,
            successor_state,
            is_goal_state)
