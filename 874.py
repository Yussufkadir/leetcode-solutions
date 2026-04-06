from typing import List
def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    obstacle_set = set(map(tuple, obstacles))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0  
    
    x, y = 0, 0
    max_dist = 0
    
    for cmd in commands:
        if cmd == -2:       
            dir_idx = (dir_idx - 1) % 4
        elif cmd == -1:    
            dir_idx = (dir_idx + 1) % 4
        else:               
            dx, dy = directions[dir_idx]
            for _ in range(cmd):
                nx, ny = x + dx, y + dy
                if (nx, ny) not in obstacle_set:
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)
                else:
                    break  
    
    return max_dist