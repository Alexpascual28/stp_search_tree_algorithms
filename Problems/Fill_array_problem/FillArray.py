## Lab Ex 1 John Stell jan 2018

## "deepcopy" is used to make a copy of a state and then change
## it to create a new state.
## This is needed because of the way Python handles lists.
## If you just assign a list to a new variable then you will
## just get a new pointer to the same list.

from copy import deepcopy

## Make the function to print out problem info
## This has to return a function with no parameters as the search procedure
## requires this

def make_fill_problem_info(array_size):
        def fill_problem_info():
                print( "The Fill Problem -- 2D version\n",
                       "Array Size: ",array_size)
        return fill_problem_info

## Description of state
## The state is a 2D array of with same number of rows and cols
## and where every entry is 1 or 0
## For example:   [[0,0,0],[0,0,1],[1,0,0]]
## That's an array with 3 rows and 3 cols
        
## Specify the initial state:
def fill_initial_state(array_size):
        return [[0 for i in range(array_size)] for i in range(array_size)]

##  Define the possible actions
##  Actions are to change a 0 in the list to a 1 in a particular position
##  One way to represent a position is as a tuple e.g. (2,4) another is a list like[2,4].
##  In any case the collection of possible actions is a list.

def fill_possible_actions(state):
    ans = []
    for i in range(len(state)):                # For each row
            for j in range(len(state[0])):     # For each column
                    if state[i][j] == 0:       # if the entry in ith row and jth col is zero, then:
                            ans.append((i,j))  # add the tuple (i,j) to the answer
    return ans                                 # At end return the answer, which will be a list of tuples

## The successor state function changes a 0 to a 1 in the specified position

def fill_successor_state( action, state ):
        row = action[0]
        col = action[1]                       # Find the row and column that the action refers to
        newstate = deepcopy(state)
        newstate[row][col] = 1                # Change the state in that position only to a 1
        return newstate

## test for goal: no 0s are left
def fill_test_goal_state( state ):
       return fill_possible_actions(state) == []

## problem specification
def make_fill_problem(array_size):
        return ( None,
                 make_fill_problem_info(array_size),
                 fill_initial_state(array_size),
                 fill_possible_actions,
                 fill_successor_state,
                 fill_test_goal_state
                 )



