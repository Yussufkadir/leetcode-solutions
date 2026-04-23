from typing import List
from collections import defaultdict
def distance(self, nums: List[int]) -> List[int]:
    indices = defaultdict(list)
    for i, num in enumerate(nums):
        indices[num].append(i)
    
    arr = [0] * len(nums)
    
    for group in indices.values():
        total = sum(group)         
        prefix_sum = 0              
        
        for rank, idx in enumerate(group):
            left_count  = rank
            right_count = len(group) - rank - 1
            
            left_contribution  = idx * left_count - prefix_sum
            right_contribution = (total - prefix_sum - idx) - idx * right_count
            
            arr[idx] = left_contribution + right_contribution
            prefix_sum += idx
    
    return arr
