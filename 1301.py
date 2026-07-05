from typing import List
def pathsWithMaxScore(self, board: List[str]) -> List[int]:
    MOD = 10**9 + 7
    n = len(board)

    dp_max = [[-1] * n for _ in range(n)]
    dp_ways = [[0] * n for _ in range(n)]
    dp_max[0][0] = 0
    dp_ways[0][0] = 1

    for r in range(n):
        for c in range(n):
            if board[r][c] == 'X':
                continue

            if dp_max[r][c] == -1:
                continue

            if r + 1 < n and board[r+1][c] != 'X':
                val = 0 if board[r+1][c] == 'S' else int(board[r+1][c])
                new_sum = dp_max[r][c] + val
                if new_sum > dp_max[r+1][c]:
                    dp_max[r+1][c] = new_sum
                    dp_ways[r+1][c] = dp_ways[r][c]
                elif new_sum == dp_max[r+1][c]:
                    dp_ways[r+1][c] = (dp_ways[r+1][c] + dp_ways[r][c]) % MOD

            if c + 1 < n and board[r][c+1] != 'X':
                val = 0 if board[r][c+1] == 'S' else int(board[r][c+1])
                new_sum = dp_max[r][c] + val
                if new_sum > dp_max[r][c+1]:
                    dp_max[r][c+1] = new_sum
                    dp_ways[r][c+1] = dp_ways[r][c]
                elif new_sum == dp_max[r][c+1]:
                    dp_ways[r][c+1] = (dp_ways[r][c+1] + dp_ways[r][c]) % MOD

            if r + 1 < n and c + 1 < n and board[r+1][c+1] != 'X':
                val = 0 if board[r+1][c+1] == 'S' else int(board[r+1][c+1])
                new_sum = dp_max[r][c] + val
                if new_sum > dp_max[r+1][c+1]:
                    dp_max[r+1][c+1] = new_sum
                    dp_ways[r+1][c+1] = dp_ways[r][c]
                elif new_sum == dp_max[r+1][c+1]:
                    dp_ways[r+1][c+1] = (dp_ways[r+1][c+1] + dp_ways[r][c]) % MOD

    if dp_max[n-1][n-1] == -1:
        return [0, 0]
    return [dp_max[n-1][n-1], dp_ways[n-1][n-1]]        