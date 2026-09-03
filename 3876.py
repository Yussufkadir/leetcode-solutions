def uniformArray(nums1: list[int]) -> bool:
    odds = [x for x in nums1 if x % 2 == 1]
    evens = [x for x in nums1 if x % 2 == 0]
    if not odds or not evens:
        return True
    return min(odds) < min(evens)