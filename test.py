import other_problems.maze_problem.sample_mazes as sample_mazes

def get_surrounding_squares(position):
    x, y = position

    for x, y in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
        if x >= 0 and y >= 0:
            yield x, y

surrounding_squares = get_surrounding_squares((3, 5))

x = len(sample_mazes.maze_initial_state_1[0])
y = len(sample_mazes.maze_initial_state_1)

print(sample_mazes.maze_initial_state_1[y-1][x-1])
print(list(surrounding_squares))