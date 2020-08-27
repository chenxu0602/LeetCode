#
# @lc app=leetcode id=644 lang=python3
#
# [644] Maximum Average Subarray II
#
# https://leetcode.com/problems/maximum-average-subarray-ii/description/
#
# algorithms
# Hard (29.02%)
# Likes:    287
# Dislikes: 31
# Total Accepted:    8.7K
# Total Submissions: 29.7K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 
# Given an array consisting of n integers, find the contiguous subarray whose
# length is greater than or equal to k that has the maximum average value. And
# you need to output the maximum average value.
# 
# 
# 
# Example 1:
# 
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.
# 
# 
# 
# 
# Note:
# 
# 1 k n 
# Elements of the given array will be in range [-10,000, 10,000].
# The answer with the calculation error less than 10^-5 will be accepted.
# 
# 
#
from collections import deque

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # n = len(nums)
        # p = [0]
        # for i in nums:
        #     p.append(p[-1] + i)

        # def d(x, y):
        #     return (p[y + 1] - p[x]) / (y - x + 1)

        # hull = deque()
        # ans = float("-inf")
        # for j in range(k - 1, n):
        #     while len(hull) >= 2 and d(hull[-2], hull[-1] - 1) >= d(hull[-2], j - k):
        #         hull.pop()

        #     hull.append(j - k + 1)
        #     while len(hull) >= 2 and d(hull[0], hull[1] - 1) <= d(hull[0], j):
        #         hull.popleft()

        #     ans = max(ans, d(hull[0], j))

        # return ans


        # Binary Search
        # To find the maximum average of a subarray with atleast kk elements. 
        # Time  complexity: O(N x log2(max_val - min_val) / 0.0001), check function is O(N)
        # Space complexity: O(1)
        def check(nums, mid, k):
            sum_, prev, min_sum = 0, 0, 0
            for i in range(k):
                sum_ += nums[i] - mid

            if sum_ >= 0: return True

            for i in range(k, len(nums)):
                sum_ += nums[i] - mid
                prev += nums[i - k] - mid
                min_sum = min(prev, min_sum)
                if sum_ >= min_sum:
                    return True

            return False

        max_val, min_val = float("-inf"), float("inf")
        for n in nums:
            max_val = max(max_val, n)
            min_val = min(min_val, n)

        prev_mid, error = max_val, float("inf")
        while error > 0.00001:
            mid = (max_val + min_val) / 2.0

            if check(nums, mid, k):
                min_val = mid
            else:
                max_val = mid

            error = abs(prev_mid - mid)
            prev_mid = mid

        return min_val




