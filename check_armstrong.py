# 1. Define a function to check if a number is an Armstrong number.
# 2. Inside the function, convert the number to a string to easily iterate over each digit.
# 3. Initialize a variable to store the sum of the digits raised to the power of the number of digits.
# 4. Iterate over each digit in the number:
#     a. Convert the digit back to an integer.
#     b. Raise the digit to the power of the number of digits.
#     c. Add the result to the sum.
# 5. Check if the sum is equal to the original number.
# 6. If they are equal, return True (the number is an Armstrong number).
# 7. Otherwise, return False.
# 8. Test the function with some example numbers.
def armstrong_number(n):
    num = str(n)
    value = len(num)
    total = 0
    for digit in num:
        total+= int(digit)**value
    if total ==n:
        return True
    else:
        return False
inp = int(input("enter a number"))
if armstrong_number(inp):
    print("yes,it is")
else:
    print("nein,es ist nicht")