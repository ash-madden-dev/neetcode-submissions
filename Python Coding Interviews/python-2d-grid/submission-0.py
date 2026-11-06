from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    if r >= len(grid):
        return False
    elif c >= len(grid[r]):
        return False
    else:
        return True
        


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0)) # True (1)
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2)) # True (9)
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1)) # True (5)
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3)) # False
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))
