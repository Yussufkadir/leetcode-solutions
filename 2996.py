from typing import List
def missingInteger(self, nums: List[int]) -> int:
    n = len(nums)

    prefix_sum = nums[0]
    for i in range(1, n):
        if nums[i] == nums[i-1] + 1:
            prefix_sum += nums[i]
        else:
            break
    
    nums_set = set(nums)
    result = prefix_sum
    while result in nums_set:
        result += 1
    
    return result     