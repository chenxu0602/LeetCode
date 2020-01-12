#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range
#
# https://leetcode.com/problems/smallest-range/description/
#
# algorithms
# Hard (48.15%)
# Likes:    725
# Dislikes: 20
# Total Accepted:    25.3K
# Total Submissions: 52.4K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in ascending order. Find the smallest
# range that includes at least one number from each of the k lists. 
# 
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c
# if b-a == d-c.
# 
# Example 1:
# 
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# 
# 
# 
# 
# Note:
# 
# The given list may contain duplicates, so ascending order means >= here.
# 1 k 
# ⁠-10^5 value of elements 
# For Java users, please note that the input type has been changed to
# List<List<Integer>>. And after you reset the code template, you'll see this
# point.
# 
# 
# 
#
import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)

        ans = -1e9, 1e9
        right = max(row[0] for row in nums)

        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                return ans

            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j + 1))
        

