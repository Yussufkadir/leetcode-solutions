def minInsertions(self, s: str) -> int:
    open_count = 0
    ans = 0
    i, n = 0, len(s)
    while i < n:
        if s[i] == "(":
            open_count += 1
        else:
            if i + 1 < n and s[i + 1] == ")":
                i += 1
            else:
                ans += 1
            if open_count > 0:
                open_count -= 1
            else:
                ans += 1
        i += 1
    return ans + 2 * open_count