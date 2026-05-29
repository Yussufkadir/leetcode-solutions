from typing import List
def minElement(self, nums: List[int]) -> int:
    placeholder = float("inf")
    for i in nums:
        count = 0
        while i > 0:
            count += i % 10
            i //= 10
        placeholder = min(placeholder, count)
    return placeholder