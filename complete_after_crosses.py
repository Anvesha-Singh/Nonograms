def is_complete_with_crosses(this_clue: list[str], row: list[str]) -> bool:
    crosses = ''.join(row).count(CROSS)
    return len(row) == crosses + sum(int(filled_element) for filled_element in this_clue)

def fill_complete_with_crosses(nonogram_grid: list[list[str]], all_row_clues: list[str]) -> list[list[str]] :
    for row_number, row_clue in enumerate(all_row_clues):
        list_row_clue = row_clue.split()
        if is_complete_with_crosses(list_row_clue, nonogram_grid[row_number]):
            row = []
            for elem in nonogram_grid[row_number]:
                if elem == EMPTY:
                    row.append(FILLED)
                else:
                    row.append(elem)
            nonogram_grid[row_number] = row
    return nonogram_grid
