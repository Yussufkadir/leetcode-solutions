from typing import List
def minMoves(self, nums: List[int]) -> int:
    max_num = max(nums)
    res = 0
    for i in nums:
        res += abs(max_num - i)
    return res