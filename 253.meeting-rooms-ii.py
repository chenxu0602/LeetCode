#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (44.59%)
# Likes:    2124
# Dislikes: 31
# Total Accepted:    235.5K
# Total Submissions: 528K
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
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # Priority Queues
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        # if not intervals:
        #     return 0

        # free_rooms = []

        # intervals.sort(key=lambda x: x[0])

        # heapq.heappush(free_rooms, intervals[0][1])

        # for i in intervals[1:]:
        #     # If the room due to free up the earliest is free, assign that room to this meeting.
        #     if free_rooms[0] <= i[0]:
        #         heapq.heappop(free_rooms)

        #     # If a new room is to be assigned, then also we add to the heap,
        #     # If an old room is allocated, then also we have to add to the heap with updated end time.
        #     heapq.heappush(free_rooms, i[1])

        # # The size of the heap tells us the minimum rooms required for all the meetings.
        # return len(free_rooms)


        # Chronological Ordering
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])
        L = len(intervals)

        end_pointer = 0
        start_pointer = 0

        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1
            start_pointer += 1

        return used_rooms

        
# @lc code=end

