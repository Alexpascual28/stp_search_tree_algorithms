import sys
import os

# Since the queue and tree solver modules are in a different directory, we need to add the path to the system path
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, file_path)

from solver.tree          import *
from solver.queue_search  import *

from maze_problem import *
from sample_mazes import *

def blind_informed_search(actual_maze, initial_known_maze, strategy=('A_star', distance_to_end_heuristic, avoid_turns_cost_function), scan_diagonals=False, print_goal_states=False, margins=0):
    # Check if the actual and initial mazes are the same size
    if are_mazes_equal_size(actual_maze, initial_known_maze) == False:
        raise Exception("Actual and initial mazes are different sizes. The initial unknown maze should be the same size as the actual maze.")
    
    print("Starting blind informed search...")
    print("\nThe actual maze is:")
    print_maze(actual_maze)
    print("\nThe initial known maze is:")
    print_maze(initial_known_maze)

    # Add margins to the actual maze
    actual_maze_with_margins = add_obstacle_margins(deepcopy(actual_maze), margins)

    # Current known maze (with added margins)
    known_maze = add_obstacle_margins(deepcopy(initial_known_maze), margins)

    # Draw the start and end points in the "final" known maze
    final_known_maze = deepcopy(actual_maze)
    start_position = find_position_by_value(known_maze, -1)
    goal_position = find_position_by_value(known_maze, -3)
    final_known_maze[start_position[0]][start_position[1]] = -1
    final_known_maze[goal_position[0]][goal_position[1]] = -3

    is_goal_reached = False
    move_number = 0

    while(is_goal_reached == False):
        # Find the path to the goal
        path = search(create_maze_problem(known_maze, scan_diagonals, print_goal_states), strategy, 500000, [])

        # Follow the path to the goal and re-assign the known maze
        is_goal_reached, visited_path, known_maze = follow_path(actual_maze_with_margins, known_maze, path)

        # Draw path in the final known maze
        final_known_maze, move_number = draw_path(final_known_maze, visited_path, move_number)

    # Print the final known maze
    print("Goal reached! The final known maze is:")
    print_maze(final_known_maze)
    
def are_mazes_equal_size(actual_maze, initial_known_maze):
    if len(actual_maze) != len(initial_known_maze):
        return False
    for i in range(len(actual_maze)):
        if len(actual_maze[i]) != len(initial_known_maze[i]):
            return False
    return True

def follow_path(actual_maze, known_maze, path):
    is_goal_reached = False
    visited_path = []
    start_position = find_position_by_value(known_maze, -1)
    delete_start_point(known_maze)

    for i in range(len(path)):
        if actual_maze[path[i][0]][path[i][1]] == -2:
            known_maze[path[i][0]][path[i][1]] = -2
            if i == 0:
                known_maze[start_position[0]][start_position[1]] = -1
            else:
                known_maze[path[i-1][0]][path[i-1][1]] = -1
            break
        if known_maze[path[i][0]][path[i][1]] == -3:
            is_goal_reached = True
            break
        visited_path.append(path[i])
    return is_goal_reached, visited_path, known_maze

def delete_start_point(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == -1:
                maze[i][j] = 0
                return maze

def draw_path(maze, path, last_move_number):
    move_number = last_move_number
    for i in range(len(path)):
        move_number = last_move_number + i + 1
        maze[path[i][0]][path[i][1]] = move_number
    return maze, move_number

def find_position_by_value(maze, value):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == value:
                return i, j
            
def print_maze(maze):
    for row in maze:
        for square in row:
            if square == -2:
                print("%4s" % "████", end='')
            elif square == -1:
                print("%4s" % "[S]", end='')
            elif square == -3:
                print("%4s" % "[G]", end='')
            else:
                print("%4i" % square, end='')
        print()

def add_obstacle_margins(maze, margin):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == -2:
                for k in range(-margin, margin+1):
                    for l in range(-margin, margin+1):
                        if i+k >= 0 and i+k < len(maze) and j+l >= 0 and j+l < len(maze[i]):
                            if maze[i+k][j+l] == 0:
                                maze[i+k][j+l] = -4
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == -4:
                maze[i][j] = -2
    return maze

# print_maze(add_obstacle_margins(yora_maze_1, 1))

blind_informed_search(yora_maze_1, yora_maze_empty, strategy=('A_star', distance_to_end_heuristic, avoid_turns_cost_function), print_goal_states=True, margins=2)
# blind_informed_search(maze_initial_state_2, maze_initial_state_empty)
