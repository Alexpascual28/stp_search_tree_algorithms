## Definition of Knight's Tour search problem
## by Brandon Bennett
## University of Leeds

from __future__ import print_function

from copy import deepcopy

# Representation of a state:
# (move_number, (current_x_pos, current_y_pos),  full_board_state)
# So on a small 3x3 board after 3 moves we might have a state such as:
#
# ( 3, (2,0), [[1,0,0],
#              [0,0,2],
#              [3,0,0]] )


def knight_get_initial_state(x,y):
      return ( 0, 0, matrix_of_zeros(y,x) )

def matrix_of_zeros(X,Y):
    return [ [0 for x in range(X)] for y in range(Y)] # Pythonic or what?


def knight_possible_actions( state ):
             if state[0] == 0:
                return knight_initial_moves()
             return knight_following_moves(state)

def knight_initial_moves():
           moves = []
           for i in range(BOARD_X):
               for j in range(BOARD_Y):
                   moves = moves + [[i,j]]
           return moves

def square_is_empty(i,j, state):
      if state[2][i][j] == 0:
         return True
      return False

knights_moves = ( (1,2),  (2,1),  (-1,2),  (2,-1),
                  (1,-2), (2,-1), (-1,-2),  (-2,-1) )

def knight_following_moves( state ):
      kx = state[1][0]
      ky = state[1][1]
      moves = []
      for move in knights_moves:
           newx = kx + move[0]    ## target x coord
           newy = ky + move[1]    ## target y coord

           ## If target square is on board and empty
           ## add it to the list of moves 
           if newx in range(BOARD_X) and newy in range(BOARD_Y):
              if state[2][newx][newy] == 0:
                 moves = moves + [move]
      return moves

def knight_successor_state( action, state ):
    if state[0] == 0:
       newstate =  knight_initial_successor( action )
       return newstate
    board = deepcopy(state[2])
    xpos = state[1][0] + action[0]
    ypos = state[1][1] + action[1]
    movenum = state[0] + 1
    board[xpos][ypos] = movenum
    return (movenum, (xpos,ypos), board)       


def knight_initial_successor( action ):
    board = deepcopy(knight_initial_state[2])
    board[action[0]][action[1]] = 1
    return( 1, action, board )


def knight_goal_state( state ):
       if state[0] == BOARD_X * BOARD_Y:
          print( "\nGOAL STATE:" )
          print_board_state( state )
          return True
       return False


def print_board_state( state ):
      board = state[2]
      for row in board:
           for square in row:
               print( " %2i" % square, end = '' )
           print()



def knight_print_problem_info():
    print( "The Knight's Tour (", BOARD_X, "x", BOARD_Y, "board)" )

## Return a problem spec tuple for a given board size
def get_knights_tour_problem(x, y):
      global BOARD_X, BOARD_Y, knight_initial_state
      BOARD_X = x
      BOARD_Y = y
      knight_initial_state = knight_get_initial_state(x,y)
      return  ( None,
                knight_print_problem_info,
                knight_initial_state,
                knight_possible_actions,
                knight_successor_state,
                knight_goal_state
              )
                
                                                

