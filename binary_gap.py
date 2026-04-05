def binaryGap(self, n: int) -> int:
    last_seen_pos = -1  
    max_distance = 0
    current_pos = 0

    while n > 0:
        if n & 1 == 1:
            if last_seen_pos != -1:
                distance = current_pos - last_seen_pos
                max_distance = max(max_distance, distance)
            last_seen_pos = current_pos
        n >>= 1
        current_pos += 1
        
    return max_distance