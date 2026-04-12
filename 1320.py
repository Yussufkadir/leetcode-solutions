def minimumDistance(self, word: str) -> int:
    def dist(a, b):
        if a == -1: return 0 
        r1, c1 = divmod(a, 6)
        r2, c2 = divmod(b, 6)
        return abs(r1 - r2) + abs(c1 - c2)

    n = len(word)
    w = [ord(c) - ord('A') for c in word]

    INF = float('inf')
    dp = [INF] * 27
    dp[26] = 0  

    for i in range(n):
        new_dp = [INF] * 27
        cur = w[i]
        prev = w[i-1] if i > 0 else -1

        for other in range(27):
            if dp[other] == INF:
                continue
            cost = dp[other]

            other_letter = other if other < 26 else -1

            move_cost = dist(prev, cur)
            new_other = other  
            new_dp[new_other] = min(new_dp[new_other], cost + move_cost)

            move_cost2 = dist(other_letter, cur)
            new_other2 = prev if prev != -1 else 26
            new_dp[new_other2] = min(new_dp[new_other2], cost + move_cost2)

        dp = new_dp

    return min(dp)   