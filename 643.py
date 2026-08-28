from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    max_range = float("-inf")
    initial_slice = sum(nums[0:k])
    max_range = max(max_range, initial_slice)
    new_sum = 0
    if len(nums) == 1:
        return nums[0] / k
    
    for i in range(len(nums)):
        if i == 0:
            continue
        if (k + i) - 1 <= len(nums) - 1:
            new_sum = nums[k + i - 1] + (initial_slice - nums[i - 1])
            initial_slice = new_sum
            max_range = max(max_range, new_sum)

    return max_range / k

findMaxAverage([1,12,-5,-6,50,3], 4)