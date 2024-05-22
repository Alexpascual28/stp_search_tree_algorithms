## Test file for coursework 1

import sys
from tree          import *
from queue_search  import *
from queen_cover  import *

original = sys.stdout
sys.stdout = open('tester_outcome.txt', 'w')

def zero_heuristic(state):
    return 0

search(make_qc_problem(1,1), ('A_star', empty_squares_heuristic), 5000, [])
search(make_qc_problem(3,3), ('A_star', empty_squares_heuristic), 5000, [])
# search(make_qc_problem(4,4), ('A_star', empty_squares_heuristic), 5000, [])
# search(make_qc_problem(5,5), ('A_star', empty_squares_heuristic), 5000, [])

# search(make_qc_problem(5,6), ('A_star', empty_squares_heuristic), 5000, [])
# search(make_qc_problem(6,5), ('A_star', empty_squares_heuristic), 5000, [])
# search(make_qc_problem(10,3), ('A_star', empty_squares_heuristic), 5000, [])

# search(make_qc_problem(3,4), ('A_star', empty_squares_heuristic), 5000, [])
# search(make_qc_problem(4,7), ('A_star', empty_squares_heuristic), 5000, [])
# search(make_qc_problem(2,50), ('A_star', empty_squares_heuristic), 5000, [])


