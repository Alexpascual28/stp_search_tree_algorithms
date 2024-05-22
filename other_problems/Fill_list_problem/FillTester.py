
import sys
from tree          import *
from queue_search  import *
from FillProblem  import *

problem = make_fill_problem(4)

search(problem, 'breadth_first', 2000, [])
