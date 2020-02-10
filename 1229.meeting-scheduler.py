#
# @lc app=leetcode id=1229 lang=python3
#
# [1229] Meeting Scheduler
#
# https://leetcode.com/problems/meeting-scheduler/description/
#
# algorithms
# Medium (44.44%)
# Likes:    70
# Dislikes: 6
# Total Accepted:    4.3K
# Total Submissions: 9.7K
# Testcase Example:  '[[10,50],[60,120],[140,210]]\n[[0,15],[60,70]]\n8'
#
# Given the availability time slots arrays slots1 and slots2 of two people and
# a meeting duration duration, return the earliest time slot that works for
# both of them and is of duration duration.
# 
# If there is no common time slot that satisfies the requirements, return an
# empty array.
# 
# The format of a time slot is an array of two elements [start, end]
# representing an inclusive time range from start to end.  
# 
# It is guaranteed that no two availability slots of the same person intersect
# with each other. That is, for any two time slots [start1, end1] and [start2,
# end2] of the same person, either start1 > end2 or start2 > end1.
# 
# 
# Example 1:
# 
# 
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]],
# duration = 8
# Output: [60,68]
# 
# 
# Example 2:
# 
# 
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]],
# duration = 12
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= slots1.length, slots2.length <= 10^4
# slots1[i].length, slots2[i].length == 2
# slots1[i][0] < slots1[i][1]
# slots2[i][0] < slots2[i][1]
# 0 <= slots1[i][j], slots2[i][j] <= 10^9
# 1 <= duration <= 10^6 
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        s = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
        heapq.heapify(s)
        while len(s) > 1:
            if heapq.heappop(s)[1] >= s[0][0] + duration:
                return [s[0][0], s[0][0] + duration]
        return []
        
# @lc code=end

