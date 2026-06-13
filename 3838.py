from typing import List
def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
    result = []
    for word in words:
        total = sum(weights[ord(c) - ord('a')] for c in word)
        r = total % 26
        result.append(chr(122 - r))
    return ''.join(result)