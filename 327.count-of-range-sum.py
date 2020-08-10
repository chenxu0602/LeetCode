#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#
# https://leetcode.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (32.79%)
# Likes:    383
# Dislikes: 61
# Total Accepted:    32K
# Total Submissions: 97.3K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# Given an integer array nums, return the number of range sums that lie in
# [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between
# indices i and j (i ≤ j), inclusive.
# 
# Note:
# A naive algorithm of O(n^2) is trivial. You MUST do better than that.
# 
# Example:
# 
# 
# Input: nums = [-2,5,-1], lower = -2, upper = 2,
# Output: 3 
# Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective
# sums are: -2, -1, 2.
# 
#
import itertools
from collections import defaultdict
import heapq

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        # O(N x (upper - lower + 1))
        # cumsum = [0] + list(itertools.accumulate(nums))
        # record = defaultdict(int)

        # res = 0
        # for csum in cumsum:
        #     for target in range(lower, upper + 1):
        #         if csum - target in record:
        #             res += record[csum - target]
        #     record[csum] += 1

        # return res


        # O(NlogN)
        first = [0] + list(itertools.accumulate(nums))

        def sort(lo, hi):
            mid = lo + (hi - lo) // 2
            if mid == lo:
                return 0

            count = sort(lo, mid) + sort(mid, hi)

            i = j = mid
            for left in first[lo:mid]:
                while i < hi and first[i] - left < lower:
                    i += 1
                while j < hi and first[j] - left <= upper:
                    j += 1

                count += j - i

            first[lo:hi] = sorted(first[lo:hi])
            return count

        return sort(0, len(first))




