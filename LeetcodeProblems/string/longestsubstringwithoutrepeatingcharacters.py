'''
Given a string s, find the length of the longest
substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with a length of 3'''
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()  # To store unique characters in the current window
    start = 0  # Start pointer for the sliding window
    max_length = 0  # Variable to keep track of the maximum length

    for end in range(len(s)):
        # If we encounter a repeating character, shrink the window from the left
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        # Add the current character to the set
        char_set.add(s[end])
        # Update the max length
        max_length = max(max_length, end - start + 1)

    return max_length

s = "abcabcbb"
result = lengthOfLongestSubstring(s)
print(result)  # Output: 3
