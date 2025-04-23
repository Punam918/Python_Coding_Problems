def print_n_times(n):
    if n == 0:  
        return 0
    print("Recursion is awesome!")
    print_n_times(n - 1) 
print(print_n_times(6))