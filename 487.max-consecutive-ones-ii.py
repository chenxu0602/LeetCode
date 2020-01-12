#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
#
# algorithms
# Medium (46.75%)
# Likes:    385
# Dislikes: 6
# Total Accepted:    26.6K
# Total Submissions: 56.9K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 
# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0.
# 
# 
# Example 1:
# 
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of
# consecutive 1s.
# ⁠   After flipping, the maximum number of consecutive 1s is 4.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
# 
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other
# words, you can't store all numbers coming from the stream as it's too large
# to hold in memory. Could you solve it efficiently?
# 
#
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev, curr, maxlen = -1, 0, 0
        for i in nums:
            if i == 0:
                prev, curr = curr, 0
            else:
                curr += 1

            maxlen = max(maxlen, prev + 1 + curr)

        return maxlen
        

