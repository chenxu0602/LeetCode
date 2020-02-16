#
# @lc app=leetcode id=1272 lang=python3
#
# [1272] Remove Interval
#
# https://leetcode.com/problems/remove-interval/description/
#
# algorithms
# Medium (56.01%)
# Likes:    58
# Dislikes: 5
# Total Accepted:    3.4K
# Total Submissions: 6.1K
# Testcase Example:  '[[0,2],[3,4],[5,7]]\n[1,6]'
#
# Given a sorted list of disjoint intervals, each interval intervals[i] = [a,
# b] represents the set of real numbers x such that a <= x < b.
# 
# We remove the intersections between any interval in intervals and the
# interval toBeRemoved.
# 
# Return a sorted list of intervals after all such removals.
# 
# 
# Example 1:
# Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
# Output: [[0,1],[6,7]]
# Example 2:
# Input: intervals = [[0,5]], toBeRemoved = [2,3]
# Output: [[0,2],[3,5]]
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# -10^9 <= intervals[i][0] < intervals[i][1] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        A, B = toBeRemoved
        return [[x, y] for a, b in intervals for x, y in ((a, min(b, A)), (max(a, B), b)) if x < y]
        
# @lc code=end

