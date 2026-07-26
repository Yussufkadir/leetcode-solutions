from typing import List
def maximumProduct(self, nums: List[int]) -> int:
    nums.sort()
    res_1 = nums[-1] * nums[-2] * nums[-3]
    res_2 = nums[0] * nums[1] * nums[-1]
    return max(res_1, res_2)