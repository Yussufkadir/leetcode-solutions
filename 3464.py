from typing import List
def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
    perimeter = 4 * side
    positions = []
    for x, y in points:
        if y == 0:
            pos = x
        elif x == side:
            pos = side + y
        elif y == side:
            pos = 2 * side + (side - x)
        else:  
            pos = 3 * side + (side - y)
        positions.append(pos)
    
    positions.sort()
    
    def can_pick_k(D):
        n = len(positions)
        extended = positions + [p + perimeter for p in positions]

        next_idx = [0] * (2 * n)
        j = 0
        for i in range(2 * n):
            while j < 2 * n and extended[j] - extended[i] < D:
                j += 1
            next_idx[i] = j

        for start in range(n):
            cur = start
            for _ in range(k - 1):
                cur = next_idx[cur]
                if cur >= start + n:  
                    break
            else:
                if extended[start] + perimeter - extended[cur] >= D:
                    return True
        return False
    left, right = 1, 2 * side
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if can_pick_k(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans        