#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#
# https://leetcode.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (51.49%)
# Likes:    503
# Dislikes: 154
# Total Accepted:    51.9K
# Total Submissions: 100.6K
# Testcase Example:  '["23:59","00:00"]'
#
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the
# minimum minutes difference between any two time points in the list. 
# 
# Example 1:
# 
# Input: ["23:59","00:00"]
# Output: 1
# 
# 
# 
# Note:
# 
# The number of time points in the given list is at least 2 and won't exceed
# 20000.
# The input time is legal and ranges from 00:00 to 23:59.
# 
# 
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        t.append(t[0] + 60 * 24)
        return min(b - a for a, b in zip(t, t[1:]))
        
# @lc code=end

