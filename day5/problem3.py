'''
create a program that can merge multiple text files into one file and another program to split a large 
file into smaller files based on a specified file size or line count.
'''
#Merging many files to one file 
import os
def merge_files(file_list, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in file_list:
            if os.path.exists(file_name):
                with open(file_name, 'r') as infile:
                    outfile.write(infile.read()) 
                    outfile.write("\n")  
            else:
                print(f"File {file_name} does not exist.")
    print(f"Files merged into {output_file}")


files_to_merge = ['file1.txt', 'file2.txt', 'file3.txt'] 
output_file = 'merged_file.txt'

merge_files(files_to_merge, output_file)

#splitting large file to smaller files based on size or line count
import os

def split_file(input_file, max_size=None, max_lines=None):
    with open(input_file, 'r') as infile:
        # Initialize variables for file splitting
        part_num = 1
        current_size = 0
        current_lines = 0
        
        # Create the first part file
        part_file = open(f"{input_file}_part{part_num}.txt", 'w')

        for line in infile:
            # Check if the file size limit is reached
            if max_size and current_size + len(line.encode('utf-8')) > max_size:
                part_file.close()
                part_num += 1
                current_size = 0
                part_file = open(f"{input_file}_part{part_num}.txt", 'w')

            # Check if the line count limit is reached
            if max_lines and current_lines >= max_lines:
                part_file.close()
                part_num += 1
                current_lines = 0
                part_file = open(f"{input_file}_part{part_num}.txt", 'w')

            # Write the line to the current part file
            part_file.write(line)
            current_size += len(line.encode('utf-8'))
            current_lines += 1
        
        # Close the last part file
        part_file.close()

    print(f"File {input_file} split into {part_num} parts.")

# Example usage
input_file = 'large_file.txt'  # Input large file
max_size = 1000  # Max file size in bytes (set None to use max_lines instead)
max_lines = 20  # Max lines per file (set None to use max_size instead)

split_file(input_file, max_size=max_size)  # You can also call with max_lines=max_lines if preferred

