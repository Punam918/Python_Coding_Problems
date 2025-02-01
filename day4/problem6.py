def days_to_seconds(days):
    return days * 86400  # 1 day = 86400 seconds

def hours_to_minutes(hours):
    return hours * 60  # 1 hour = 60 minutes

def minutes_to_seconds(minutes):
    return minutes * 60  # 1 minute = 60 seconds

def seconds_to_minutes(seconds):
    return seconds / 60  # Convert seconds to minutes

def hours_to_seconds(hours):
    return hours * 3600  # 1 hour = 3600 seconds

def weeks_to_days(weeks):
    return weeks * 7  # 1 week = 7 days

def months_to_days(months):
    return months * 30  # Approximate (assuming 30 days per month)

def years_to_days(years):
    return years * 365  # Approximate (assuming 365 days per year)

# Example Usage
print(f"2 days in seconds: {days_to_seconds(2)}")
print(f"3 hours in minutes: {hours_to_minutes(3)}")
print(f"5 minutes in seconds: {minutes_to_seconds(5)}")
print(f"120 seconds in minutes: {seconds_to_minutes(120)}")
print(f"4 weeks in days: {weeks_to_days(4)}")
