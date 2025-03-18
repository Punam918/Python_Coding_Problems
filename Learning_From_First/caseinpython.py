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

# while loop
counter = 1
while counter <= 5:
    print(counter)
    counter += 1  # increment the counter to avoid infinite loop


# Post-increment (a++): Uses the value before incrementing.
# Post-decrement (a--): Uses the value before decrementing.
# Pre-increment (++a): Increments the value before using it.
# Pre-decrement (--a): Decrements the value before using it.






