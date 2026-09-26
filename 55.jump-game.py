#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g = 0
        for i in nums:
            if g < 0:
                return False
            elif i > g: # i greater the gas then gas=i and we will decrease gas until it become '0'
                g = i
            g -= 1

        return True
        # here i had take an eg. of car gasoline 
        # n1 --> n2 --> n3 --> n4 --> n5
        #    dist cover and gasoline decrease , after reaching new destination gasoline amount increase , this increment and decrement will done until gas < 0
# @lc code=end

