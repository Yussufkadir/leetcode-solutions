from collections import deque
from typing import List
def assignEdgeWeights(self, edges: List[List[int]]) -> int:
    MOD = 10**9 + 7
    n = len(edges) + 1
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1]*(n+1)
    dist[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    max_depth = max(dist[1:])   
    return pow(2, max_depth-1, MOD)