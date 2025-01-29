class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string and check if it's equal to its reverse
        return str(x) == str(x)[::-1]

# Create an instance of the Solution class
solution = Solution()

# Test cases
print(solution.isPalindrome(121))     # Output: True
print(solution.isPalindrome(-121))    # Output: False
print(solution.isPalindrome('madam'))     # Output: False
