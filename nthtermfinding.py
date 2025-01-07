# Function to find the Nth term of an Arithmetic Series
def find_nth_term(a1, a2, n):
    # Calculate the common difference
    d = a2 - a1
    # Calculate the Nth term using the formula: a_n = a1 + (n-1) * d
    nth_term = a1 + (n - 1) * d
    return nth_term

# Input: first two terms and the term number to find
a1 = int(input("Enter the first term (a1): "))
a2 = int(input("Enter the second term (a2): "))
n = int(input("Enter the term number to find (n): "))

# Find and print the Nth term
nth_term = find_nth_term(a1, a2, n)
print(f"The {n}th term of the arithmetic series is: {nth_term}")