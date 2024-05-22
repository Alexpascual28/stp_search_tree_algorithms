## Test file for coursework 1

import sys
import os
from queen_cover  import *

# Since the queue and tree solver modules are in a different directory, we need to add the path to the system path
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, file_path)

# Importing the necessary modules
from solver.tree          import *
from solver.queue_search  import *

# Redirecting the output to a file
original = sys.stdout
sys.stdout = open('queen_coverage/tester_outcome.txt', 'w')

search(make_qc_problem(1,1), ('A_star', empty_squares_heuristic), 5000, [])
search(make_qc_problem(3,3), ('A_star', zero_heuristic), 5000, [])
search(make_qc_problem(4,4), ('A_star', empty_squares_heuristic), 5000, [])
search(make_qc_problem(5,5), ('A_star', empty_squares_heuristic), 5000, [])

search(make_qc_problem(5,6), ('A_star', empty_squares_heuristic), 5000, [])
search(make_qc_problem(6,5), ('A_star', empty_squares_heuristic), 5000, [])
search(make_qc_problem(10,3), ('A_star', zero_heuristic), 5000, [])

search(make_qc_problem(3,4), ('A_star', empty_squares_heuristic), 5000, [])
search(make_qc_problem(4,7), ('A_star', empty_squares_heuristic), 5000, [])
search(make_qc_problem(2,50), ('A_star', empty_squares_heuristic), 5000, [])
