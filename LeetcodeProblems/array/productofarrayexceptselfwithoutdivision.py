def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and combine with prefix
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer

# Test the function
nums = [1, 2, 3, 4]
output = product_except_self(nums)
print("Output:", output)
