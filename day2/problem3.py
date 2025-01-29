import re

text = """/* this is a
multiline comment */
"""

# Regular expression pattern using re.DOTALL
pattern = r"/\*.*?\*/"

match = re.search(pattern, text, re.DOTALL)

if match:
    print("Matched text:", match.group())
else:
    print("No match found.")
