def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
    n = len(s)
    if s[-1] == '1':
        return False
    
    dp = [False] * n
    dp[0] = True
    pre = [0] * (n + 1)
    pre[1] = 1
    
    for j in range(1, n):
        if s[j] == '0':
            left = max(0, j - maxJump)
            right = j - minJump
            if right >= 0:
                if pre[right + 1] - pre[left] > 0:
                    dp[j] = True
        
        pre[j + 1] = pre[j] + (1 if dp[j] else 0)
    
    return dp[-1]        