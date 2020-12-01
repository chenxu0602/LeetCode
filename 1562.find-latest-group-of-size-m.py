#
# @lc app=leetcode id=1562 lang=python3
#
# [1562] Find Latest Group of Size M
#
# https://leetcode.com/problems/find-latest-group-of-size-m/description/
#
# algorithms
# Medium (38.96%)
# Likes:    272
# Dislikes: 63
# Total Accepted:    8.4K
# Total Submissions: 21.6K
# Testcase Example:  '[3,5,1,2,4]\n1'
#
# Given an array arr that represents a permutation of numbers from 1 to n. You
# have a binary string of size n that initially has all its bits set to zero.
# 
# At each step i (assuming both the binary string and arr are 1-indexed) from 1
# to n, the bit at position arr[i] is set to 1. You are given an integer m and
# you need to find the latest step at which there exists a group of ones of
# length m. A group of ones is a contiguous substring of 1s such that it cannot
# be extended in either direction.
# 
# Return the latest step at which there exists a group of ones of length
# exactly m. If no such group exists, return -1.
# 
# 
# Example 1:
# 
# 
# Input: arr = [3,5,1,2,4], m = 1
# Output: 4
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "00101", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "11101", groups: ["111", "1"]
# Step 5: "11111", groups: ["11111"]
# The latest step at which there exists a group of size 1 is step 4.
# 
# Example 2:
# 
# 
# Input: arr = [3,1,5,4,2], m = 2
# Output: -1
# Explanation:
# Step 1: "00100", groups: ["1"]
# Step 2: "10100", groups: ["1", "1"]
# Step 3: "10101", groups: ["1", "1", "1"]
# Step 4: "10111", groups: ["1", "111"]
# Step 5: "11111", groups: ["11111"]
# No group of size 2 exists during any step.
# 
# 
# Example 3:
# 
# 
# Input: arr = [1], m = 1
# Output: 1
# 
# 
# Example 4:
# 
# 
# Input: arr = [2,1], m = 2
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# n == arr.length
# 1 <= n <= 10^5
# 1 <= arr[i] <= n
# All integers in arr are distinct.
# 1 <= m <= arr.length
# 
# 
#

# @lc code=start
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # Note that the length value is updated on the leftmost and the rightmost bit of the group.
        # The length value inside the group may be out dated.
        # O(N)
        if m == len(arr): return m
        length = [0] * (len(arr) + 2)
        res = -1
        for i, v in enumerate(arr):
            left, right = length[v - 1], length[v + 1]
            if left == m or right == m:
                res = i
            length[v - left] = length[v + right] = left + right + 1
        return res
        
# @lc code=end

