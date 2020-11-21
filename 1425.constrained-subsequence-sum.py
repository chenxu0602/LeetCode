#
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subsequence Sum
#
# https://leetcode.com/problems/constrained-subsequence-sum/description/
#
# algorithms
# Hard (44.58%)
# Likes:    396
# Dislikes: 20
# Total Accepted:    9.8K
# Total Submissions: 22K
# Testcase Example:  '[10,2,-10,5,20]\n2'
#
# Given an integer array nums and an integer k, return the maximum sum of a
# non-empty subsequence of that array such that for every two consecutive
# integers in the subsequence, nums[i] and nums[j], where i < j, the condition
# j - i <= k is satisfied.
# 
# A subsequence of an array is obtained by deleting some number of elements
# (can be zero) from the array, leaving the remaining elements in their
# original order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest
# number.
# 
# 
# Example 3:
# 
# 
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
from collections import deque
import heapq

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        # where res[i] means the maximum result you can get if the last element is A[i].
        # O(n) / O(k)
        # queue = deque()
        # for i in range(len(nums)):
        #     nums[i] += queue[0] if queue else 0
        #     while len(queue) and nums[i] > queue[-1]:
        #         queue.pop()
        #     if nums[i] > 0:
        #         queue.append(nums[i])
        #     if i >= k and queue and queue[0] == nums[i - k]:
        #         queue.popleft()
        
        # return max(nums)


        heap = [(-nums[0], 0)]
        ret = nums[0]

        for i in range(1, len(nums)):
            remove = i - k - 1
            while remove >= heap[0][1]:
                heapq.heappop(heap)

            cur = max(0, -heap[0][0]) + nums[i]
            ret = max(ret, cur)
            heapq.heappush(heap, (-cur, i))

        return ret

            

# @lc code=end

