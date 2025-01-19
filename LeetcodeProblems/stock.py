def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0  # No profit can be made
    
    min_price = float('inf')  # Initialize the minimum price as infinity
    max_profit = 0  # Initialize the maximum profit as 0
    
    for price in prices:
        # Update the minimum price seen so far
        if price < min_price:
            min_price = price
        # Calculate profit and update the maximum profit
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
