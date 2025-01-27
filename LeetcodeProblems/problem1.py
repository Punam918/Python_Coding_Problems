nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

largest_3 = sorted(nums, reverse=True)[:3]
smallest_3 = sorted(nums)[:3]

print("Largest 3 numbers:", largest_3)
print("Smallest 3 numbers:", smallest_3)
