from typing import List
def maxJumps(self, arr: List[int], d: int) -> int:
    n = len(arr)
    dp = [-1] * n
    
    def dfs(i):
        if dp[i] != -1:
            return dp[i]
        
        max_jumps = 1 

        for j in range(i + 1, min(i + d + 1, n)):
            if arr[j] >= arr[i]:
                break  
            max_jumps = max(max_jumps, 1 + dfs(j))

        for j in range(i - 1, max(i - d - 1, -1), -1):
            if arr[j] >= arr[i]:
                break  
            max_jumps = max(max_jumps, 1 + dfs(j))
        
        dp[i] = max_jumps
        return dp[i]
    
    return max(dfs(i) for i in range(n))        