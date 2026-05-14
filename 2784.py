from typing import List
from collections import Counter
def isGood(nums: List[int]) -> bool:
    n = len(nums)
    if n == 0:
        return False

    m = max(nums)

    if n != m + 1:
        return False

    from collections import Counter
    freq = Counter(nums)

    for i in range(1, m):
        if freq.get(i, 0) != 1:
            return False

    return freq.get(m, 0) == 2
