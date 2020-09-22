#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (48.71%)
# Likes:    1080
# Dislikes: 75
# Total Accepted:    39.9K
# Total Submissions: 80.9K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an array A of integers, return the number of (contiguous, non-empty)
# subarrays that have a sum divisible by K.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # Approach 1: Prefix Sums and Counting
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # P = [0]
        # for x in A:
        #     P.append((P[-1] + x) % K)

        # count = Counter(P)
        # return sum(v * (v - 1) // 2 for v in count.values())


        res = 0
        d = [1] + [0] * K
        acc = 0
        for a in A:
            acc = (acc + a) % K
            if d[acc]:
                res += d[acc]
            d[acc] += 1
        return res
        
# @lc code=end

