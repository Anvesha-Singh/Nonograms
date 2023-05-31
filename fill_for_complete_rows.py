FILLED = "X"
EMPTY = "_"

def is_line_complete(this_line: list[str], grid_size: int) -> bool:
	no_of_filled_blocks_in_line = len(this_line)
	minimum_spaces_between_filled_blocks = no_of_filled_blocks_in_line - 1
	return grid_size == minimum_spaces_between_filled_blocks + sum(int(filled_element) for filled_element in this_line)

def fill_for_complete_rows(nonogram_grid: list[list[str]], all_row_clues: list[str]) -> list[list[str]] :
    for row_number, row_clue in enumerate(all_row_clues):
        list_row_clue = row_clue.split()
        filled_row = []
        if is_line_complete(list_row_clue, len(nonogram_grid)):
            for clue in list_row_clue:
                fill_row = [FILLED] * int(clue)
                fill_row.append(EMPTY)
                filled_row.extend(fill_row)
            nonogram_grid[row_number] = filled_row[:-1]
    return nonogram_grid
