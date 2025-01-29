

''' 
5. Explore bytes strings, encoding and decoding of the strings. Provided a text file containing some 
text, write a program that reads the file, converts its contents to bytes, and saves it as a new file. Then,  
read the bytes file, decode it back to a string, and print the original text.

'''
input_filename = "input.txt"  # for string file
bytes_filename = "bytes_output.bin"  # storing byte file

with open(input_filename, "r", encoding="utf-8") as file:
    original_text = file.read()


encoded_bytes = original_text.encode("utf-8")

# Writing the bytedata to a new file
with open(bytes_filename, "wb") as bytes_file:
    bytes_file.write(encoded_bytes)

print("Text successfully encoded to bytes and written to a new file.")

#Reading the bytes file and decode it back to the string

with open(bytes_filename, "rb") as bytes_file:
    read_bytes = bytes_file.read()

decoded_text = read_bytes.decode("utf-8")

print("\nDecoded text from bytes:")
print(decoded_text)

# Verifing that the decoded text matches the original text
if original_text == decoded_text:
    print("\nThe decoded text matches the original text!")
else:
    print("\nThe decoded text does NOT match the original text.")
