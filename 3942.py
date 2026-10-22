from typing import List
def minOperations(self, nums: List[int]) -> int:
    n = len(nums)
    INF = float('inf')
    res = INF

    k = nums[0]
    if all(nums[i] == (k + i) % n for i in range(n)):
        res = 0 if k == 0 else min(n - k, k + 2)

    c = nums[0]
    if all(nums[i] == (c - i) % n for i in range(n)):
        res = min(res, (c + 1) % n + 1, 1 + (n - c - 1) % n)

    return -1 if res == INF else res  