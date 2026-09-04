#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = {'a','e','i','o','u'}
        w = []
        result = ""
        for ch in s:
            if ch.lower() in v:
                w.append(ch)

        for ch in s:
            if ch.lower() in v:
                result += w.pop()
            else:
                result += ch

        return result


# @lc code=end

