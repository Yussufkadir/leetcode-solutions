def mirrorDistance(self, n: int) -> int:
    reverse = int(str(n)[::-1])

    abs_val = abs(n - reverse)
    return abs_val