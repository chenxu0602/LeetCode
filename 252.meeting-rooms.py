#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#
# https://leetcode.com/problems/meeting-rooms/description/
#
# algorithms
# Easy (52.53%)
# Likes:    385
# Dislikes: 27
# Total Accepted:    101.8K
# Total Submissions: 191.6K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all
# meetings.
# 
# Example 1:
# 
# 
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# 
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: true
# 
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        return all([intervals[i][0] >= intervals[i-1][1] for i in range(1, len(intervals))])
        
# @lc code=end

