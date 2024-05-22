
import sys
from tree          import *
from queue_search  import *
from FillArray  import *

problem = make_fill_array_problem(10)

search(problem, 'depth_first', 100000, ['loop_check'])
