from typing import List
from collections import deque
def canReach(self, arr: List[int], start: int) -> bool:
    n = len(arr)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    
    while queue:
        i = queue.popleft()

        if arr[i] == 0:
            return True
        
        for jump in [i + arr[i], i - arr[i]]:
            if 0 <= jump < n and not visited[jump]:
                visited[jump] = True
                queue.append(jump)
    
    return False        