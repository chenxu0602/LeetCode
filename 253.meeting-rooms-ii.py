#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (43.34%)
# Likes:    1769
# Dislikes: 29
# Total Accepted:    197.7K
# Total Submissions: 450.5K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
# 
# Example 1:
# 
# 
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: 1
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
from heapq import heapify, heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        """
        if not intervals:
            return 0

        free_rooms = []

        intervals.sort(key=lambda x: x[0])

        heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heappop(free_rooms)

            heappush(free_rooms, i[1])

        return len(free_rooms)
        """

        if not intervals:
            return 0

        used_rooms = 0

        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])
        L = len(intervals)

        start_pointer, end_pointer = 0, 0

        while start_pointer < L:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1

            used_rooms += 1
            start_pointer += 1

        return used_rooms


        
# @lc code=end

