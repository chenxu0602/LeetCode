#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
#
# algorithms
# Medium (40.90%)
# Likes:    562
# Dislikes: 238
# Total Accepted:    22.2K
# Total Submissions: 54K
# Testcase Example:  '[1,2,3,3,4,5]'
#
# Given an array nums sorted in ascending order, return true if and only if you
# can split it into 1 or more subsequences such that each subsequence consists
# of consecutive integers and has length at least 3.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,2,3,4,4,5]
# Output: False
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10000
# 
# 
# 
# 
#
from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:


        """
        count[i] counts the number of i that hasn't been placed yet.
        tails[i] counts the number of consecutive subsequences that ends at number i
        """

        count = Counter(nums)
        tails = Counter()

        for x in nums:
            if count[x] == 0:
                continue 
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False

            count[x] -= 1

        return True

        

