from typing import List
def validSequence(self, word1: str, word2: str) -> List[int]:
    n, m = len(word1), len(word2)
    if m > n:
        return []

    suffix = [0] * (n + 1)
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and word1[i] == word2[j]:
            j -= 1
        suffix[i] = m - 1 - j

    result = []
    changed = False
    idx = 0

    for i, ch in enumerate(word2):
        matched = False
        while idx < n:
            if word1[idx] == ch:
                result.append(idx)
                idx += 1
                matched = True
                break
            elif not changed and suffix[idx + 1] >= m - i - 1:
                result.append(idx)
                idx += 1
                changed = True
                matched = True
                break
            idx += 1
        if not matched:
            return []

    return result 