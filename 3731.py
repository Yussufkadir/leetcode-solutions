from typing import List
def findMissingElements(self, nums: List[int]) -> List[int]:
    max_n = max(nums)
    min_n = min(nums)

    nums_set = set(nums)

    res = []
    
    for i in range(min_n, max_n + 1):
        if i not in nums_set:
            res.append(i)
    
    return res