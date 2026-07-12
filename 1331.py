from typing import List
def arrayRankTransform(self, arr: List[int]) -> List[int]:
    sorted_unique = sorted(set(arr))

    rank_map = {}
    for i, val in enumerate(sorted_unique, 1):
        rank_map[val] = i
    
    return [rank_map[val] for val in arr]     