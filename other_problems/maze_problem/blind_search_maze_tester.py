# blind_search_maze_tester.py
# by Alejandro Pascual San Roman (bdh532)
# University of York

# Tester for the blind informed search maze path planning problem.

# The maze is represented as a 2D array of integers, where:
# -2: wall
# -1: initial square
#  0: unvisited square
# -3: goal square
#  1+: visited square, in order of visitation

# Example maze:
# [ [-2, -2, -2, -1, -2, -2, -2, -2, -2, -2],
#   [-2,  0,  0,  0,  0,  0,  0,  0,  0, -2],
#   [-2, -2, -2, -2, -2, -2, -2, -2,  0, -2],
#   [-2,  0, -2,  0,  0,  0,  0, -2,  0, -2],
#   [-2,  0, -2,  0, -2, -2,  0, -2,  0, -2],
#   [-2,  0,  0,  0,  0, -2,  0, -2,  0, -2],
#   [-2, -2, -2, -2,  0, -2,  0, -2,  0, -2],
#   [-2,  0,  0,  0,  0, -2,  0,  0,  0, -2],
#   [-2, -3, -2, -2, -2, -2, -2, -2, -2, -2], ]

# The main interface function is:
#
# blind_informed_search(actual_maze, initial_known_maze, margins=0,
#                       scan_diagonals=False, change_scanning_strategy=False, max_node_increment=2000, max_node_limit=15000,
#                       print_goal_states=False,
#                       strategy=('A_star', distance_to_end_heuristic, avoid_turns_cost_function),
#                       max_nodes=20000,
#                       options=['loop_check', 'print_loops', 'hide_debug_info']):
#
# search(PROBLEM, STRATEGY, MAX_NODES, OPTIONS )
#
# PROBLEM is a problem specification tuple of the form:
#     ( initialise_func,     # function for problem initialisation (if not required put None)
#       problem_info_func,   # function to print out basic info about the problem
#       initial_state,       # initial state for search
#       poss_act_func,       # function operating on a state to return list of possible actions
#       successor_func,      # function operating on an action and a state to return successor state
#       goal_test_func       # Boolean function operating on a state to test if it is a goal
#     )
#
# Typically the PROBLEM argument will be a function call that returns a problem tuple.
#
# STRATEGY can be one of the following:
# 'breadth_first'
# 'depth_first'
# 'randomised_depth_first'
# ('uniform_cost', cost_func )
# ('best_first', heuristic_func )
# ('A_star', heuristic_func, cost_func )
# ('A_star', heuristic_func)              # if cost_func is omitted it defaults to path length
#
# heuristic_func  is a function that operates on a state to return an estimate of distance to goal
# cost_func       is a function that operates on a **node** to give the cost of reaching that node
#
# MAX_NODES is the maximum number of nodes that will be explored
#
# OPTIONS is a list, which can contain any selection of the following:
# 'node_dots'   --- print a dot every time a node is expanded (just so you can tell it is running)
# 'loop_check'  --- check if node already generated and if so discard it
# 'print_loops' --- print indication when a loop is detected (only useful with 'loop_check')
# 'print_ties' --- print indication when a new node ties in cost/heuristic with an existing node.
# 'show_expand' --- print out the state of the node being expanded
# 'hide_debug_info' --- hide printed out debug info


from blind_informed_search import *

# print_maze(add_obstacle_margins(yora_maze_1, 1))

#blind_informed_search(yora_maze_1, yora_maze_empty, margins=2, scan_diagonals=False)
blind_informed_search(yora_maze_1, yora_maze_empty, margins=2, scan_diagonals=True, change_scanning_strategy=True, max_node_increment=4000, max_nodes=4000)

# blind_informed_search(yora_maze_1, yora_maze_empty, margins=0, scan_diagonals=True, change_scanning_strategy=True, max_node_increment=4000, max_nodes=2000,)
# blind_informed_search(yora_maze_1, yora_maze_empty, margins=0, scan_diagonals=True, change_scanning_strategy=True, max_nodes=3000,)

# blind_informed_search(yora_maze_2, yora_maze_empty, margins=2, scan_diagonals=True, change_scanning_strategy=True, max_node_increment=4000, max_nodes=3000,)

# blind_informed_search(yora_maze_1, yora_maze_empty, strategy=('A_star', distance_to_end_heuristic, avoid_turns_cost_function), scan_diagonals=True, print_goal_states=True, margins=2)
# blind_informed_search(maze_initial_state_2, maze_initial_state_empty)
