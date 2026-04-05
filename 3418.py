from typing import List
def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = float('-inf')

        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = coins[0][0]  
        if coins[0][0] < 0:
            dp[0][0][1] = 0                               
        else:
            dp[0][0][1] = coins[0][0]

        for j in range(1, n):
            for k in range(3):
                if dp[0][j-1][k] == NEG_INF:
                    continue
                val = dp[0][j-1][k] + coins[0][j]
                dp[0][j][k] = max(dp[0][j][k], val)
                if coins[0][j] < 0 and k < 2:
                    val2 = dp[0][j-1][k]                 
                    dp[0][j][k+1] = max(dp[0][j][k+1], val2)
        for i in range(1, m):
            for k in range(3):
                if dp[i-1][0][k] == NEG_INF:
                    continue
                val = dp[i-1][0][k] + coins[i][0]
                dp[i][0][k] = max(dp[i][0][k], val)
                if coins[i][0] < 0 and k < 2:
                    val2 = dp[i-1][0][k]
                    dp[i][0][k+1] = max(dp[i][0][k+1], val2)
        for i in range(1, m):
            for j in range(1, n):
                for k in range(3):
                    incoming = max(dp[i-1][j][k], dp[i][j-1][k])
                    if incoming == NEG_INF:
                        continue
                    val = incoming + coins[i][j]
                    dp[i][j][k] = max(dp[i][j][k], val)
                    if coins[i][j] < 0 and k < 2:
                        val2 = incoming                  
                        dp[i][j][k+1] = max(dp[i][j][k+1], val2)

        return max(dp[m-1][n-1])