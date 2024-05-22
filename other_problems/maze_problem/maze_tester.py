import sys
import os

# Since the queue and tree solver modules are in a different directory, we need to add the path to the system path
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, file_path)

from solver.tree          import *
from solver.queue_search  import *

from maze_problem  import *

maze_initial_state = [[-2, -2, -2, -1, -2, -2, -2, -2, -2, -2],
                      [-2,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                      [-2, -2, -2, -2, -2, -2, -2, -2,  0, -2],
                      [-2,  0, -2,  0,  0,  0,  0, -2,  0, -2],
                      [-2,  0, -2,  0, -2, -2,  0, -2,  0, -2],
                      [-2,  0,  0,  0,  0, -2,  0, -2,  0, -2],
                      [-2, -2, -2, -2,  0, -2,  0, -2,  0, -2],
                      [-2,  0,  0,  0,  0, -2,  0,  0,  0, -2],
                      [-2, -3, -2, -2, -2, -2, -2, -2, -2, -2]]

maze_puzzle = create_maze_problem(maze_initial_state)

search(maze_puzzle, ('A_star', distance_to_end_heuristic), 5000, [])
