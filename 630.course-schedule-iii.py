#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#
# https://leetcode.com/problems/course-schedule-iii/description/
#
# algorithms
# Hard (32.83%)
# Likes:    569
# Dislikes: 27
# Total Accepted:    16.7K
# Total Submissions: 51K
# Testcase Example:  '[[100,200],[200,1300],[1000,1250],[2000,3200]]'
#
# There are n different online courses numbered from 1 to n. Each course has
# some duration(course length) t and closed on dth day. A course should be
# taken continuously for t days and must be finished before or on the dth day.
# You will start at the 1st day.
# 
# Given n online courses represented by pairs (t,d), your task is to find the
# maximal number of courses that can be taken.
# 
# Example:
# 
# 
# Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# Output: 3
# Explanation: 
# There're totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the
# 100th day, and ready to take the next course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the
# 1100th day, and ready to take the next course on the 1101st day. 
# Third, take the 2nd course, it costs 200 days so you will finish it on the
# 1300th day. 
# The 4th course cannot be taken now, since you will finish it on the 3300th
# day, which exceeds the closed date.
# 
# 
# 
# 
# Note:
# 
# 
# The integer 1 <= d, t, n <= 10,000.
# You can't take two courses simultaneously.
# 
# 
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Priority Queue
        # The iteration over the sorted coursescourses remains the same as in the last approaches. 
        # Whenver the current course_i can be taken(time + duration_i ≤ end_i), 
        # it is added to the queuequeue and the value of the current time is updated to time + duration_itime+duration_i.
        # If the current course can't be taken directly, as in the previous appraoches, 
        # we need to find a course whose duration duration_j is maximum from amongst the courses taken till now. Now, since we are maintaing a Max-Heap, queuequeue, we can obtain this duration directly from this queuequeue. 
        # If the duration duration_j > duration_i, we can replace the jth course, with the current one.
        # Time  complexity: O(nlogn)
        # Space complexity: O(n)

        pq, start = [], 0

        for t, end in sorted(courses, key=lambda x: x[1]):
            start += t
            heapq.heappush(pq, -t)
            while start > end:
                start += heapq.heappop(pq)

        return len(pq)

        
# @lc code=end

