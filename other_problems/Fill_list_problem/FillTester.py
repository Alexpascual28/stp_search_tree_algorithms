
import sys
import os

# Since the queue and tree solver modules are in a different directory, we need to add the path to the system path
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, file_path)

from solver.tree          import *
from solver.queue_search  import *

from FillProblem  import *

problem = make_fill_problem(4)

search(problem, 'breadth_first', 2000, [])
