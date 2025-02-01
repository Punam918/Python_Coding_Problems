'''write a program that compresses a file using a compression algorithm (e.g., zlib) and then another 
program to decompress it.'''

#compression
import zlib

def compress_file(input_file, output_file):
    # Open the input file in binary mode
    with open(input_file, 'rb') as f_in:
        file_data = f_in.read()

    # Compress the data using zlib
    compressed_data = zlib.compress(file_data)

    # Write the compressed data to the output file
    with open(output_file, 'wb') as f_out:
        f_out.write(compressed_data)

    print(f"File '{input_file}' compressed successfully into '{output_file}'")

if __name__ == '__main__':
    input_file = 'example.txt'  # Change this to your input file
    output_file = 'example_compressed.zlib'  # Change this to your desired output file name
    compress_file(input_file, output_file)


#decompression
import zlib

def decompress_file(input_file, output_file):
    # Open the compressed file in binary mode
    with open(input_file, 'rb') as f_in:
        compressed_data = f_in.read()

    # Decompress the data using zlib
    decompressed_data = zlib.decompress(compressed_data)

    # Write the decompressed data to the output file
    with open(output_file, 'wb') as f_out:
        f_out.write(decompressed_data)

    print(f"File '{input_file}' decompressed successfully into '{output_file}'")

if __name__ == '__main__':
    input_file = 'example_compressed.zlib'  # Change this to your compressed file
    output_file = 'example_decompressed.txt'  # Change this to your desired output file name
    decompress_file(input_file, output_file)
