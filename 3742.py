from typing import List
def maxPathScore(self, grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])

    dp = [[{} for _ in range(n)] for _ in range(m)]

    dp[0][0][0] = 0  
    
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue

            candidates = {}

            if i > 0:
                for cost, score in dp[i-1][j].items():
                    new_cost = cost
                    new_score = score
                    
                    val = grid[i][j]
                    if val == 1:
                        new_cost += 1
                        new_score += 1
                    elif val == 2:
                        new_cost += 1
                        new_score += 2
                    
                    if new_cost <= k:
                        if new_cost not in candidates or new_score > candidates[new_cost]:
                            candidates[new_cost] = new_score

            if j > 0:
                for cost, score in dp[i][j-1].items():
                    new_cost = cost
                    new_score = score
                    
                    val = grid[i][j]
                    if val == 1:
                        new_cost += 1
                        new_score += 1
                    elif val == 2:
                        new_cost += 1
                        new_score += 2
                    
                    if new_cost <= k:
                        if new_cost not in candidates or new_score > candidates[new_cost]:
                            candidates[new_cost] = new_score

            items = sorted(candidates.items())
            best_score = -1
            for cost, score in items:
                if score > best_score:
                    dp[i][j][cost] = score
                    best_score = score

    if not dp[m-1][n-1]:
        return -1
    return max(dp[m-1][n-1].values())     