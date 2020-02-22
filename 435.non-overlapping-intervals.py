#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (42.22%)
# Likes:    773
# Dislikes: 28
# Total Accepted:    58.1K
# Total Submissions: 137.7K
# Testcase Example:  '[[1,2]]'
#
# Given a collection of intervals, find the minimum number of intervals you
# need to remove to make the rest of the intervals non-overlapping.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are
# non-overlapping.
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals
# non-overlapping.
# 
# 
# Example 3:
# 
# 
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
# 
# 
# 
# 
# Note:
# 
# 
# You may assume the interval's end point is always bigger than its start
# point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap
# each other.
# 
# 
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort()
        # res = lo = 0
        # for hi in range(1, len(intervals)):
        #     if intervals[lo][1] > intervals[hi][0]:
        #         res += 1
        #     if not intervals[hi][0] < intervals[lo][1] < intervals[hi][1]:
        #         lo = hi
        # return res

        if not len(intervals) > 0: return 0
        intervals.sort(key=lambda x: x[1])
        end, count = float("-inf"), 0
        for i in range(len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1

        return len(intervals) - count

        
# @lc code=end

