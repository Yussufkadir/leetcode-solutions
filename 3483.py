from typing import List
from math import factorial
def totalNumbers(digits: List[int]) -> int:
    final_set = set(digits)
    even_set = set([ i for i in digits if i % 2 == 0])

    if final_set == even_set:
        return factorial(len(even_set))

    final_count = 0

    print(final_set)
    print(even_set)

    for i in digits:
        if i not in even_set and len(even_set) != 0:
            final_count += factorial(len(even_set) + 1)

        

    return final_count


totalNumbers([1,3,5])