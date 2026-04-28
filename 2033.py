from typing import List
def minOperations(self, grid: List[List[int]], x: int) -> int:
    values = []
    for row in grid:
        for val in row:
            values.append(val)

    remainder = values[0] % x
    for val in values:
        if val % x != remainder:
            return -1

    values.sort()
    n = len(values)
    median = values[n // 2]
    
    operations = 0
    for val in values:
        operations += abs(val - median) // x
    
    return operations