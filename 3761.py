from typing import List
from collections import defaultdict
def minMirrorPairDistance(self, nums: List[int]) -> int:
    def reverse(x):
        return int(str(x)[::-1])

    seen = {}  
    result = float('inf')

    for j, val in enumerate(nums):
        if val in seen:
            result = min(result, j - seen[val])  

        seen[reverse(val)] = j 

    return -1 if result == float('inf') else result