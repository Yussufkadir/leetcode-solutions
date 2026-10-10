def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
    k = k1 + k2
    d = [abs(a - b) for a, b in zip(nums1, nums2)]
    if sum(d) <= k:
        return 0
    
    freq = [0] * (max(d) + 1)
    for x in d:
        freq[x] += 1
    
    for v in range(len(freq) - 1, 0, -1):
        c = freq[v]
        if c == 0:
            continue
        take = min(c, k)     
        freq[v] -= take
        freq[v - 1] += take
        k -= take
        if k == 0:
            break
    
    return sum(v * v * c for v, c in enumerate(freq))        