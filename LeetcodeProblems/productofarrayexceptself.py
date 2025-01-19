def product_except_self(nums):
    # Calculate the total product of all elements in the array
    total_product = 1
    zero_count = 0
    
    # Handle the case where zeros are present
    for num in nums:
        if num != 0:
            total_product *= num
        else:
            zero_count += 1
    
    # If more than one zero exists, all products will be zero
    if zero_count > 1:
        return [0] * len(nums)
    
    # Calculate the result for each element
    result = []
    for num in nums:
        if zero_count == 0:
            result.append(total_product // num)  # Normal division case
        elif num == 0:
            result.append(total_product)  # Zero exists; include total product
        else:
            result.append(0)  # Non-zero element when a zero exists elsewhere
    
    return result

# Example usage
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]

nums_with_zero = [1, 2, 0, 4]
print(product_except_self(nums_with_zero))  # Output: [0, 0, 8, 0]
