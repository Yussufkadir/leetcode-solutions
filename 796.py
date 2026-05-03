def rotateString(self, s: str, goal: str) -> bool:
    chars = list(s)
    
    for i in range(len(s)):
        element = chars.pop(0)
        chars.append(element)

        if "".join(chars) == goal:
            return True

    return False