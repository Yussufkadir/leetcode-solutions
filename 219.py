from typing import List
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    last_seen = {}
    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    return False

containsNearbyDuplicate([4,1,2,3,1,5], 3)