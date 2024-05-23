def get_surrounding_squares(position):
    x, y = position

    for x, y in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
        if x >= 0 and y >= 0:
            yield x, y

surrounding_squares = get_surrounding_squares((3, 5))

print(list(surrounding_squares))