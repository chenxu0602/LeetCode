#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
#
# algorithms
# Hard (48.61%)
# Likes:    813
# Dislikes: 22
# Total Accepted:    29.4K
# Total Submissions: 59.1K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in ascending order. Find the smallest
# range that includes at least one number from each of the k lists.
# 
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c
# if b-a == d-c.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# 
# 
# 
# 
# Note:
# 
# 
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -10^5 <= value of elements <= 10^5.
# 
# 
#

# @lc code=start
from heapq import heappush, heappop, heapify

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapify(pq)

        ans = float("-inf"), float("inf")
        right = max(row[0] for row in nums)

        while pq:
            left, i, j = heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                return ans

            v = nums[i][j+1]
            right = max(right, v)
            heappush(pq, (v, i, j+1))

        """
        indices = [0] * len(nums)
        minHeap = [(num[0], bid) for bid, num in enumerate(nums)]
        heapify(minHeap)

        upper = max(num[0] for num in nums)
        lower = minHeap[0][0]

        high = upper

        while minHeap:
            minVal, bid = heappop(minHeap)
            indices[bid] += 1
            ind = indices[bid]

            if ind == len(nums[bid]):
                break

            heappush(minHeap, (nums[bid][ind], bid))

            high = max(high, nums[bid][ind])

            low = minHeap[0][0]

            if high - low < upper - lower:
                lower, upper = low, high

        return lower, upper
        """

        
# @lc code=end

