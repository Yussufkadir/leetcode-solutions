from typing import List
def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
    pivot_1 = []
    pivot_2 = []
    pivot_3 = []
    for i in nums:
        if i < pivot:
            pivot_1.append(i)
        elif i == pivot:
            pivot_2.append(i)
        else:
            pivot_3.append(i)
    return pivot_1 + pivot_2 + pivot_3