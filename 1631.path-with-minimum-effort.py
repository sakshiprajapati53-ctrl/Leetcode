#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        n = len(heights)
        m = len(heights[0])

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while pq:
            effort, r, c = heapq.heappop(pq)
            if r == n - 1 and c == m - 1:
                return effort

            if effort > dist[r][c]:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(effort, diff)

                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(pq,(new_effort, nr, nc))

        return 0
# @lc code=end

