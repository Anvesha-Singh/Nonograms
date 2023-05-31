def is_line_complete(this_line: list[str], grid_size: int) -> bool:
	no_of_filled_blocks_in_line = len(this_line)
	minimum_spaces_between_filled_blocks = no_of_filled_blocks_in_line - 1
	return grid_size == minimum_spaces_between_filled_blocks + sum(int(filled_element) for filled_element in this_line)
