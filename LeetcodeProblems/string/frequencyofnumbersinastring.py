# Frequency of Numbers in String – Python
import re
s = "geeks4feeks is No. 1 4 geeks"
res = len(re.findall(r'\d+', s))
print("Count of numerics in string:", res)