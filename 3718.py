from typing import List
def missingMultiple(self, nums: List[int], k: int) -> int:
    num_set = set(nums)
    counter = 0
    while True:
        counter += 1
        if counter * k not in num_set:
            return counter * k