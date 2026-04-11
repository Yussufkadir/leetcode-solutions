from collections import defaultdict
from typing import List
def minimumDistance(self, nums: List[int]) -> int:
    positions = defaultdict(list)
    for i, v in enumerate(nums):
        positions[v].append(i)

    result = float('inf')

    for idx in positions.values():
        if len(idx) < 3:
            continue
        for t in range(len(idx) - 2):
            result = min(result, 2 * (idx[t + 2] - idx[t]))

    return -1 if result == float('inf') else result