from typing import List
def maxTotalValue(self, nums: List[int], k: int) -> int:
    return (max(nums) - min(nums)) * k