from collections import defaultdict, deque
from typing import List
def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    for a, b in invocations:
        graph[a].append(b)

    suspicious = set()
    queue = deque([k])
    suspicious.add(k)
    
    while queue:
        method = queue.popleft()
        for called in graph[method]:
            if called not in suspicious:
                suspicious.add(called)
                queue.append(called)

    reverse_graph = defaultdict(list)
    for a, b in invocations:
        reverse_graph[b].append(a)

    can_remove = True
    for method in suspicious:
        for caller in reverse_graph[method]:
            if caller not in suspicious:
                can_remove = False
                break
        if not can_remove:
            break

    if can_remove:
        return [i for i in range(n) if i not in suspicious]
    else:
        return list(range(n))        