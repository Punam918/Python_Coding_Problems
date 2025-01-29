from fractions import Fraction

def get_fraction_input(prompt):
    numerator = int(input(f"Enter the numerator for {prompt}: "))
    denominator = int(input(f"Enter the denominator for {prompt}: "))
    return Fraction(numerator, denominator)

def main():
    print("Enter the first fraction:")
    fraction1 = get_fraction_input("first fraction")
    
    print("Enter the second fraction:")
    fraction2 = get_fraction_input("second fraction")
    
    result = fraction1 + fraction2
    print(f"The sum of {fraction1} and {fraction2} is {result}")

if __name__ == "__main__":
    main()