#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
            #stck empty! and k > 0    # last digit > curr digits
                stack.pop() #stack se pop kar do largest num
                k -= 1 # k -- hoga 

            stack.append(digit) #stack me current digit aye ga
        # Agar k abhi bhi bacha hai
        while k > 0: # agar k > 0 tab pehle val pop kar do  
            stack.pop() 
            k -= 1 # k-- kar do 
        # Leading zeros remove
        ans = "".join(stack).lstrip("0") # lstrip --> String ke starting (left side) ke saare 0 hata do.
        return ans if ans else "0"
# @lc code=end

