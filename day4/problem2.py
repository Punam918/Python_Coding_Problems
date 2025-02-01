
'''
You have a byte string and you need to unpack it into an integer value. Alternatively,
 you need to convert a large integer back into a byte string
'''

byte_string = b'\x00\x10'
integer_value = int.from_bytes(byte_string)  
print(integer_value) 


integer_value = 16
byte_length = 3  
byte_string = integer_value.to_bytes(byte_length, byteorder='big') 
print(byte_string)  
