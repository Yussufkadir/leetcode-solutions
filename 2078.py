from typing import List
def maxDistance(self, colors: List[int]) -> int:
    count = 0
    max_val = 0
    placeholder = 0
    for i in range(len(colors)):
        for j in range(len(colors[::-1])):
            if colors[i] != colors[j]:
                placeholder = abs(i - j)
                max_val = max(max_val, placeholder)
    return max_val