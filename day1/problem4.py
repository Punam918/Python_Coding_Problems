'''Converting integer to roman'''
def int_to_roman(num: int) -> str:
    # Define a list of tuples containing Roman numerals and their values
    roman_symbols = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ""
    
    # Iterate through each Roman numeral and its value
    for value, symbol in roman_symbols:
        while num >= value:  # Keep subtracting while the value fits
            result += symbol  # Append the Roman numeral
            num -= value      # Reduce the integer value by the Roman numeral's value
    
    return result

# Example usage:
integer_value = 1994
roman_numeral = int_to_roman(integer_value)
print(f"The Roman numeral for {integer_value} is {roman_numeral}")
