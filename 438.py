from typing import List
def findAnagrams(s: str, p: str) -> List[int]:
    len_s = len(s)
    len_p = len(p) 
    final_s = []
    temp_map = {}
    p_map = {}
    for i in p:
        p_map[i] = p_map.get(i, 0) + 1
    for i in range(len_s - len_p + 1):
        for j in range(len(p)):
            temp_map.add(s[j], 0) + 1
            if temp_map == p_map:
                final_s.append(j)
    return final_s

s = "cbaebabacd"
p = "abc"

findAnagrams(s, p)