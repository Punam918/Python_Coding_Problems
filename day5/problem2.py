'''
You want to feed a text or binary string to code that’s been written to operate on file
like objects instead. ( files in memory)
'''

import io
text_data = "This is a sample text string."
text_file = io.StringIO(text_data)
print("Reading from the text file-like object:")
print(text_file.read())  
text_file.seek(0)
print("\nReading line-by-line:")
for line in text_file:
    print(line.strip())  
text_file.close()


# Binary String as a File-Like Object (io.BytesIO)
import io
binary_data = b"This is a sample binary data."
# Creating a file-like object from the binary data
binary_file = io.BytesIO(binary_data)
print("Reading from the binary file-like object:")
print(binary_file.read())
binary_file.seek(0)
print("\nReading binary data in chunks:")
print(binary_file.read(10)) 
binary_file.close()
