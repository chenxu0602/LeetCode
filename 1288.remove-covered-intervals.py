#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#
# https://leetcode.com/problems/remove-covered-intervals/description/
#
# algorithms
# Medium (61.17%)
# Likes:    93
# Dislikes: 7
# Total Accepted:    5.4K
# Total Submissions: 8.9K
# Testcase Example:  '[[1,4],[3,6],[2,8]]'
#
# Given a list of intervals, remove all intervals that are covered by another
# interval in the list. Interval [a,b) is covered by interval [c,d) if and only
# if c <= a and b <= d.
# 
# After doing so, return the number of remaining intervals.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 1000
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# intervals[i] != intervals[j] for all i != j
# 
# 
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy
        # O(NlogN)
        res = right = 0
        for i, j in sorted(intervals, key=lambda a: [a[0], -a[1]]):
            res += j > right
            right = max(right, j)
        return res
        
# @lc code=end

