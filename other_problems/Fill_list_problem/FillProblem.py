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

def make_fill_problem_info(list_size):
        def fill_problem_info():
                print( "The List Fill Problem\n",
                       "List Size: ",list_size)
        return fill_problem_info

## Description of state
## The state is an array of length list_size every entry is 1 or 0
        
## Specify the initial state:
def fill_initial_state(list_size):
        return [0 for i in range(list_size)] 

##  Define the possible actions
##  Actions are to change a 0 in the list to a 1 in a particular position

def fill_possible_actions(state):
    ans = []
    for i in range(len(state)):
        if state[i] == 0:
            ans.append(i)
    return ans

## The successor state function changes a 0 to a 1 in the specified position

def fill_successor_state( action, state ):
        newstate = deepcopy(state)
        newstate[action] = 1
        return newstate

## test for goal: no 0s are left
def fill_test_goal_state( state ):
       return fill_possible_actions(state) == []

## problem specification
def make_fill_problem(list_size):
        return ( None,
                 make_fill_problem_info(list_size),
                 fill_initial_state(list_size),
                 fill_possible_actions,
                 fill_successor_state,
                 fill_test_goal_state
                 )



