#
# @lc app=leetcode id=1353 lang=python3
#
# [1353] Maximum Number of Events That Can Be Attended
#
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/
#
# algorithms
# Medium (29.80%)
# Likes:    555
# Dislikes: 76
# Total Accepted:    15.7K
# Total Submissions: 52.9K
# Testcase Example:  '[[1,2],[2,3],[3,4]]'
#
# Given an array of events where events[i] = [startDayi, endDayi]. Every event
# i starts at startDayi and ends at endDayi.
# 
# You can attend an event i at any day d where startTimei <= d <= endTimei.
# Notice that you can only attend one event at any time d.
# 
# Return the maximum number of events you can attend.
# 
# 
# Example 1:
# 
# 
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
# 
# 
# Example 2:
# 
# 
# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: events = [[1,100000]]
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# 1 <= events.length <= 10^5
# events[i].length == 2
# 1 <= startDayi <= endDayi <= 10^5
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # events.sort(key=lambda x: (x[1], x[0]))
        # days = set()
        # for s, e in events:
        #     for d in range(s, e + 1):
        #         if d not in days:
        #             days.add(d)
        #             break
        # return len(days)


        # O(nlogn)
        events.sort(reverse=True)
        h = []
        res = d = 0

        while events or h:
            if not h:
                d = events[-1][0]
            while events and events[-1][0] <= d:
                heapq.heappush(h, events.pop()[1])
            heapq.heappop(h)

            res += 1; d += 1
            while h and h[0] < d:
                heapq.heappop(h)

        return res
        
# @lc code=end

