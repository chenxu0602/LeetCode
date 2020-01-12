#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (55.18%)
# Likes:    373
# Dislikes: 318
# Total Accepted:    143K
# Total Submissions: 259.1K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
# 
# Example 1:
# 
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
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
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        count = maxCount = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 0

        return max(count, maxCount)
        """

        """
        return max(map(lambda x: len(x), ''.join([str(num) for num in nums]).split('0')))
        """

        for i in range(1, len(nums)):
            if nums[i]:
                nums[i] += nums[i-1]
        return max(nums)

        

