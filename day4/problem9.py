'''
You had a conference call scheduled for December 21, 2012, at 9:30 a.m. in Chicago. At
 what local time did your friend in Bangalore, India, have to show up to attend?
'''
from datetime import datetime
import pytz

# Define time zones
chicago_tz = pytz.timezone('America/Chicago')
bangalore_tz = pytz.timezone('Asia/Kolkata')  

# Given time in Chicago (CST)
chicago_time = chicago_tz.localize(datetime(2012, 12, 21, 9, 30))

# Convert to Bangalore time (IST)
bangalore_time = chicago_time.astimezone(bangalore_tz)

# Print the result
print("Chicago Time (CST):", chicago_time.strftime('%Y-%m-%d %I:%M %p %Z'))
print("Bangalore Time (IST):", bangalore_time.strftime('%Y-%m-%d %I:%M %p %Z'))
