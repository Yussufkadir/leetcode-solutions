from collections import Counter
def maxNumberOfBalloons(self, text: str) -> int:
    needed = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}

    text_count = Counter(text)
    
    max_balloons = float('inf')
    for char, needed_count in needed.items():
        available = text_count.get(char, 0)
        max_balloons = min(max_balloons, available // needed_count)
    
    return max_balloons