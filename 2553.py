from typing import List
def separateDigits(self, nums: List[int]) -> List[int]:
    dummy = []
    for i in nums:
        i = str(i)
        if len(i) >= 1:
            for j in i:
                j = int(j)
                dummy.append(j)
        else:
            i = int(i)
            dummy.append(i)
    return dummy