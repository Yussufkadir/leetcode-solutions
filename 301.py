def removeInvalidParentheses(self, s: str) -> list[str]:
    l = r = 0
    for c in s:
        if c == '(':
            l += 1
        elif c == ')':
            if l > 0:
                l -= 1
            else:
                r += 1

    res = set()         
    path = []

    def dfs(i, l_rem, r_rem, bal):
        if i == len(s):
            if l_rem == 0 and r_rem == 0 and bal == 0:
                res.add(''.join(path))
            return

        c = s[i]

        if c == '(' and l_rem > 0:
            dfs(i + 1, l_rem - 1, r_rem, bal)
        elif c == ')' and r_rem > 0:
            dfs(i + 1, l_rem, r_rem - 1, bal)

        if c == '(':
            path.append(c)
            dfs(i + 1, l_rem, r_rem, bal + 1)
            path.pop()
        elif c == ')':
            if bal > 0:                 
                path.append(c)
                dfs(i + 1, l_rem, r_rem, bal - 1)
                path.pop()
        else:                       
            path.append(c)
            dfs(i + 1, l_rem, r_rem, bal)
            path.pop()

    dfs(0, l, r, 0)
    return list(res)     