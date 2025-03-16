'''
https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/


in tabular form find the difference of  3. Performance Comparison of f-string formatting and % formatting.
ChatGPT said:
ChatGPT
Here’s a tabular comparison of the performance of f-string formatting and % formatting in Python:

Feature	f-string Formatting (f"{var}")	             % Formatting ("%s" % var)
Performance	Faster due to direct evaluation	               Slower as it uses tuple packing/unpacking
Readability	More readable and concise	                     Less readable, especially for multiple variables
Flexibility	Supports expressions inside {}	                  Limited to simple variable substitution
Usage with Objects	Supports direct method calls within {}	     Requires explicit conversion using str()
Introduced In	Python 3.6	Python 2 and Python 3                           
Memory Efficiency	More efficient, avoids extra function calls          	Less efficient due to intermediate processing
Preferred For	Modern Python applications	                        Legacy code compatibility
Performance Benchmark (Time Complexity)
Using the timeit module:

python
Copy
Edit
import timeit

name = "Alice"
n = 1000000  # 1 million iterations

fstring_time = timeit.timeit(lambda: f"Hello, {name}!", number=n)
percent_time = timeit.timeit(lambda: "Hello, %s!" % name, number=n)

print(f"f-string time: {fstring_time:.6f} sec")
print(f"% formatting time: {percent_time:.6f} sec")
Expected Result:

f-string is generally faster than % formatting because it avoids tuple packing and function calls.
Would you like a performance comparison including .format() as well? 🚀













ChatGPT can 

'''