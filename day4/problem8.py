'''
. Your application receives temporal data in string format, but you want to convert those
 strings into datetime objects in order to perform nonstring operations on them
'''
from datetime import datetime


date_str = "2025-01-30 14:45:00"

# Convert string to datetime object
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")


print(date_obj)  
print(type(date_obj)) 
