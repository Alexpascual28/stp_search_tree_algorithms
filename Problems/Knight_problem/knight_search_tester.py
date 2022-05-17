## knight_search_tester.py
## Modified by John Stell 2018 from original by Brandon Bennett --- 27/10/2009

## This is the top level file for running search on the knight's tour


import sys
from tree          import *
from queue_search  import *

from knights_tour  import *


# Use this if you want to make Python wait between search tests.
# For Python 3 replace raw_input by input
# defwait():
#      raw_input('<Press enter to continue>')


search(get_knights_tour_problem(3,4), 'depth_first',   500000, [] )
search(get_knights_tour_problem(5,5), 'depth_first',   500000, ['loop_check'] )



