''' 1. You need to check the start or end of a string for specific text patterns, such as filename
 extensions, URL schemes, and so on.
 Eg: [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h', 'http://www.python.org']'''
 
 
# List of strings
files_and_urls = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h', 'http://www.python.org']

# Patterns to check
file_extensions = ('.c', '.py', '.h')  # File extensions
url_schemes = ('http://', 'https://')  # URL schemes
special_files = ('Makefile',)  # Special files

# Check for specific patterns
print("Files with specific extensions:")
for item in files_and_urls:
    if item.endswith(file_extensions):
        print(f"  - {item}")

print("\nItems with specific URL schemes:")
for item in files_and_urls:
    if item.startswith(url_schemes):
        print(f"  - {item}")

print("\nSpecial files (e.g., Makefile):")
for item in files_and_urls:
    if item in special_files:
        print(f"  - {item}")
