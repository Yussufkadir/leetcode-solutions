def targetIndices(self, nums: list[int], target: int) -> list[int]:
    nums.sort()
    final_list = []
    for i in range(len(nums)):
        if nums[i] == target:
            final_list.append(i)
    return final_list