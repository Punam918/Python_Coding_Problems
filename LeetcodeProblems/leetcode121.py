'''Stock Buy and Sell'''
#brute for ce
prices = [1,2,1,5,6,4,8]
maxp = 0 
def maxp(prices):
    n = len(prices)
    for i in range(0,n):
        for j in range(i+1,n):
            if prices[j]>prices[i]:
                p = prices[j] - prices[i]
                maxp = max(maxp,p)

    return maxp

''' Tc = o(n(n+1)/2) = o(n**2) sc = O(1)'''

#optimal
def maxp(prices):
    maxp = 0
    minprice = float('inf')
    n = len(prices)
    for i in range(0,n):
        minprice = min(minprice,prices[i])
        maxprofit = max(maxprofit,prices[i]-minprice)

    return maxp 
'''     
    TC = O(n)
    Sc = o(1)
'''