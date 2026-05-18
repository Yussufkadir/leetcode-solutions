from typing import List
from collections import deque
def minJumps(self, arr: List[int]) -> int:
    n = len(arr)
    if n == 1:
        return 0

    val_to_idx = {}
    for i, v in enumerate(arr):
        val_to_idx.setdefault(v, []).append(i)
    
    visited = [False] * n
    q = deque()
    q.append((0, 0))  
    visited[0] = True
    
    while q:
        i, steps = q.popleft()
        if i == n - 1:
            return steps
        
        for ni in (i - 1, i + 1):
            if 0 <= ni < n and not visited[ni]:
                visited[ni] = True
                q.append((ni, steps + 1))

        if arr[i] in val_to_idx:
            for ni in val_to_idx[arr[i]]:
                if not visited[ni]:
                    visited[ni] = True
                    q.append((ni, steps + 1))
            del val_to_idx[arr[i]]
    
    return -1         