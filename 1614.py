def maxDepth(s: str) -> int:
    temp = 0
    depth_checker = 0
    for i in s:
        if i == "(":
            temp += 1
            depth_checker = max(temp, depth_checker)
        if i == ")":
            temp -= 1
    return depth_checker
