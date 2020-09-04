#
# @lc app=leetcode id=759 lang=python3
#
# [759] Employee Free Time
#
# https://leetcode.com/problems/employee-free-time/description/
#
# algorithms
# Hard (65.95%)
# Likes:    573
# Dislikes: 45
# Total Accepted:    42.2K
# Total Submissions: 63.4K
# Testcase Example:  '[[[1,2],[5,6]],[[1,3]],[[4,10]]]'
#
# We are given a list schedule of employees, which represents the working time
# for each employee.
# 
# Each employee has a list of non-overlapping Intervals, and these intervals
# are in sorted order.
# 
# Return the list of finite intervals representing common, positive-length free
# time for all employees, also in sorted order.
# 
# (Even though we are representing Intervals in the form [x, y], the objects
# inside are Intervals, not lists or arrays. For example, schedule[0][0].start
# = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we
# wouldn't include intervals like [5, 5] in our answer, as they have zero
# length.
# 
# 
# Example 1:
# 
# 
# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation: There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
# 
# 
# Example 2:
# 
# 
# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= schedule.length , schedule[i].length <= 50
# 0 <= schedule[i].start < schedule[i].end <= 10^8
# 
# 
#

# @lc code=start
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Time  complexity: O(ClogC), where C is the number of intervals across all employees.
        # Space complexity: O(C)
        # OPEN, CLOSE = 0, 1

        # events = []
        # for emp in schedule:
        #     for iv in emp:
        #         events.append((iv.start, OPEN))
        #         events.append((iv.end, CLOSE))

        # events.sort()
        # ans, prev, bal = [], None, 0
        # for t, cmd in events:
        #     if bal == 0 and prev is not None:
        #         ans.append(Interval(prev, t))

        #     bal += 1 if cmd is OPEN else -1
        #     prev = t

        # return ans


        # Priority Queue
        # Time  complexity: O(ClogN), where N is the number of employees,
        # and C is the number of jobs across all employees.
        # Space complexity: O(N)
        ans = []
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(schedule)]
        heapq.heapify(pq)
        anchor = min(iv.start for emp in schedule for iv in emp)
        while pq:
            t, e_id, e_jx = heapq.heappop(pq)
            if anchor < t:
                ans.append(Interval(anchor, t))
            anchor = max(anchor, schedule[e_id][e_jx].end)
            if e_jx + 1 < len(schedule[e_id]):
                heapq.heappush(pq, (schedule[e_id][e_jx + 1].start, e_id, e_jx + 1))

        return ans
        
# @lc code=end

