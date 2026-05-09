from typing import List
def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    
    def extract(layer):
        elements = []
        top, bottom = layer, m - 1 - layer
        left, right = layer, n - 1 - layer

        for col in range(left, right + 1):
            elements.append(grid[top][col])
        for row in range(top + 1, bottom + 1):
            elements.append(grid[row][right])
        for col in range(right - 1, left - 1, -1):
            elements.append(grid[bottom][col])
        for row in range(bottom - 1, top, -1):
            elements.append(grid[row][left])
        
        return elements
    
    def place_back(layer, elements):
        top, bottom = layer, m - 1 - layer
        left, right = layer, n - 1 - layer
        idx = 0

        for col in range(left, right + 1):
            grid[top][col] = elements[idx]; idx += 1
        for row in range(top + 1, bottom + 1):
            grid[row][right] = elements[idx]; idx += 1
        for col in range(right - 1, left - 1, -1):
            grid[bottom][col] = elements[idx]; idx += 1
        for row in range(bottom - 1, top, -1):
            grid[row][left] = elements[idx]; idx += 1
    
    num_layers = min(m, n) // 2
    
    for layer in range(num_layers):
        elements = extract(layer)
        rotate_by = k % len(elements)     
        rotated = elements[rotate_by:] + elements[:rotate_by]
        place_back(layer, rotated)
    
    return grid