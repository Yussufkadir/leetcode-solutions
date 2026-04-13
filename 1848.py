from typing import List
def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
    output = float('inf')
    for i in range(len(nums)):
        if nums[i] == target:
            output = min(output, abs(i - start))
    return output