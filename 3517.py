from collections import Counter
def smallestPalindrome(self, s: str) -> str:
    freq = Counter(s)

    left = []
    middle = ''

    for ch in sorted(freq.keys()):
        count = freq[ch]

        if count % 2 == 1:
            middle = ch
        
        left.append(ch * (count // 2))

    left_half = ''.join(left)

    return left_half + middle + left_half[::-1] 