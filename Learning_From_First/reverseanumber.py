'''Reverse Digits of A Number
Problem Statement: Given an integer N return the reverse of the given number.

Note: If a number has trailing zeros, then its reverse will not include them. 
For e.g., reverse of 10400 will be 401 instead of 00401.'''

def reverse_number(N):
    revers = 0
    while N>0:
        last = N%10
        revers = revers*10 + last
        N =N//10
    return revers

print(reverse_number(123004))
print(reverse_number(1234))
print(reverse_number(1000))