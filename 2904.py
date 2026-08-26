def shortestBeautifulSubstring( s: str, k: int) -> str:
    n = len(s)
    left = 0
    right = 0
    counter = 0
    best = ""
    min_len = float('inf')

    while right < n:
        if s[right] == "1":
            counter += 1
        right += 1  
        while counter == k:
            length = right - left
            candidate = s[left:right]
            if length < min_len or (length == min_len and candidate < best):
                min_len = length
                best = candidate

            if s[left] == "1":
                counter -= 1
            left += 1

    return best

shortestBeautifulSubstring("100011001", 3)           