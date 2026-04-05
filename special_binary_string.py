def makeLargestSpecial(self, s: str) -> str:
    if not s:
        return ""
    
    mountains = []
    balance = 0
    left = 0
        

    for right, char in enumerate(s):
        if char == '1':
            balance += 1
        else:
            balance -= 1

        if balance == 0:
            inner_string = s[left + 1 : right]

            solved_inner = self.makeLargestSpecial(inner_string)
            mountains.append('1' + solved_inner + '0')

            left = right + 1

    mountains.sort(reverse=True)

    return "".join(mountains)