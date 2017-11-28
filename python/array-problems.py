def add_up(nums, s):
    seen = set()
    pairs = []
    for num in nums:
        if num in seen:
            pairs.append((num, s - num ))
        seen.add(s - num)
    return pairs


print add_up([2, 4, 6, 8, 3, 3, 1], 10)
