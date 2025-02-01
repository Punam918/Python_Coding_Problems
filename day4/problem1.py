'''You need to convert or output integers represented by binary, octal, or hexadecimal
 digits.'''
 
binary_num = "1010"
octal_num = "12"
hex_num = "A"

print(int(binary_num, 2)) 
print(int(octal_num, 8))  
print(int(hex_num, 16))   

#converting from integer to binary
num = 42

print(bin(num))  
print(oct(num))  
print(hex(num))  
