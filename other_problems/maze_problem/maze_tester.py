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

from maze_problem import *

from sample_mazes import *

random = Random()

def create_random_maze(x, y, wall_density):

    maze = [[0 for _ in range(x)] for _ in range(y)]

    for i in range(y):
        for j in range(x):
            if int(random.random()*100) < wall_density:
                maze[i][j] = -2

    maze[random.randint(0, y-1)][random.randint(0, x-1)] = -1
    maze[random.randint(0, y-1)][random.randint(0, x-1)] = -3

    return maze

maze_puzzle_a_star = create_maze_problem(maze_initial_state_3, scan_diagonals=False)
search(maze_puzzle_a_star, ('A_star', distance_to_end_heuristic, avoid_turns_cost_function), 500000, ['loop_check'])
search(maze_puzzle_a_star, ('A_star', distance_to_end_heuristic), 500000, ['loop_check'])

maze_puzzle_best_first = create_maze_problem(maze_initial_state_2, scan_diagonals=False)
search(maze_puzzle_best_first, ('best_first', distance_to_end_heuristic), 500000, ['loop_check'])

random_maze = create_random_maze(10, 15, 40)
random_maze_problem = create_maze_problem(random_maze, scan_diagonals=True)
search(random_maze_problem, ('A_star', distance_to_end_heuristic), 5000, [])
