#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#
# https://leetcode.com/problems/max-chunks-to-make-sorted/description/
#
# algorithms
# Medium (52.29%)
# Likes:    496
# Dislikes: 86
# Total Accepted:    25.5K
# Total Submissions: 48.8K
# Testcase Example:  '[4,3,2,1,0]'
#
# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we
# split the array into some number of "chunks" (partitions), and individually
# sort each chunk.  After concatenating them, the result equals the sorted
# array.
# 
# What is the most number of chunks we could have made?
# 
# Example 1:
# 
# 
# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2],
# which isn't sorted.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks
# possible.
# 
# 
# Note:
# 
# 
# arr will have length in range [1, 10].
# arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
# 
# 
# 
# 
#
import itertools

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # O(N)

        # ans = ma = 0
        # for i, x in enumerate(arr):
        #     ma = max(ma, x)
        #     if ma == i:
        #         ans += 1
        # return ans


        # return sum(mx == i for i, mx in enumerate(itertools.accumulate(arr, max)))


        i = targetSum = ans = 0
        n = len(arr)
        while i < n:
            currentSum = arr[i]
            while targetSum != currentSum:
                i += 1
                targetSum += i
                currentSum += arr[i]
            
            ans += 1
            i += 1
            targetSum = i
        return ans

        

