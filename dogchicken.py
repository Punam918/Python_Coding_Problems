def solve(heads, legs):
    # Check for invalid inputs
    if legs % 2 != 0 or heads > legs or heads < 0 or legs < 0:
        return "Invalid input"

    # Calculate number of chickens and dogs
    chickens = (2 * heads - legs // 2)
    dogs = heads - chickens

    # Check for negative values
    if chickens < 0 or dogs < 0:
        return "Invalid input"

    return f"dogs -> {dogs}, chicken -> {chickens}"

# Example usage
heads = int(input("Enter the number of heads: "))
legs = int(input("Enter the number of legs: "))
result = solve(heads, legs)
print(result)