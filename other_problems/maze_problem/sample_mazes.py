
import random

rand = random.Random()

def create_random_maze(x, y, wall_density):

    maze = [[0 for _ in range(x)] for _ in range(y)]

    for i in range(y):
        for j in range(x):
            if int(rand.random()*100) < wall_density:
                maze[i][j] = -2

    maze[rand.randint(0, y-1)][rand.randint(0, x-1)] = -1
    maze[rand.randint(0, y-1)][rand.randint(0, x-1)] = -3

    return maze

maze_initial_state_1 = [[-2, -2, -2, -1, -2, -2, -2, -2, -2, -2],
                      [-2,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                      [-2, -2, -2, -2, -2, -2, -2, -2,  0, -2],
                      [-2,  0, -2,  0,  0,  0,  0, -2,  0, -2],
                      [-2,  0, -2,  0, -2, -2,  0, -2,  0, -2],
                      [-2,  0,  0,  0,  0, -2,  0, -2,  0, -2],
                      [-2, -2, -2, -2,  0, -2,  0, -2,  0, -2],
                      [-2,  0,  0,  0,  0, -2,  0,  0,  0, -2],
                      [-2, -3, -2, -2, -2, -2, -2, -2, -2, -2]]

maze_initial_state_2 = [[-2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2],
                        [-2,  0,  0,  0,   0, -2,  0,  0,   0,  0,  0,  0,   0,  0,  0,  0,  -2,  0,  0,  0,   0,  0, -2,  0,   0,  0,  0,  0,   0, -2,  0, -2],
                        [-2,  0, -2,  0,   0, -2, -2, -2,   0,  0,  0,  0,   0,  0,  0,  0,  -2,  0,  0, -2,  -2,  0, -2,  0,  -2, -2, -2,  0,  -2, -2,  0, -2],
                        [-2,  0, -2,  0,   0,  0,  0, -2,   0,  0, -2,  0,   0, -2, -2,  0,   0,  0,  0, -2,   0,  0,  0,  0,  -2,  0, -2,  0,  -2,  0,  0, -2],
                        [-2,  0, -2, -2,  -2, -2,  0, -2,   0,  0, -2, -2,   0, -2, -2,  0,  -2,  0,  0, -2,   0,  0, -2,  0,  -2,  0, -2,  0,   0,  0,  0, -2],
                        [-2,  0,  0,  0,  -3, -2,  0, -2,   0,  0,  0, -2,   0,  0, -2,  0,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2,  0, -2,  0,   0,  0,  0, -2],
                        [-2,  0, -2, -2,  -2, -2,  0, -2,   0,  0,  0, -2,   0, -2, -2,  0,  -2,  0,  0, -2,   0,  0,  0,  0,   0,  0, -2, -2,  -2, -2,  0, -2],
                        [-2,  0, -2,  0,   0,  0,  0, -2,  -2, -2,  0, -2,   0,  0,  0,  0,  -2,  0,  0,  0,   0,  0, -2, -2,   0,  0, -2,  0,   0,  0,  0, -2],
                        [-2,  0, -2,  0,  -2, -2, -2, -2,   0, -2,  0, -2,   0,  0,  0,  0,  -2,  0,  0, -2,   0,  0,  0,  0,   0,  0, -2,  0,   0,  0,  0, -2],
                        [-2, -2, -2,  0,  -2,  0,  0,  0,   0, -2,  0, -2,  -2, -2,  0,  0,  -2,  0,  0, -2,   0, -2, -2, -2,  -2, -2, -2,  0,  -2, -2, -2, -2],
                        [-2,  0,  0,  0,  -2,  0, -2, -2,   0, -2,  0, -2,   0, -2,  0,  0,  -2,  0, -2, -2,   0, -2,  0,  0,   0,  0, -2,  0,   0,  0,  0, -2],
                        [-2,  0, -2, -2,  -2,  0, -2, -2,   0, -2,  0, -2,   0, -2,  0,  0,  -2,  0,  0, -2,   0, -2,  0,  0,   0,  0, -2,  0,   0, -2,  0, -2],
                        [-2,  0,  0,  0,   0,  0, -2, -2,   0, -2,  0, -2,   0, -2, -2,  0,   0,  0,  0, -2,   0,  0,  0, -2,   0,  0, -2, -2,  -2, -2,  0, -2],
                        [-2,  0, -2, -2,  -2,  0, -2, -2,   0, -2,  0, -2,   0,  0, -2,  0,   0,  0,  0, -2,   0,  0,  0, -2,   0,  0, -2,  0,   0,  0,  0, -2],
                        [-2,  0,  0,  0,  -2,  0, -2, -2,   0,  0,  0, -2,   0,  0, -2,  0,   0,  0, -2, -2,  -2, -2, -2, -2,   0,  0, -2,  0,   0,  0,  0, -2],
                        [-2, -2,  0, -2,  -2, -2, -2, -2,   0,  0,  0, -2,   0,  0,  0,  0,   0,  0, -2,  0,   0, -2, -2,  0,   0,  0, -2, -2,   0, -2,  0, -2],
                        [-2,  0,  0, -2,   0,  0, -2,  0,   0,  0,  0, -2,   0,  0,  0,  0,  -2, -2, -2,  0,   0,  0,  0,  0,   0,  0, -2, -2,   0, -2, -2, -2],
                        [-2,  0,  0, -2,   0,  0,  0,  0,   0, -2, -2, -2,   0, -2,  0,  0,  -2,  0,  0,  0,   0,  0,  0,  0,   0, -2, -2,  0,   0, -2, -1, -2],
                        [-2,  0,  0, -2,   0,  0,  0,  0,   0, -2,  0, -2,   0, -2,  0,  0,  -2,  0,  0,  0,  -2,  0, -2, -2,  -2, -2,  0,  0,   0, -2,  0, -2],
                        [-2,  0,  0, -2,   0,  0, -2, -2,  -2, -2,  0, -2,  -2, -2,  0, -2,  -2,  0,  0, -2,  -2,  0, -2,  0,   0,  0,  0,  0,   0, -2,  0, -2],
                        [-2,  0, -2, -2,   0,  0, -2,  0,   0,  0,  0, -2,   0,  0,  0,  0,  -2,  0,  0, -2,   0,  0, -2,  0,   0, -2,  0, -2,  -2, -2,  0, -2],
                        [-2,  0,  0,  0,   0,  0,  0,  0,  -2,  0,  0, -2,   0, -2, -2,  0,  -2,  0, -2, -2,  -2, -2, -2,  0,  -2, -2,  0,  0,   0, -2,  0, -2],
                        [-2,  0,  0, -2,   0,  0,  0,  0,  -2,  0,  0, -2,   0,  0,  0,  0,  -2,  0,  0,  0,   0,  0,  0,  0,  -2, -2, -2,  0,   0,  0,  0, -2],
                        [-2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2,  -2, -2, -2, -2],]

maze_initial_state_3 = [[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                        [-2,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0, -2,  0, -2, -2,  0, -2,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0, -2,  0, -2],
                        [-2,  0, -2, -2,  0, -2, -2, -2,  0, -2,  0,  0,  0,  0,  0,  0, -2, -2,  0, -2, -2,  0, -2,  0, -2, -2, -2,  0, -2, -2,  0, -2],
                        [-2,  0, -2,  0,  0,  0,  0, -2,  0, -2, -2, -2,  0, -2, -2,  0,  0,  0,  0, -2, -2,  0,  0,  0, -2,  0, -2,  0, -2,  0,  0, -2],
                        [-2,  0, -2, -2, -2, -2,  0, -2,  0,  0, -2, -2,  0, -2, -2,  0, -2, -2,  0, -2,  0,  0, -2,  0, -2,  0, -2,  0, -2,  0, -2, -2],
                        [-2,  0,  0,  0, -3, -2,  0, -2, -2,  0, -2, -2,  0,  0, -2,  0, -2, -2, -2, -2, -2, -2, -2, -2, -2,  0, -2,  0,  0,  0,  0, -2],
                        [-2,  0, -2, -2, -2, -2,  0, -2,  0,  0,  0, -2,  0, -2, -2,  0, -2,  0,  0, -2,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2,  0, -2],
                        [-2,  0, -2,  0,  0,  0,  0, -2, -2, -2,  0, -2,  0, -2, -2,  0, -2, -2,  0,  0,  0, -2, -2, -2, -2,  0, -2,  0, -2, -2,  0, -2],
                        [-2,  0, -2,  0, -2, -2, -2, -2,  0, -2,  0, -2,  0,  0,  0,  0, -2, -2,  0, -2,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0, -2],
                        [-2, -2, -2,  0, -2,  0,  0,  0,  0, -2,  0, -2, -2, -2,  0, -2, -2,  0,  0, -2,  0, -2, -2, -2, -2, -2, -2,  0, -2, -2, -2, -2],
                        [-2,  0,  0,  0, -2,  0, -2, -2,  0, -2,  0, -2,  0, -2,  0, -2, -2,  0, -2, -2,  0, -2, -2,  0, -2,  0, -2,  0,  0,  0,  0, -2],
                        [-2,  0, -2, -2, -2,  0, -2, -2,  0, -2,  0, -2,  0, -2,  0,  0, -2,  0,  0, -2,  0, -2,  0,  0,  0,  0, -2, -2,  0, -2,  0, -2],
                        [-2,  0,  0,  0,  0,  0, -2, -2,  0, -2,  0, -2,  0, -2, -2,  0, -2, -2,  0, -2,  0, -2,  0, -2,  0, -2, -2, -2, -2, -2,  0, -2],
                        [-2,  0, -2, -2, -2,  0, -2, -2,  0, -2,  0, -2,  0,  0, -2,  0,  0,  0,  0, -2,  0,  0,  0, -2,  0,  0, -2,  0, -2, -2,  0, -2],
                        [-2,  0,  0,  0, -2,  0, -2, -2,  0,  0,  0, -2, -2,  0, -2,  0, -2,  0, -2, -2, -2, -2, -2, -2, -2,  0, -2,  0,  0,  0,  0, -2],
                        [-2, -2,  0, -2, -2, -2, -2, -2,  0, -2,  0, -2,  0,  0,  0,  0, -2,  0, -2,  0, -2, -2, -2,  0,  0,  0, -2, -2,  0, -2,  0, -2],
                        [-2, -2,  0, -2,  0,  0, -2,  0,  0, -2,  0, -2,  0, -2,  0, -2, -2, -2, -2,  0, -2, -2, -2,  0, -2, -2, -2, -2,  0, -2, -2, -2],
                        [-2, -2,  0, -2,  0, -2, -2, -2,  0, -2, -2, -2,  0, -2,  0, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2,  0, -2, -1, -2],
                        [-2, -2,  0, -2,  0,  0,  0,  0,  0, -2,  0, -2,  0, -2,  0,  0, -2, -2,  0, -2, -2,  0, -2, -2, -2, -2, -2, -2,  0, -2,  0, -2],
                        [-2,  0,  0, -2, -2,  0, -2, -2, -2, -2,  0, -2, -2, -2,  0, -2, -2, -2,  0, -2, -2,  0, -2, -2,  0,  0,  0,  0,  0, -2,  0, -2],
                        [-2,  0, -2, -2,  0,  0, -2,  0,  0,  0,  0, -2,  0,  0,  0,  0, -2,  0,  0, -2,  0,  0, -2,  0,  0, -2,  0, -2, -2, -2,  0, -2],
                        [-2,  0,  0,  0,  0, -2, -2,  0, -2,  0, -2, -2,  0, -2, -2,  0, -2,  0, -2, -2, -2, -2, -2,  0, -2, -2,  0,  0, -2, -2,  0, -2],
                        [-2, -2,  0, -2,  0,  0,  0,  0, -2,  0, -2, -2,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0, -2],
                        [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],]

maze_initial_state_empty = [[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                            [-2, -3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                            [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -2],
                            [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],]

maze_initial_state_4 = [[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                        [-2, -3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                        [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2,  0,  0,  0,  0, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1, -2],
                        [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],]

yora_maze_1 = [[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
               [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0, -3,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2],

               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2],

               [-2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2],

               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0, -1,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0, -2],

               [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],]

yora_maze_2 = [[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
               [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],

               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

               [-2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2, -2, -2, -2,  0,  0, -3,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],

               [-2,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],
               [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2, -2, -2,  0,  0,  0,  0,  0, -2],

               [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],]

yora_maze_empty = [[-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                   [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0, -3,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],
                   [-2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -2],

                   [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],]
