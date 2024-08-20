## Test file for all problems

import sys
import os

from solver.tree import *
from solver.queue_search import *

from queen_coverage.queen_cover import *
from other_problems.Knight_problem.knights_tour import *
from other_problems.Eight_problem.eight_puzzle import *
from other_problems.Fill_array_problem.FillArray import *
from other_problems.Fill_list_problem.FillProblem import *
from other_problems.maze_problem.maze_problem import *
# from other_problems.maze_problem.blind_informed_search import *
from other_problems.maze_problem.sample_mazes import *

# Redirecting the output to a file
original = sys.stdout
sys.stdout = open('tester_outcome.txt', 'w')

eight_tile_puzzle_initial_state = [[7,1,5],
                                   [3,4,2],
                                   [8,0,6]]

search(make_qc_problem(10,12), ('A_star', empty_squares_heuristic), 5000, [])
search(get_knights_tour_problem(5,5), 'depth_first',   500000, ['loop_check'] )
search(make_eight_tile_problem(eight_tile_puzzle_initial_state), 'breadth_first', 50000, ['loop_check'] )
search(make_fill_problem(10), 'depth_first', 100000, ['loop_check'])
search(make_fill_array_problem(10), 'depth_first', 100000, ['loop_check'])

# search(create_maze_problem(maze_initial_state_1, scan_diagonals=False), ('A_star', distance_to_end_heuristic, avoid_turns_cost_function), 500000, ['loop_check'])
# blind_informed_search(yora_maze_1, yora_maze_empty, strategy=('A_star', distance_to_end_heuristic, avoid_turns_cost_function), print_goal_states=True, margins=2)