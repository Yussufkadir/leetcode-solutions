from sortedcontainers import SortedList
from typing import List
def minOperations(self, nums: List[int], x: int, k: int) -> int:
    n = len(nums)
    lo, hi = SortedList(), SortedList()   
    sum_lo = sum_hi = 0
    cost = [0] * (n - x + 1)             

    def add(v):
        nonlocal sum_lo, sum_hi
        if lo and v > lo[-1]:
            hi.add(v); sum_hi += v
        else:
            lo.add(v); sum_lo += v

    def remove(v):
        nonlocal sum_lo, sum_hi
        if lo and v <= lo[-1]:
            lo.remove(v); sum_lo -= v
        else:
            hi.remove(v); sum_hi -= v

    def balance():
        nonlocal sum_lo, sum_hi
        while len(lo) > len(hi) + 1:
            v = lo.pop(); sum_lo -= v
            hi.add(v); sum_hi += v
        while len(lo) < len(hi):
            v = hi.pop(0); sum_hi -= v
            lo.add(v); sum_lo += v

    for i, v in enumerate(nums):
        add(v)
        if i >= x:
            remove(nums[i - x])
        balance()
        if i >= x - 1:
            m = lo[-1]
            cost[i - x + 1] = m * len(lo) - sum_lo + sum_hi - m * len(hi)

    INF = float('inf')
    prev = [0] * (n + 1)
    for j in range(1, k + 1):
        cur = [INF] * (n + 1)
        for i in range(j * x, n + 1):
            cur[i] = min(cur[i - 1],                    
                            prev[i - x] + cost[i - x])     
        prev = cur
    return prev[n]        