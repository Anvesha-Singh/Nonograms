EMPTY = "o"
FILLED = "x"
def empty_grid(grid_size: int) -> list[list[str]]:
    empty_grid = []
    for row in range(grid_size):
        empty_grid.append([EMPTY] * grid_size)
    return empty_grid
