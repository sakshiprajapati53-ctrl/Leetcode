#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        result.append([1])
        for i in range(numRows-1):
            row = [1]
            for j in range(i):
                row.append(result[i][j] + result[i][j+1])
            row.append(1)
            result.append(row)
        
        return result
# @lc code=end

