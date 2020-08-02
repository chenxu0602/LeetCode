#
# @lc app=leetcode id=1508 lang=python3
#
# [1508] Range Sum of Sorted Subarray Sums
#
# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/
#
# algorithms
# Medium (71.65%)
# Likes:    117
# Dislikes: 26
# Total Accepted:    8.9K
# Total Submissions: 12.4K
# Testcase Example:  '[1,2,3,4]\n4\n1\n5'
#
# Given the array nums consisting of n positive integers. You computed the sum
# of all non-empty continous subarrays from the array and then sort them in
# non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
# 
# Return the sum of the numbers from index left to index right (indexed from
# 1), inclusive, in the new array. Since the answer can be a huge number return
# it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
# Output: 13 
# Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After
# sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5,
# 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3
# + 3 + 4 = 13. 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
# Output: 6
# Explanation: The given array is the same as example 1. We have the new array
# [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to
# ri = 4 is 3 + 3 = 6.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
# Output: 50
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^3
# nums.length == n
# 1 <= nums[i] <= 100
# 1 <= left <= right <= n * (n + 1) / 2
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)

        ans = 0
        for k in range(1, right + 1):
            x, i = heapq.heappop(heap)
            if k >= left:
                ans += x
            if i + 1 < n:
                heapq.heappush(heap, (x + nums[i+1], i + 1))

        return ans % (10**9 + 7)

        # A = nums[:]

        # B, C = [0] * (n + 1), [0] * (n + 1)
        # for i in range(n):
        #     B[i + 1] = B[i] + A[i]
        #     C[i + 1] = C[i] + B[i + 1]

        # def count_sum_under(score):
        #     res = i = 0
        #     for j in range(n + 1):
        #         while B[j] - B[i] > score:
        #             i += 1
        #         res += j - i
        #     return res

        # def sum_k_sums(k):
        #     score = kth_score(k)
        #     res = i = 0
        #     for j in range(n + 1):
        #         while B[j] - B[i] > score:
        #             i += 1
        #         res += B[j] * (j - i + 1) - (C[j] - (C[i - 1] if i else 0))
        #     return res - (count_sum_under(score) - k) * score

        # def kth_score(k):
        #     l, r = 0, B[n]
        #     while l < r:
        #         m = (l + r) / 2
        #         if count_sum_under(m) < k:
        #             l += 1
        #         else:
        #             r = m
        #     return l

        # return sum_k_sums(right) - sum_k_sums(left - 1)


        
# @lc code=end

