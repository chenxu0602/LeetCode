#
# @lc app=leetcode id=2398 lang=python3
#
# [2398] Maximum Number of Robots Within Budget
#

# @lc code=start
from sortedcontainers import SortedList
from collections import deque
import heapq

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        """
        # Time  complexity: O(nlogn)
        # Space complexity: O(n)
        cur = i = 0
        n = len(chargeTimes)
        s = SortedList()
        for j in range(n):
            cur += runningCosts[j]
            s.add(chargeTimes[j])
            if s[-1] + (j - i + 1) * cur > budget:
                s.remove(chargeTimes[i])
                cur -= runningCosts[i]
                i += 1
        return n - i
        """

        # Time  complexity: O(n)
        # Space complexity: O(n)
        cur = i = 0
        n = len(chargeTimes)
        d = deque()
        for j in range(n):
            cur += runningCosts[j]
            while d and chargeTimes[d[-1]] <= chargeTimes[j]:
                d.pop()
            d.append(j)

            if chargeTimes[d[0]] + (j - i + 1) * cur > budget:
                if d[0] == i:
                    d.popleft()
                cur -= runningCosts[i]
                i += 1
        return n - i

        """
        def remove_stale(pq, j):
            while pq and pq[0][1] <= j: 
                heapq.heappop(pq)
            return -pq[0][0] if pq else 0

        ans, s, j, pq = 0, 0, -1, []
        for i in range(len(runningCosts)):
            s += runningCosts[i]
            heapq.heappush(pq, (-chargeTimes[i], i))
            while s * (i - j) + remove_stale(pq, j) > budget:
                j += 1
                s -= runningCosts[j]

            ans = max(ans, i - j)
        return ans
        """


        
# @lc code=end

