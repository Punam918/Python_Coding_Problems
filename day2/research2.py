'''
Bytes String vs. Text String comparison

Here's a tabular comparison of Bytes Strings vs. Text Strings:

Aspect	Text String (str)	                                           Bytes String (bytes)
Definition	Sequence of Unicode characters (human-readable text).	Sequence of raw binary data (8-bit values).
Representation	Enclosed in quotes (', ", or triple quotes).	     Prefixed with b and enclosed in quotes (b"...").
Example	"Hello, World!"                                                    	b"Hello, World!"
Purpose	For handling textual data like names, sentences, etc.	For handling binary data like files, streams, or network packets.
Data Type	      str	bytes
Character Values	Unicode characters (e.g., H, e, l).	           Bytes (0–255) only (e.g., 72, 101, 108).
Encoding Needed?	No encoding needed; natively handles Unicode.	      Requires encoding to represent text.
Conversion	Can be encoded to bytes using .encode().	                     Can be decoded to str using .decode().
Encoding Example	"Hello".encode("utf-8") → b"Hello"	                    b"Hello".decode("utf-8") → "Hello"
Use Cases	Reading/writing text files, user inputs, UI elements.              	Binary files (e.g., images, videos), network protocols.
Mutability	Immutable (cannot be changed after creation).	                 Immutable (cannot be changed after creation).
Length Calculation	Counts characters (e.g., len("Hello") = 5).	             Counts bytes (e.g., len(b"Hello") = 5).

'''