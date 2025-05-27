'''In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''
def high_and_low(numbers):
    str_numbers = numbers.split()
    int_numbers = []
    
    for s in str_numbers:
        int_numbers.append(int(s))
        
    highest = int_numbers[0]
    lowest = int_numbers[0]
    
    for num in int_numbers:
        if num> highest:
            highest = num
        if num<lowest:
            lowest = num
    return f"{highest} {lowest}"