# Problem Statement: Best Time to Buy and Sell Stock
# You are given an integer array prices, where prices[i] represents the price of a stock on the iᵗʰ day.
# You are allowed to complete at most one transaction, which means:
# Choose one day to buy the stock
# Choose a different future day to sell the stock
# Your objective is to maximize the profit from this single transaction. 
# If no profitable transaction is possible, return 0.
########################## Rules ##########################
# You must buy before you sell
# Only one buy and one sell operation is allowed
# If prices always decrease, no transaction should be performed
# 
# Input
# An array prices of length n
# prices[i] is the stock price on day i

# Output
# An integer representing the maximum profit
# Return 0 if no profit can be achieved
#
###############################################################################
# Examples
# Example 1
# Input:  prices = [7,1,5,3,6,4]
# Output: 5
# Explanation:
# Buy on day 2 at price 1 and sell on day 5 at price 6.
# Profit = 6 − 1 = 5

# Example 2
# Input:  prices = [7,6,4,3,1]
# Output: 0
# Explanation:
# Stock prices keep decreasing, so no profitable transaction is possible.
# ##############################################################################
# 
# Task
# Write a program or function that determines the maximum profit achievable from
# a single buy-sell transaction using the given price array.

def Stock_Trade(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
        
    return max_profit

print(Stock_Trade([7,1,5,3,6,4]))
print(Stock_Trade([7,6,4,3,1]))