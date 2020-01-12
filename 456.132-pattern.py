#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#
# https://leetcode.com/problems/132-pattern/description/
#
# algorithms
# Medium (27.44%)
# Likes:    655
# Dislikes: 39
# Total Accepted:    29.7K
# Total Submissions: 108.2K
# Testcase Example:  '[1,2,3,4]'
#
# 
# Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a
# subsequence ai, aj, ak such
# that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n
# numbers as input and checks whether there is a 132 pattern in the list.
# 
# Note: n will be less than 15,000.
# 
# Example 1:
# 
# Input: [1, 2, 3, 4]
# 
# Output: False
# 
# Explanation: There is no 132 pattern in the sequence.
# 
# 
# 
# Example 2:
# 
# Input: [3, 1, 4, 2]
# 
# Output: True
# 
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# 
# 
# 
# Example 3:
# 
# Input: [-1, 3, 2, 0]
# 
# Output: True
# 
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1,
# 3, 0] and [-1, 2, 0].
# 
# 
#
class Solution:

    def binarySearch(self, val, A, high):
        low = 0
        while high - low > 0:
            i = low + (high - low) // 2
            if A[i] > val:
                low = i + 1
            else:
                high = i
        return high


    def find132pattern(self, nums: List[int]) -> bool:

        """
        min_i = float("inf")
        for j in range(len(nums)-1):
            min_i = min(min_i, nums[j])
            for k in range(j+1, len(nums)):
                if nums[k] < nums[j] and min_i < nums[k]:
                    return True

        return False
        """

        """
        stack = []

        if not nums: return False

        min_i = [float("inf")] * len(nums)
        min_i[0] = nums[0]

        for i in range(1, len(nums)):
            min_i[i] = min(min_i[i-1], nums[i])

        for j in range(len(nums)-1, -1, -1):
            if nums[j] > min_i[j]:
                while stack and stack[-1] <= min_i[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])

        return False
        """

        mins, maxs = [], []
        cur_min = float("inf")
        i = -1
        for x in nums:
            if x < cur_min:
                cur_min = x
            else:
                i = self.binarySearch(x, maxs, i + 1)
                if i > 0 and x > mins[i-1]:
                    return True
                if i < len(maxs):
                    maxs[i] = x
                    mins[i] = cur_min
                else:
                    maxs.append(x)
                    mins.append(cur_min)

        return False

        
        

