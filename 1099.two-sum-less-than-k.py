#
# @lc app=leetcode id=1099 lang=python3
#
# [1099] Two Sum Less Than K
#
# https://leetcode.com/problems/two-sum-less-than-k/description/
#
# algorithms
# Easy (60.54%)
# Likes:    372
# Dislikes: 43
# Total Accepted:    43.1K
# Total Submissions: 70.9K
# Testcase Example:  '[34,23,1,24,75,33,54,8]\n60'
#
# Given an array A of integers and integer K, return the maximum S such that
# there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist
# satisfying this equation, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [34,23,1,24,75,33,54,8], K = 60
# Output: 58
# Explanation: 
# We can use 34 and 24 to sum 58 which is less than 60.
# 
# 
# Example 2:
# 
# 
# Input: A = [10,20,30], K = 15
# Output: -1
# Explanation: 
# In this case it's not possible to get a pair sum less that 15.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i] <= 1000
# 1 <= K <= 2000
# 
# 
#

# @lc code=start
import bisect

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        # Two Pointers
        # Time  complexity: O(nlogn)
        # Space complexity: O(logn) to O(n)
        # S = -1
        # A.sort()
        # lo, hi = 0, len(A) - 1
        # while lo < hi:
        #     if A[lo] + A[hi] < K:
        #         S = max(S, A[lo] + A[hi])
        #         lo += 1
        #     else:
        #         hi -= 1
        # return S


        # Binary Search
        # Time  complexity: O(nlogn)
        # Space complexity: O(logn) to O(n)
        # S = -1
        # A.sort()
        # for i in range(len(A)):
        #     j = bisect.bisect_left(A, K - A[i], i + 1) - 1
        #     if j > i:
        #         S = max(S, A[i] + A[j])
        # return S


        # Counting Sort
        # Time  complexity: O(n + m) where m corresponds to the range of values in the input array.
        # Space complexity: O(m)
        S = -1
        count = [0] * 1001
        for i in A:
            count[i] += 1
        lo, hi = 0, 1000
        while lo < hi:
            if lo + hi >= K or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > 0 if lo < hi else 1:
                    S = max(S, lo + hi)
                lo += 1
        return S

        
# @lc code=end

