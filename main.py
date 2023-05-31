CROSS = "x"
EMPTY = " "
FILLED = "■"
def solve_nonogram(all_clues: list[list[str]]) -> list[list[str]]:
        nonogram_grid = empty_grid(len(all_clues[0]))
        
        nonogram_grid = fill_for_complete_rows(nonogram_grid, all_clues[0])      
        transpose =  make_list_of_lists(list(zip(*nonogram_grid)))
        transpose = fill_for_complete_rows(transpose, all_clues[1])        
        nonogram_grid = make_list_of_lists(list(zip(*transpose)))


        nonogram_grid = fill_complete_with_crosses(nonogram_grid, all_clues[0])
        transpose =  make_list_of_lists(list(zip(*nonogram_grid)))
        transpose = fill_complete_with_crosses(transpose, all_clues[1])
        nonogram_grid = make_list_of_lists(list(zip(*transpose)))

        #nonogram_grid = fill_for_bigger_than_half(nonogram_grid, all_clues[0])
        #transpose =  make_list_of_lists(list(zip(*nonogram_grid)))
        #transpose = fill_for_bigger_than_half(nonogram_grid, all_clues[1])
        #nonogram_grid = make_list_of_lists(list(zip(*transpose)))
        return nonogram_grid	
