#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (36.44%)
# Likes:    901
# Dislikes: 63
# Total Accepted:    105K
# Total Submissions: 288.1K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#
from heapq import heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        res, i, j, k = [1], 0, 0, 0
        while len(res) < n:
            u2, u3, u5 = 2 * res[i], 3 * res[j], 5 * res[k]
            umin = min(u2, u3, u5)
            if umin == u2:
                i += 1
            if umin == u3:
                j += 1
            if umin == u5:
                k += 1
            res.append(umin)

        return res[-1]
        """

        """
        seen = {1, }
        nums = []
        heap = []
        heappush(heap, 1)

        for _ in range(1690):
            curr_ugly = heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)

        return nums[n-1]
        """

        nums = [1, ]
        i2, i3, i5 = 0, 0, 0
        while len(nums) < n:
            ugly = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1

        return nums[-1]
            
        

