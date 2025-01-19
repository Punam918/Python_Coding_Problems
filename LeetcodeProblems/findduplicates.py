def contains_duplicate(nums):
    seen = set()  # Initialize an empty set to track seen numbers
    
    for num in nums:
        if num in seen:  # If the number is already in the set, it's a duplicate
            return True
        seen.add(num)  # Add the number to the set if it's not already there
    
    return False  # If no duplicates were found, return False

# Example usage
nums = [1, 2, 3, 1]
print(contains_duplicate(nums))
