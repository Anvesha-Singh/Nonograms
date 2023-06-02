def compare_row_with_clue(row: list[str], list_row_clue):
    row_string = "".join(row).replace(CROSS," ").replace(EMPTY," ")
    row = row_string.split()
    filled_row_numbers = [str(len(elem)) for elem in row]
    return all(int(x) <= int(y) for x, y in zip(filled_row_numbers, list_row_clue))

def element_is_right(nonogram_grid: list[list[str]], all_clues: list[list[str]]):
    ans = True
    for row_number in range(len(nonogram_grid)):
        ans = ans and compare_row_with_clue(nonogram_grid[row_number], all_clues[0][row_number].split())
    transpose =  make_list_of_lists(list(zip(*nonogram_grid)))
    for row_number in range(len(nonogram_grid)):
        ans = ans and compare_row_with_clue(transpose[row_number], all_clues[1][row_number].split())
    nonogram_grid = make_list_of_lists(list(zip(*transpose)))
    return ans

def fill_blanks(nonogram_grid: list[list[str]], all_clues: list[list[str]]) -> list[list[str]] :
    for row_number in range(len(nonogram_grid)):
        for elem in range(len(nonogram_grid)):
            if nonogram_grid[row_number][elem] == EMPTY:
                nonogram_grid[row_number][elem] = FILLED
                if element_is_right(nonogram_grid, all_clues):
                    nonogram_grid[row_number][elem] = FILLED
                else:
                    nonogram_grid[row_number][elem] = CROSS
    return nonogram_grid
