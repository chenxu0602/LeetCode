#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#
# https://leetcode.com/problems/wiggle-subsequence/description/
#
# algorithms
# Medium (37.47%)
# Likes:    541
# Dislikes: 47
# Total Accepted:    48.7K
# Total Submissions: 129.6K
# Testcase Example:  '[1,7,4,9,2,5]'
#
# A sequence of numbers is called a wiggle sequence if the differences between
# successive numbers strictly alternate between positive and negative. The
# first difference (if one exists) may be either positive or negative. A
# sequence with fewer than two elements is trivially a wiggle sequence.
# 
# For example, [1,7,4,9,2,5] is a wiggle sequence because the differences
# (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5]
# and [1,7,4,5,5] are not wiggle sequences, the first because its first two
# differences are positive and the second because its last difference is zero.
# 
# Given a sequence of integers, return the length of the longest subsequence
# that is a wiggle sequence. A subsequence is obtained by deleting some number
# of elements (eventually, also zero) from the original sequence, leaving the
# remaining elements in their original order.
# 
# Example 1:
# 
# 
# Input: [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.
# 
# 
# Example 2:
# 
# 
# Input: [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is
# [1,17,10,13,10,16,8].
# 
# 
# Example 3:
# 
# 
# Input: [1,2,3,4,5,6,7,8,9]
# Output: 2
# 
# Follow up:
# Can you do it in O(n) time?
# 
# 
# 
#
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        nan = float("nan")
        diffs = [a - b for a, b in zip([nan] + nums, nums + [nan]) if a - b]
        return sum(not d * e >= 0 for d, e in zip(diffs, diffs[1:]))
        """

        """
        n = len(nums)
        if n < 2: 
            return n

        up, down = [0] * n, [0] * n
        up[0] = down[0] = 1

        for i in range(1, n):
            if nums[i] - nums[i-1] > 0:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] - nums[i-1] < 0:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        
        return max(up[n-1], down[n-1])
        """

        n = len(nums)
        if n < 2:
            return n

        down = up = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(down, up)



