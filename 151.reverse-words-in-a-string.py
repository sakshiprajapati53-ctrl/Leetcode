#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split() # split the word 
        nword = []

        for i in range(len(w)): 
            nword.append(w[len(w) - 1 - i]) # push w into nword until len of w-1-i

        result = " ".join(nword) # then join nword into result
        return result
            
# @lc code=end

