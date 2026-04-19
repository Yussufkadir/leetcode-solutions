from typing import List
def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
    i = len(nums1) - 1   
    j = len(nums2) - 1   
    max_dist = 0

    while i >= 0 and j >= 0:
        if nums1[i] <= nums2[j]:
            max_dist = max(max_dist, j - i)
            i -= 1         
        else:
            j -= 1        

    return max_dist    