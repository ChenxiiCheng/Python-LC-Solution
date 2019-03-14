'''
Question: 
  121. Best Time to Buy and Sell Stock

Descrition: 
  Say you have an array for which the ith element is the price of a given stock on day i.
  If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
  design an algorithm to find the maximum profit. Note that you cannot sell a stock before you buy one.

Examples:

  Input: [7,1,5,3,6,4]
  Output: 5
  Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
'''

#Python3 Code:

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Solution 2
        if not prices:
            return 0
        min_price, max_profit = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit
        
        
        #Solution
        if not prices:
            return 0
        buy = prices[0]
        sale = profit = 0
        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price > buy:
                sale = price
                profit = max(profit, sale - buy)
        return profit

        