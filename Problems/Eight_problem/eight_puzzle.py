## eight_puzzle.py
## by Brandon Bennett
## University of Leeds

## Specification of 8-Puzzle search problem
## designed for use with queue_search.py

print( "Loading eight_puzzle.py" )


## "deepcopy" is used to make a copy of a state and then change
## it to create a new state.
## This is needed because of the way Python handles lists.
## If you just assign a list to a new variable then you will
## just get a new pointer to the same list.


from copy import deepcopy


### Print out problem info
def eight_problem_info():
        print( "The sliding tile 8 puzzle" )


### Declarations of some example states

eight_state_0 = [ [1,2,3],  ## 2 moves from goal
                  [4,0,5],
                  [7,8,6] ] 
        
eight_state_1 = [ [2,0,3],   ## 5 moves from goal
                  [1,4,6],
                  [7,5,8] ] 

eight_state_2 = [ [1,5,0],   ## 10 moves from goal
                  [7,3,2],
                  [8,4,6]
                ] 

eight_state_3 = [ [7,1,5],   ## ? moves from goal
                  [3,4,2],
                  [8,0,6]
                ] 

eight_initial_state = eight_state_3

## Specify the goal state:
eight_goal_state = [ [1,2,3],
                     [4,5,6],
                     [7,8,0]
                   ] 


### For the successsor state function I just check which position on
### the board the zero is at and return the appropriate sequence of
### possible actions.

def eight_possible_actions( state ):
       if state[0][0] == 0:
          return ['up','left']
       if state[0][1] == 0:
          return ['up','left','right']
       if state[0][2] == 0:
          return ['up','right']
       if state[1][0] == 0:
          return ['up','down','left']
       if state[1][1] == 0:
          return ['up','down','left','right']
       if state[1][2] == 0:
          return ['up','down','right']
       if state[2][0] == 0:
          return ['down','left']
       if state[2][1] == 0:
          return ['down','left','right']
       if state[2][2] == 0:
          return ['down','right']


## The successor state function finds the position of
## the zero (ie the space) and swaps it with a neighbouring tile
## in accordance with the action.
## Note that the original state is first copied using the
## deepcopy function and then this copy is modified and returned.

def eight_successor_state( action, state ):
        newstate = deepcopy(state)
        row = tile_position(0,state)[0]
        col = tile_position(0,state)[1]
        if action == 'up':
             newstate[row][col] = newstate[row+1][col]
             newstate[row+1][col] = 0
        if action == 'down':
             newstate[row][col] = newstate[row-1][col]
             newstate[row-1][col] = 0
        if action == 'left':
             newstate[row][col] = newstate[row][col+1]
             newstate[row][col+1] = 0
        if action == 'right':
             newstate[row][col] = newstate[row][col-1]
             newstate[row][col-1] = 0
        return newstate

def tile_position( N, state ):
       for i in range(3):
           for j in range(3):
             if state[i][j] == N:
                   return (i,j)

def eight_test_goal_state( state ):
       global eight_goal_state
       return eight_equivalent_states( state, eight_goal_state )


### The equivalent states function should compare each corresponding
### position in the two states.
### Just checking for equality will not work as the states will be
### Two different structures, but containing the same elements.

def eight_equivalent_states(  s1, s2 ):
       ##print "eight_equivalent_states", s1, s2
       for i in range(3):
           for j in range(3):
             if not(s1[i][j] == s2[i][j]):
                return False
       return True


## HEURISTICS

def eight_misplaced_tiles_heuristic( state ):
        return eight_num_diff_tiles_between_states( state, eight_goal_state )

def eight_num_diff_tiles_between_states(  s1, s2 ):
       dist = 0
       for i in range(3):
           for j in range(3):
             if ((not s1[i][j]==0) and (not(s1[i][j] == s2[i][j])) ):
                dist += 1
       return dist


def eight_manhatten_heuristic( state ):
        #h = eight_manhatten_dist_between_states( state, eight_goal_state )
        #print( "Manhatten heuristic:", h )
        #return h
        return eight_manhatten_dist_between_states( state, eight_goal_state )

def eight_manhatten_dist_between_states( s1, s2 ):
       dist = 0
       for i in range(1,9):
           dist += eight_manhatten_dist_of_tile_between_states( i, s1, s2 )
       return dist

def eight_manhatten_dist_of_tile_between_states( i, s1, s2 ):
       (x1, y1) = tile_position( i, s1 )
       (x2, y2) = tile_position( i, s2 )
       return (abs(x1-x2) + abs(y1-y2))




#### Eight Puzzle problem specification
eight_puzzle = ( None,
             eight_problem_info,
             eight_initial_state,
             eight_possible_actions,
             eight_successor_state,
             eight_test_goal_state
           )



