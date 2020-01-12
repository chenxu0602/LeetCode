#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (40.89%)
# Likes:    440
# Dislikes: 241
# Total Accepted:    51.4K
# Total Submissions: 125.4K
# Testcase Example:  '[1,2,2,4]'
#
# 
# The set S originally contains numbers from 1 to n. But unfortunately, due to
# the data error, one of the numbers in the set got duplicated to another
# number in the set, which results in repetition of one number and loss of
# another number. 
# 
# 
# 
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number
# that is missing. Return them in the form of an array.
# 
# 
# 
# Example 1:
# 
# Input: nums = [1,2,2,4]
# Output: [2,3]
# 
# 
# 
# Note:
# 
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
# 
# 
#
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        d = Counter(nums)
        dup = missing = 0

        for i in range(1, len(nums)+1):
            if i in d:
                if d[i] == 2:
                    dup = i
            else:
                missing = i

        return [dup, missing]
        """

        """
        arr = [0] * (len(nums)+1)
        dup, missing = -1, 1
        for i in range(len(nums)):
            arr[nums[i]] += 1

        for i in range(1, len(arr)):
            if arr[i] == 0:
                missing = i
            elif arr[i] == 2:
                dup = i

        return dup, missing
        """

        """
        dup, missing = -1, 1
        for n in nums:
            if nums[abs(n)-1] < 0:
                dup = abs(n)
            else:
                nums[abs(n)-1] *= -1

        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1

        return dup, missing
        """

        n = len(nums)
        s = n * (n+1) // 2
        missing = s - sum(set(nums))
        dup = sum(nums) + missing - s
        return dup, missing

        

