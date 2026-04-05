def loop(nums):
        counter = 0
        while sum(nums) != 0:
            min_positives = min((x for x in nums if x > 0), default=float('inf'))
            if min_positives in nums:
                nums = [x if x != min_positives else 0 for x in nums]   
                counter += 1
        return counter

result = loop([0,2])
print(result)