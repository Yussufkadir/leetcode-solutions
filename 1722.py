from typing import List, Counter
from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)

        for a, b in allowedSwaps:
            uf.union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)

        hamming = 0
        for indices in groups.values():
            src_count = Counter(source[i] for i in indices)
            tgt_count = Counter(target[i] for i in indices)

            matched = sum((src_count & tgt_count).values()) 
            hamming += len(indices) - matched

        return hamming        