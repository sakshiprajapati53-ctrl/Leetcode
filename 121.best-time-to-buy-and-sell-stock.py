#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0 # profit 
        buy = prices[0] # first buy is first element of prices
        for sell in prices[1:]: # first element ko skip kar ke all elements
            if sell > buy: # profit hoga
                p = max(p,sell - buy)
            else: #loss hoga
                buy = sell

        return p
# @lc code=end

