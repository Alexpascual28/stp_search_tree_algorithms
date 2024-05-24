# maze_tester.py
# by Alejandro Pascual San Roman (bdh532)
# University of York

# Tester for the maze path planning problem.

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

import sys
import os
import random

# Since the queue and tree solver modules are in a different directory, we need to add the path to the system path
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, file_path)

from solver.tree          import *
from solver.queue_search  import *

from maze_problem  import *

maze_initial_state_1 = [[-2, -2, -2, -1, -2, -2, -2, -2, -2, -2],
                        [-2,  0,  0,  0,  0,  0,  0, -2,  0, -2],
                        [-2,  0, -2, -2, -2, -2, -2, -2,  0, -2],
                        [-2,  0, -2,  0,  0,  0,  0, -2,  0, -2],
                        [-2,  0, -2,  0,  0,  0,  0, -2,  0, -2],
                        [-2,  0, -2,  0, -2, -2,  0, -2,  0, -2],
                        [-2,  0,  0,  0,  0, -2,  0, -2,  0, -2],
                        [-2, -2, -2, -2,  0, -2,  0, -2,  0, -2],
                        [-2,  0,  0,  0,  0, -2,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0, -2,  0,  0,  0, -2],
                        [-2, -3, -2, -2, -2, -2, -2, -2, -2, -2]]

maze_puzzle_1 = create_maze_problem(maze_initial_state_1)

search(maze_puzzle_1, ('A_star', distance_to_end_heuristic), 5000, [])
