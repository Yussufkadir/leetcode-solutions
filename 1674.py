from typing import List
def minMoves(self, nums: List[int], limit: int) -> int:
    n = len(nums)
    pairs = n // 2
    diff = [0] * (2 * limit + 5) 

    for i in range(pairs):
        a = nums[i]
        b = nums[n - 1 - i]
        low = min(a, b) + 1
        high = max(a, b) + limit
        total = a + b

        diff[low] -= 1
        diff[high + 1] += 1

        diff[total] -= 1
        diff[total + 1] += 1

    curr = 0
    best = float('inf')
    base = pairs * 2  

    for s in range(2, 2 * limit + 1):
        curr += diff[s]
        moves = base + curr
        if moves < best:
            best = moves

    return best        