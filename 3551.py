from typing import List
def minSwaps(self, nums: List[int]) -> int:
    def digit_sum(x: int) -> int:
        s = 0
        while x:
            s += x % 10
            x //= 10
        return s

    n = len(nums)
    order = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))

    visited = [False] * n
    cycles = 0
    for i in range(n):
        if visited[i]:
            continue
        cycles += 1
        j = i
        while not visited[j]:
            visited[j] = True
            j = order[j]

    return n - cycles   