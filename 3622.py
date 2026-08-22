from math import prod
def checkDivisibility(n: int) -> bool:
    seperated_number = []
    digit = n
    while digit > 0:
        decimal = digit % 10
        seperated_number.append(decimal)
        digit = digit // 10

    sum_add = sum(seperated_number)
    sum_prod = prod(seperated_number)

    total_sum = sum_add + sum_prod

    if n % total_sum == 0:
        return True

    return False
