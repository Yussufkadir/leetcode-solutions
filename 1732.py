from typing import List
def largestAltitude(gain: List[int]) -> int:
    new_list = []
    new_list.append(0)
    sum_list = 0
    for i in range(len(gain)):
        sum_list = new_list[i] + gain[i]
        new_list.append(sum_list)
    return max(new_list) 

largestAltitude(gain = [-5,1,5,0,-7])