#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

 # graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Graph + indegree
        for pre in prerequisites:
            a = pre[0] # course 
            b = pre[1] # prerequisites
            # b--->a [b ke baad a]
            graph[b].append(a)
    # indegree -->Kisi node ke andar kitne arrows aa rahe hain.
    #Example:
    # 0 → 1
    # Course 1 ke andar 1 arrow aa raha hai:
    # indegree[1] = 1
    # Course 0 ke andar koi arrow nahi:
    # indegree[0] = 0
            # arrow (a) me ja raha hai
            # indegree of course increase hoga
            indegree[a] += 1

             # Courses with no prerequisite
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0: 
            # Indegree 0 ka matlab?
            # is course ko start karne ke liye koi prerequisite 
            # pending nahi hai.
                q.append(i)

        count = 0

        # BFS / Kahn's Algorithm
        while q:
            node = q.popleft()
            count += 1

            for neighbour in graph[node]:
                indegree[neighbour] -= 1 # prerequsite kam hota jaye ga

                if indegree[neighbour] == 0:
                    q.append(neighbour) 

        return count == numCourses

# @lc code=end

