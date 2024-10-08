# maze_problem.py
# by Alejandro Pascual San Roman (bdh532)
# University of York

# Definition of Maze Path Planning search problem
# In a maze path planning problem, the goal is to find a path from the initial square to the goal square
# avoiding the walls and visiting each square only once

# The maze is represented as a 2D array of integers, where:

# Representation of a state:
# (move_number, (current_x_pos, current_y_pos), full_board_state)
# Example:
# (4, (1, 6), [[-2, -2, -2, -1, -2, -2, -2, -2, -2, -2],
#              [-2,  0,  0,  1,  2,  3,  4,  0,  0, -2],
#              [-2, -2, -2, -2, -2, -2, -2, -2,  0, -2],
#              [-2,  0, -2,  0,  0,  0,  0, -2,  0, -2],
#              [-2,  0, -2,  0, -2, -2,  0, -2,  0, -2],
#              [-2,  0,  0,  0,  0, -2,  0, -2,  0, -2],
#              [-2, -2, -2, -2,  0, -2,  0, -2,  0, -2],
#              [-2,  0,  0,  0,  0, -2,  0,  0,  0, -2],
#              [-2, -3, -2, -2, -2, -2, -2, -2, -2, -2]], )
#  
# -2: wall
# -1: initial square
#  0: unvisited square
# -3: goal square
#  1+: visited square, in order of visitation

from copy import deepcopy

def maze_problem_info():
    print("\nMaze Path Planning Problem.")
    print("Solves the given maze.\n")

def initialise_maze(maze_initial_state):
    global BOARD_X, BOARD_Y, INITIAL_POSITION, MAZE_INITIAL_STATE
    BOARD_X = len(maze_initial_state)
    BOARD_Y = len(maze_initial_state[0])
    INITIAL_POSITION = find_initial_position(maze_initial_state)
    MAZE_INITIAL_STATE = maze_initial_state

def get_initial_state():
    return 0, INITIAL_POSITION, MAZE_INITIAL_STATE # Starting at the top-left corner

def find_initial_position(maze_initial_state):
    for i in range(len(maze_initial_state)):
        for j in range(len(maze_initial_state[i])):
            if maze_initial_state[i][j] == -1:
                return i, j

def possible_actions(state):
    surrounding_squares = get_surrounding_squares(state[1], SCAN_DIAGONALS)
    return [square for square in surrounding_squares if state[2][square[0]][square[1]] == 0 or state[2][square[0]][square[1]] == -3] # Can only move to unvisited squares or the goal square

def get_surrounding_squares(position, scan_diagonals):
    x, y = position

    squares_to_scan = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)] if scan_diagonals else [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]

    # print(x, y)

    for i, j in squares_to_scan:
        if (i >= 0 and i < BOARD_X) and (j >= 0 and j < BOARD_Y):
            yield i, j

def successor_state(action, state):
    # Returns new state after applying action
    board = deepcopy(state[2])
    x_position = action[0]
    y_position = action[1]

    if board[x_position][y_position] == -3:
        move_number = -3
    else:
        move_number = state[0] + 1

    # Mark the square as visited
    board[x_position][y_position] = move_number

    return move_number, (x_position, y_position), board

def is_goal_state(state):
    if state[0] == -3:
        if PRINT_GOAL_STATE:
            print("\nGOAL STATE:")
            print_board_state(state)
        return True
    return False
    
def print_board_state(state):
    board = state[2]
    for row in board:
        for square in row:
            if square == -2:
                print("%4s" % "████", end='')
            elif square == -1:
                print("%4s" % "[S]", end='')
            elif square == -3:
                print("%4s" % "[G]", end='')
            else:
                print("%4i" % square, end='')
        print()

# HEURISTICS

def distance_to_end_heuristic(state):
    goal_position = find_goal(state[2])
    current_position = state[1]

    # Euclidean distance
    return ((goal_position[0] - current_position[0])**2 + (goal_position[1] - current_position[1])**2)**0.5

def find_goal(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == -3:
                return i, j

def zero_heuristic(state):
    return 0

# COST FUNCTION

# Each node takes the form:
# [parent_node, list_of_child_nodes, [action_path, state, cost, heuristic_value]]
# Representation of a state:
# (move_number, (current_x_pos, current_y_pos), current_full_board)

def avoid_turns_cost_function(node):
    """
    Calculates the cost of a node based on the number of turns in the path.

    Parameters:
    - node: The node to calculate the cost for.

    Returns:
    - The cost of the node.
    """
    path = node[2][0]  # Get the action path from the node
    cost = 0  # Initialize the cost to 0

    # Iterate through the path starting from the second position
    for i in range(1, len(path)):
        if i >= 2:
            # Check if the current position and the previous two positions form a straight line
            if not (path[i][0] - path[i-1][0] == path[i-1][0] - path[i-2][0] and path[i][1] - path[i-1][1] == path[i-1][1] - path[i-2][1]):
                cost += 1  # Increment the cost by 1 for each turn

    return cost

# CREATE MAZE PROBLEM

# Return the problem specification for a given maze
def create_maze_problem(maze_initial_state, scan_diagonals=True, print_goal_state=True):
    global SCAN_DIAGONALS, PRINT_GOAL_STATE
    SCAN_DIAGONALS = scan_diagonals
    PRINT_GOAL_STATE = print_goal_state
    return (initialise_maze(maze_initial_state),
            maze_problem_info,
            get_initial_state(),
            possible_actions,
            successor_state,
            is_goal_state)
