#
# @lc app=leetcode id=1133 lang=python3
#
# [1133] Largest Unique Number
#
# https://leetcode.com/problems/largest-unique-number/description/
#
# algorithms
# Easy (69.69%)
# Likes:    27
# Dislikes: 1
# Total Accepted:    4.4K
# Total Submissions: 6.6K
# Testcase Example:  '[5,7,3,9,4,9,8,3,1]'
#
# Given an array of integers A, return the largest integer that only occurs
# once.
# 
# If no integer occurs once, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: 
# The maximum integer in the array is 9 but it is repeated. The number 8 occurs
# only once, so it's the answer.
# 
# 
# Example 2:
# 
# 
# Input: [9,9,8,8]
# Output: -1
# Explanation: 
# There is no number that occurs only once.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 2000
# 0 <= A[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:

        unique_A = set()
        duplicates_A = set()

        if not A:
            return -1


        for a in A:
            if a in duplicates_A:
                continue

            if a in unique_A:
                duplicates_A.add(a)
                unique_A.remove(a)
            else:
                unique_A.add(a)

        if not unique_A:
            return -1
        else:
            return max(unique_A)

        
# @lc code=end

