#
# @lc app=leetcode id=768 lang=python3
#
# [768] Max Chunks To Make Sorted II
#
# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/
#
# algorithms
# Hard (48.57%)
# Likes:    445
# Dislikes: 20
# Total Accepted:    21.7K
# Total Submissions: 44.4K
# Testcase Example:  '[5,4,3,2,1]'
#
# This question is the same as "Max Chunks to Make Sorted" except the integers
# of the given array are not necessarily distinct, the input array could be up
# to length 2000, and the elements could be up to 10**8.
# 
# 
# 
# Given an array arr of integers (not necessarily distinct), we split the array
# into some number of "chunks" (partitions), and individually sort each chunk.
# After concatenating them, the result equals the sorted array.
# 
# What is the most number of chunks we could have made?
# 
# Example 1:
# 
# 
# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3],
# which isn't sorted.
# 
# 
# Example 2:
# 
# 
# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks
# possible.
# 
# 
# Note:
# 
# 
# arr will have length in range [1, 2000].
# arr[i] will be an integer in range [0, 10**8].
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict, Counter

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Sliding Window
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        # count = defaultdict(int)
        # ans = nonzero = 0

        # for x, y in zip(arr, sorted(arr)):
        #     count[x] += 1
        #     if count[x] == 0: nonzero -= 1
        #     if count[x] == 1: nonzero += 1

        #     count[y] -= 1
        #     if count[y] == -1: nonzero += 1
        #     if count[y] == 0: nonzero -= 1

        #     if nonzero == 0: ans += 1

        # return ans
        

        # Sorted Count Pairs
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        # count, counted = Counter(), []
        # for x in arr:
        #     count[x] += 1
        #     counted.append((x, count[x]))

        # ans, cur = 0, (0, 0)
        # for X, Y in zip(counted, sorted(counted)):
        #     cur = max(cur, X)
        #     if cur == Y:
        #         ans += 1
        # return ans


        stack = []
        for e in arr:
            start = 0
            while stack and (stack[-1][0] > e or stack[-1][1] > e):
                last = stack.pop()
                start = max(start, last[0], last[1])
            stack.append((e, start))
        return len(stack)


# @lc code=end

