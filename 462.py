def minMoves2(self, nums: list[int]) -> int:
    nums.sort()
    anchor = nums[len(nums) // 2]
    final_sum = 0

    for i in nums:
        final_sum += abs(anchor - i)
    
    return final_sum