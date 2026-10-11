from typing import List
def sumOfSquares(nums: List[int]) -> int:
    len_n = len(nums)
    count = 0
    for index, val in enumerate(nums, start=1):
        if len_n % index == 0:
            count += (val*val)
    return count
