def is_armstrong(n):
    num_digits = len(str(n))  #len function doesn't work for int but string
    original = n
    armstrong_sum = 0
    
    while n > 0:
        digit = n % 10 
        armstrong_sum += digit ** num_digits 
        n //= 10 
    return armstrong_sum == original  

print(is_armstrong(153))   
print(is_armstrong(9474))  
print(is_armstrong(123))  


'''String is iterable but int is not so we can iterate by converting int to string'''
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)  
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)  
    return armstrong_sum == n

print(is_armstrong(153))  
print(is_armstrong(9474))  
print(is_armstrong(123))
