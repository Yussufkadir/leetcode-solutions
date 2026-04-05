def survivedRobotsHealths(positions, healths, directions):    
    n = len(positions)

    robots = []
    for i in range(n):
        robots.append([positions[i], healths[i], directions[i], i])

    robots.sort()
    
    stack = [] 
    
    for robot in robots:

        if robot[2] == 'R':
            stack.append(robot)
            continue

        while stack and robot[1] > 0:
            top_r = stack[-1]
            
            if robot[1] > top_r[1]:
                robot[1] -= 1
                stack.pop()
            elif robot[1] < top_r[1]:
                top_r[1] -= 1
                robot[1] = 0 
            else:
                robot[1] = 0
                stack.pop()
        
    survivors = []
    for r in robots:
        if r[1] > 0:
            survivors.append(r)

    survivors.sort(key=lambda x: x[3])
    
    return [r[1] for r in survivors]