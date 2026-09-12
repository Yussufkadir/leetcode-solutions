from typing import List
def decrypt(code: List[int], k: int) -> List[int]:
    virtual_list = code * 2
    final_list = []

    if k < 0:
        k = abs(k)
        code = code[::-1]
        virtual_list = code * 2
        final_list = []
        for i in range(len(code)):
            sum_of_nums = sum(virtual_list[i+1 : i+1+k])
            final_list.append(sum_of_nums)
        return final_list[::-1]

    else:
        for i in range(len(code)):
            sum_of_nums = sum(virtual_list[i+1 : i+1+k])
            final_list.append(sum_of_nums)
    return final_list
            
        