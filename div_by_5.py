def prefixesDivBy5(nums):
    """Return a list where each element indicates whether the binary
    number represented by the prefix ending at that index is divisible by 5.

    Uses rolling modulo to avoid large integers: val = (val*2 + bit) % 5.
    """
    result = []
    val = 0
    for bit in nums:
        val = (val * 2 + bit) % 5
        result.append(val == 0)
    return result


if __name__ == "__main__":
    arr = [1, 1, 0]
    print(prefixesDivBy5(arr))