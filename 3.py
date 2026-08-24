def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    max_len = 0
    window_set = set()
    for right in range(len(s)):
        while s[right] in window_set:
            window_set.remove(s[left])
            left += 1
        window_set.add(s[right])
        max_len = max(len(window_set), max_len)

    return max_len
