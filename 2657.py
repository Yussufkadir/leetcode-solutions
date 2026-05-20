from typing import List
def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
    n = len(A)
    seenA = [False] * (n + 1)
    seenB = [False] * (n + 1)
    common = 0
    C = []
    for i in range(n):
        if not seenA[A[i]]:
            seenA[A[i]] = True
            if seenB[A[i]]:
                common += 1
        if not seenB[B[i]]:
            seenB[B[i]] = True
            if seenA[B[i]]:
                common += 1
        C.append(common)
    return C        