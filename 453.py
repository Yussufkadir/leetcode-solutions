def minMoves(self, nums: list[int]) -> int:
    if len(set(nums)) == 1:
        return 0
    min_num = min(nums)
    final_sum = 0
    for i in nums:
        if i == min_num:
            continue
        else:
            final_sum += i - min_num
    return final_sum
