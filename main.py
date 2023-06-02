CROSS = "x"
EMPTY = " "
FILLED = "■"

def make_list_of_lists(list_of_tup) -> list[list[str]]:
    return [list(tup) for tup in list_of_tup]

def apply_on_nonogram_grid_and_transpose(nonogram_grid: list[list[str]], all_clues:list[list[str]], function) -> list[list[str]]:
    nonogram_grid = function(nonogram_grid, all_clues[0])      
    transpose =  make_list_of_lists(list(zip(*nonogram_grid)))
    transpose = function(transpose, all_clues[1])        
    nonogram_grid = make_list_of_lists(list(zip(*transpose)))
    return nonogram_grid

def solve_nonogram(all_clues: list[list[str]]) -> list[list[str]]:
    nonogram_grid = empty_grid(len(all_clues[0]))       
    nonogram_grid = apply_on_nonogram_grid_and_transpose(nonogram_grid, all_clues, fill_for_complete_rows)           
    nonogram_grid = apply_on_nonogram_grid_and_transpose(nonogram_grid, all_clues, add_crosses_to_full_rows)        
    nonogram_grid = apply_on_nonogram_grid_and_transpose(nonogram_grid, all_clues, fill_complete_with_crosses) 
    nonogram_grid = apply_on_nonogram_grid_and_transpose(nonogram_grid, all_clues, fill_for_bigger_than_half)
    nonogram_grid = apply_on_nonogram_grid_and_transpose(nonogram_grid, all_clues, add_crosses_to_full_rows)
    nonogram_grid = fill_blanks(nonogram_grid, all_clues) 
    return nonogram_grid
