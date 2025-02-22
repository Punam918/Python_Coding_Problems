# Finding sum of digits of a number until sum becomes single digit
'''
Input: n = 1234 
Output: 1 
Explanation:
Step 1: 1 + 2 + 3 + 4 = 10 
Step 2: 1 + 0 = 1

'''
def singleDigit(n):
    sum = 0
    while n > 0 or sum > 9:

        # If n becomes 0, reset it to sum 
        # and start a new iteration
        if n == 0:
            n = sum
            sum = 0

        sum += n % 10
        n //= 10
    return sum

if __name__ == "__main__":
    n = 1234
    print(singleDigit(n))