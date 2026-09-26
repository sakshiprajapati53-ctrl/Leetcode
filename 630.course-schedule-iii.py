#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#

# @lc code=start
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Deadline ke according sort
        courses.sort(key=lambda x: x[1]) # Har element x lo aur uska index 1 return karo."
        time = 0
        max_heap = [] # store selected courses ki duration
        for duration,lastDay in courses:
            time += duration
            # Python heapq min-heap hai
            # -duration use karke max-heap bana rahe hain
            heapq.heappush(max_heap, -duration)

            # Deadline cross ho gayi
            if time > lastDay:
                # Sabse bada duration remove karo
                longest = -heapq.heappop(max_heap)
                time -= longest

        return len(max_heap)
            

 
# @lc code=end

