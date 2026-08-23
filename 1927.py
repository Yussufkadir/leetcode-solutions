def sumGame(num: str) -> bool:
    n = len(num)
    half = n // 2
    sum1 = sum2 = 0
    cnt1 = cnt2 = 0
    
    for i, ch in enumerate(num):
        if ch == '?':
            if i < half:
                cnt1 += 1
            else:
                cnt2 += 1
        else:
            if i < half:
                sum1 += int(ch)
            else:
                sum2 += int(ch)
    
    q = cnt1 + cnt2
    if q % 2 == 1:
        return True  
    
    V = (sum1 - sum2) + 9 * (cnt1 - cnt2) // 2
    return V != 0


sumGame("81??")