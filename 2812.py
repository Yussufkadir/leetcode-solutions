from collections import deque
from typing import List

def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
    n = len(grid)
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    dist = [[float('inf')] * n for _ in range(n)]
    q = deque()
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))
    
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    
    def can_reach(min_dist: int) -> bool:
        if dist[0][0] < min_dist or dist[n-1][n-1] < min_dist:
            return False
        
        visited = [[False] * n for _ in range(n)]
        q = deque([(0, 0)])
        visited[0][0] = True
        
        while q:
            r, c = q.popleft()
            if r == n-1 and c == n-1:
                return True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    if dist[nr][nc] >= min_dist:
                        visited[nr][nc] = True
                        q.append((nr, nc))
        
        return False
    
    left, right = 0, 2 * n
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_reach(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result        