def fill_for_bigger_than_half(nonogram_grid: list[list[str]], all_row_clues: list[str]) -> list[list[str]] :
    grid_size = len(nonogram_grid)
    for row_number, row_clue in enumerate(all_row_clues):
        list_row_clue = row_clue.split()
        if len(list_row_clue) ==  1 and int(list_row_clue[0]) > grid_size // 2:
            for central in range(grid_size - int(list_row_clue[0]), int(list_row_clue[0])):
                nonogram_grid[row_number][central] = FILLED
    return nonogram_grid
