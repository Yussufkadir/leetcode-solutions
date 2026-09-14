from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    step = float('inf')
    left = 0
    right = 0
    current_count = 0

    while right < len(nums):
        current_count += nums[right]
        while current_count >= target:
            step = min(step, right - left + 1)
            current_count -= nums[left]
            left += 1
        right += 1
    if step == float('inf'):
        return 0
    return step

minSubArrayLen(11, [1,2,3,4,5])