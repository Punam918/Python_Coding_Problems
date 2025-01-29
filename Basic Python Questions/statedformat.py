
# **Given strings**:
# ```
# "Data" "Science" "Mentorship" "Program"
# "By" "CampusX"
# ```
# **Output**:
# ```
# Data-Science-Mentorship-Program-started-By-CampusX
# ```

s1 = 'Data Science Mentorship Program by campusx'
s2 = s1.split()
s3 = '-'.join(s2)
print(s3)
