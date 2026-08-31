def countGoodSubstrings(s: str) -> int:
    left = 0
    right = 0
    check_list = []
    counter = 0
    while right < len(s):
        check_list.append(s[right])
        right += 1
        while len(check_list) == 3:
            if len(set(check_list)) == 3:
                counter += 1
            check_list.remove(s[left])
            left += 1
        
    return counter
