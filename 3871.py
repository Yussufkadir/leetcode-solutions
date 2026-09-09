def countCommas(n: int) -> int:
    s = str(n)
    d = len(s)
    total = 0

    for L in range(1, d):
        count = 10**L - 10**(L - 1) 
        total += count * ((L - 1) // 3) 
    
    count_last = n - 10**(d - 1) + 1
    total += count_last * ((d - 1) // 3) 

    return total