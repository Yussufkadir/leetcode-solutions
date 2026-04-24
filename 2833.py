def furthestDistanceFromOrigin(self, moves: str) -> int:
    count = 0
    count_l = 0
    count_r = 0
    for i in moves:
        if i == "_":
            count += 1
        elif i == "L":
            count_l += 1
        else:
            count_r += 1

    fill_right = count_r + count
    fill_left = count_l + count

    right_way = fill_right - count_l
    left_way = fill_left - count_r

    final = max(right_way, left_way)
    return final