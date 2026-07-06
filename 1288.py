from typing import List
def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    n = len(intervals)
    covered = [False] * n
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a, b = intervals[i]
            c, d = intervals[j]
            
            if c <= a and b <= d:
                covered[i] = True
                break  
    
    return n - sum(covered)