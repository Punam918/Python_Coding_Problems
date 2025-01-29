# Program to calculate simple interest

# Get user input for principal, rate of interest, and time period
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time_period = float(input("Enter the time period in years: "))

# Calculate simple interest
simple_interest = (principal * rate_of_interest * time_period) / 100

# Display the result
print(f"The simple interest is: {simple_interest} Rs")