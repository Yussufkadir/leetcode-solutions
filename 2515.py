from typing import List
def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
    n = len(words)
    result = float('inf')

    for i, word in enumerate(words):
        if word == target:
            right = (i - startIndex) % n   
            left  = n - right               
            result = min(result, right, left)

    return -1 if result == float('inf') else result