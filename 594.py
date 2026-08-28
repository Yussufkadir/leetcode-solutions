from typing import List
from collections import Counter
def findLHS(nums: List[int]) -> int:
    counter_dict = Counter(nums)
    counter = 0
    placeholder = 0
    for num in counter_dict:
        if (num + 1) in counter_dict:
            placeholder = counter_dict[num] + counter_dict[num+1]
            counter = max(counter, placeholder)
        
    return counter


findLHS([1,1,1,1])