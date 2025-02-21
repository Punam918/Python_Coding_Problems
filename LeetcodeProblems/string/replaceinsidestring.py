s = "14, 625, 498.002"

# Replace commas with a temporary character
s = s.replace(',', '#')

# # Replace dots with commas
s = s.replace('.', ',')

# # Replace the temporary character with dots
s = s.replace('#', '.')
print(s)