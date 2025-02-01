'''
 You want a general solution for finding a date for the last occurrence of a day of the
 week. Last Friday, for example
 
'''
from datetime import datetime, timedelta

def last_weekday(weekday, reference_date=None):
    """
    Find the date of the last occurrence of a given weekday.
    
    Parameters:
    - weekday (int): The day of the week (0=Monday, 6=Sunday).
    - reference_date (datetime, optional): The date to calculate from (default: today).
    
    Returns:
    - datetime: The last occurrence of the specified weekday.
    """
    if reference_date is None:
        reference_date = datetime.today()
    
    days_ago = (reference_date.weekday() - weekday) % 7
    if days_ago == 0:  # If today is the target weekday, go back one week
        days_ago = 7
    
    return reference_date - timedelta(days=days_ago)

# Example Usage
last_friday = last_weekday(4)  # 4 = Friday (Monday=0, ..., Sunday=6)
print(f"Last Friday was on: {last_friday.strftime('%Y-%m-%d')}")
