#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))  # ["3", "30", "34", "5", "9"]
        nums.sort(key=lambda x: x * 10, reverse=True) # ["9", "5", "34", "3", "30"]
        ans = ""
        for x in nums:
            ans += x
        return "0" if ans[0] == "0" else ans  # "9534330"

        # 2nd method

   #     from functools import cmp_to_key
   #     def compare(a, b):
   #         if a + b > b + a: [ if adding of 2 string is grater then return 1]
  #             return -1
  #          else:
 #              return 1
 #       nums.sort(key=cmp_to_key(compare))
 #       ans = "".join(nums)
#        return "0" if ans[0] == "0" else ans
  
# @lc code=end

