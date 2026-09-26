#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def house_rob(nums):
            first = 0
            second = 0

            for i in nums:
                ans = max(first, second + i)
                second = first
                first = ans

            return first

        case1 = house_rob(nums[:-1])  # first house included, last excluded
        case2 = house_rob(nums[1:])   # first house excluded, last included

        return max(case1, case2)
# @lc code=end

