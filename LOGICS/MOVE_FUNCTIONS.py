from LOGICS.COMPRESS_FUNCTION import compress
from LOGICS.MERGE_FUNCTION import merge
from LOGICS.REVERSE_FUNCTION import reverse
from LOGICS.TRANSPOSE_FUNCTION import transpose


def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid, changed1 = compress(transposed_grid)
    new_grid, changed2 = merge(new_grid)
    new_grid, temp = compress(new_grid)
    final_grid = transpose(new_grid)
    changed = changed1 or changed2
    return final_grid, changed


def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    new_grid, temp = compress(new_grid)
    changed = changed1 or changed2
    final_reverse = reverse(new_grid)
    final_grid = transpose(final_reverse)
    return final_grid, changed


def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    new_grid, temp = compress(new_grid)
    changed = changed1 or changed2
    final_grid = reverse(new_grid)
    return final_grid, changed


def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, temp = compress(new_grid)
    return new_grid, changed
