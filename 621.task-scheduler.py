#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Frequency of each task
        count = [0] * 26 # size 26 freq 0
        for ch in tasks:
            count[ord(ch) - ord('A')] += 1 # update frequency
        pq = []  # Max heap

        for freq in count: # count the freq in count 26 tak
            if freq > 0: # freq > 0 then 
                heapq.heappush(pq, -freq) # push in pq and freq--

        time = 0

        while pq: # until pq is not empty
            temp = []
            # One cycle is n + 1 means ek baar me we can take n+1 tasks 
            for _ in range(n + 1): 
                if pq:
                    freq = -heapq.heappop(pq) # pop the top element of pq
                    freq -= 1 # decrease frequency
                    if freq > 0: # agar freq is >0 then push into temp
                        temp.append(freq)

                time += 1 # and time ko increase karo
                # No tasks left and no remaining tasks
                if not pq and not temp: 
                    break

            # Put remaining tasks back into heap
            for freq in temp: #
                heapq.heappush(pq, -freq)

        return time
    # pending to understand 
# @lc code=end55

