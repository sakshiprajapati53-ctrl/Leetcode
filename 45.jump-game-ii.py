#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        reach,count,last = 0,0,0 # last ,count ,last idex initilization 
        for i in range(len(nums)-1):
            # update reach if we found max number b/w i + nums[i]
            reach = max(reach,i + nums[i])

        # if i rech last then last idx == reach idx and count will increase
            if i == last:
                last = reach 
                # increment the number of jumps made so far
                count +=1
        # return the min no. of jumps required
        return count
# @lc code=end

