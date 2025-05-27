def binary_array_to_number(arr):
    stri = ''
    for num in arr:
        stri+=str(num)
    return stri



# for binary to decimal conversion

def binary_array_to_number(arr):
    binary_str = ''
    for bit in arr:
        binary_str += str(bit)
    return int(binary_str, 2)

        
print(binary_array_to_number([0,0,0,1]))