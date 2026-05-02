def rotatedDigits(self, n: int) -> int:
    count = 0
    current = 1
    
    while current <= n:
        s = str(current)

        has_invalid = False
        for digit in s:
            if digit in '347':
                has_invalid = True
                break
        
        if has_invalid:
            current += 1
            continue

        has_changing = False
        for digit in s:
            if digit in '2569':
                has_changing = True
                break
        
        if has_changing:
            count += 1
        
        current += 1
    
    return count