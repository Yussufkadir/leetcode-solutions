from typing import List
from collections import defaultdict
from bisect import bisect_left

def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
    n = len(nums)

    positions = defaultdict(list)
    for i, v in enumerate(nums):
        positions[v].append(i)

    answer = []
    for q in queries:
        val     = nums[q]
        indices = positions[val]

        if len(indices) == 1:
            answer.append(-1)
            continue

        pos = bisect_left(indices, q)  

        best = float('inf')

        right_pos = (pos + 1) % len(indices)
        j = indices[right_pos]
        right = (j - q) % n
        best  = min(best, right, n - right)

        left_pos = (pos - 1) % len(indices)
        j = indices[left_pos]
        right = (j - q) % n
        best  = min(best, right, n - right)

        answer.append(best)