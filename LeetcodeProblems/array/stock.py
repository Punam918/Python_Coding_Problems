def max_profit(prices):
    l, r = 0, 1  # l = left pointer (buy day), r = right pointer (sell day)
    maxp = 0  # Initialize max profit as 0
    
    while r < len(prices):  # Loop until the right pointer reaches the end
        if prices[r] > prices[l]:  # Check if selling today gives a profit
            profit = prices[r] - prices[l]
            maxp = max(maxp, profit)  # Update max profit if current profit is greater
        else:
            l = r  # Update left pointer to the right pointer if no profit
        r += 1  # Move the right pointer to the next day
    
    return maxp

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
