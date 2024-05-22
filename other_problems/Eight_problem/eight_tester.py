import sys
import os

# Since the queue and tree solver modules are in a different directory, we need to add the path to the system path
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, file_path)

from solver.tree          import *
from solver.queue_search  import *

from eight_puzzle  import *

### Declarations of some example initial states

eight_initial_state_0 = [[1,2,3],  ## 2 moves from goal
                         [4,0,5],
                         [7,8,6]] 
        
eight_initial_state_1 = [[2,0,3],   ## 5 moves from goal
                         [1,4,6],
                         [7,5,8]] 

eight_initial_state_2 = [[1,5,0],   ## 10 moves from goal
                         [7,3,2],
                         [8,4,6]] 

eight_initial_state_3 = [[7,1,5],   ## ? moves from goal
                         [3,4,2],
                         [8,0,6]]

eight_puzzle = make_eight_tile_problem(eight_initial_state_3)

search(eight_puzzle, 'breadth_first', 50000, ['loop_check'] )
