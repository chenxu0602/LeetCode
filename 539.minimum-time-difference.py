#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#
# https://leetcode.com/problems/minimum-time-difference/description/
#
# algorithms
# Medium (48.31%)
# Likes:    258
# Dislikes: 88
# Total Accepted:    30.3K
# Total Submissions: 62.6K
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
from math import inf

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        for i, timePoint in enumerate(timePoints):
            hours, mins = timePoint.split(':')
            timeInMins = int(hours) * 60 + int(mins)
            timePoints[i] = timeInMins

        timePoints.sort()
        smallestDiff = inf

        for i in range(1, len(timePoints)):
            smallestDiff = min(smallestDiff, timePoints[i] - timePoints[i-1])

        smallestDiff = min(smallestDiff, 60 * 24 + timePoints[0] - timePoints[-1])

        return smallestDiff
        """

        t = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        t.append(t[0] + 1440)
        return min(b - a for a, b in zip(t, t[1:]))


        

