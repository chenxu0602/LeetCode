#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (31.61%)
# Likes:    1056
# Dislikes: 134
# Total Accepted:    200.2K
# Total Submissions: 627K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
from bisect import bisect_left, bisect_right

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        starts = [x[0] for x in intervals]
        ends = [x[1] for x in intervals]

        left_idx = bisect_left(ends, newInterval[0])
        right_idx = bisect_right(starts, newInterval[1])

        intervals3 = intervals[left_idx:right_idx] + [newInterval]
        intervals3.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals3:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])


        return intervals[:left_idx] + merged + intervals[right_idx:]            


        
# @lc code=end

