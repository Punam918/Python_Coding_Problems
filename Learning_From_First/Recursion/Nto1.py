def print_n_to_1(n):
    if n < 1:  # Base condition to stop recursion
        return
    print(n)  
    print_n_to_1(n - 1) 
print_n_to_1(10)

def recursion(num):
    if num > 0:
        print(num, end=" ")  # Print first
        recursion(num - 1)  # Then recurse

recursion(8)
