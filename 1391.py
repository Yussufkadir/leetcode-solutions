from typing import List
def hasValidPath(self, grid: List[List[int]]) -> bool:
    m, n = len(grid), len(grid[0])

    streets = {
        1: {'L', 'R'},
        2: {'U', 'D'},
        3: {'L', 'D'},
        4: {'R', 'D'},
        5: {'L', 'U'},
        6: {'R', 'U'}
    }

    opposite = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    
    visited = [[False] * n for _ in range(m)]
    
    stack = [(0, 0)]
    visited[0][0] = True
    
    while stack:
        r, c = stack.pop()

        if r == m - 1 and c == n - 1:
            return True

        curr_type = grid[r][c]

        for dir_char in streets[curr_type]:
            dr, dc = directions[dir_char]
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                neighbor_type = grid[nr][nc]
                if opposite[dir_char] in streets[neighbor_type]:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
    
    return False        