from collections import List
def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
    def diff(w1, w2):
        return sum(c1 != c2 for c1, c2 in zip(w1, w2))
    
    result = []
    for query in queries:
        for word in dictionary:
            if diff(query, word) <= 2:
                result.append(query)
                break               
    
    return result    