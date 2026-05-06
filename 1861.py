from typing import List
def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
    m, n = len(boxGrid), len(boxGrid[0])

    rotated = [['.'] * m for _ in range(n)]
    for r in range(m):
        for c in range(n):
            rotated[c][m-1-r] = boxGrid[r][c]

    for c in range(m):  
        bottom = n - 1  
        for r in range(n-1, -1, -1): 
            if rotated[r][c] == '*':
                bottom = r - 1  
            elif rotated[r][c] == '#':
                rotated[r][c] = '.'
                rotated[bottom][c] = '#'
                bottom -= 1
    
    return rotated     