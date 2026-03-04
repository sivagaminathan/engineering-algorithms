"""
LC 121 - Best Time to Buy and Sell Stock
Difficulty: Easy
Pattern: Prefix Minimum / Greedy
Time: O(n)
Space: O(1)

Solved on: 2026-03-04
Re-solved on:
Notes:
"""

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        min_price = float('inf') # Set min price to infinity 

        for price in prices: 
            if min_price > price:
                min_price = price
            else:
                profit = price - min_price 
                max_profit = max(max_profit, profit)
        return max_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))  # Expected: 5