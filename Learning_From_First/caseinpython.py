def check_day(day):
    match day:
        case "Monday":
            return "Start of the work week."
        case "Friday":
            return "Weekend is near!"
        case "Sunday":
            return "Relax, it's the weekend."
        case _:            # This is for default
            return "Just another day."

print(check_day("Friday"))  # Output: Weekend is near!
