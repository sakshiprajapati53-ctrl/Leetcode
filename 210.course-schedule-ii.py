#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Graph + indegree
        for pre in prerequisites:
            a = pre[0]
            b = pre[1]

            # b ---> a
            graph[b].append(a)

            # a ki indegree increase
            indegree[a] += 1

        # Indegree 0 courses
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        result = []

        # BFS / Kahn's Algorithm
        while q:

            node = q.popleft()

            # Course ko result mein add karo
            result.append(node)

            # Neighbours
            for neighbour in graph[node]:

                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    q.append(neighbour)

        # Cycle check
        if len(result) == numCourses:
            return result

        return []     
# @lc code=end

