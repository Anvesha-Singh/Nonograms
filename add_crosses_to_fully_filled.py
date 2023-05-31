def is_row_fully_filled(row: list[str], this_clue: list[str]):
    return sum(int(elem) for elem in this_clue) == row.count(FILLED)

def add_crosses_to_full_rows(nonogram_grid: list[list[str]], all_row_clues: list[str]) -> list[list[str]] :
    for row_number, row_clue in enumerate(all_row_clues):
        list_row_clue = row_clue.split()
        if is_row_fully_filled(nonogram_grid[row_number], list_row_clue):
            row = "".join(nonogram_grid[row_number])
            row = row.replace(EMPTY, CROSS)
            nonogram_grid[row_number] = [elem for elem in row]
    return nonogram_grid
