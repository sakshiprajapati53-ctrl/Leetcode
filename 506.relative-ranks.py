#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_score = sorted(score, reverse=True) # sort the score list 

        rank = {} # empty list for storing the rank

        for i in range(len(sort_score)):
            if i == 0:
                rank[sort_score[i]] = "Gold Medal"
            elif i == 1:
                rank[sort_score[i]] = "Silver Medal"
            elif i == 2:
                rank[sort_score[i]] = "Bronze Medal"
            else:
                rank[sort_score[i]] = str(i + 1) # if i = 3 ,"3"+1 = 4 rank etc.

        return [rank[x] for x in score] # return rank of scores present in list


# @lc code=end

