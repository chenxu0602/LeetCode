#
# @lc app=leetcode id=795 lang=python3
#
# [795] Number of Subarrays with Bounded Maximum
#
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
#
# algorithms
# Medium (46.20%)
# Likes:    605
# Dislikes: 43
# Total Accepted:    19.4K
# Total Submissions: 41.8K
# Testcase Example:  '[2,1,4,3]\n2\n3'
#
# We are given an array A of positive integers, and two positive integers L and
# R (L <= R).
# 
# Return the number of (contiguous, non-empty) subarrays such that the value of
# the maximum array element in that subarray is at least L and at most R.
# 
# 
# Example :
# Input: 
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2,
# 1], [3].
# 
# 
# Note:
# 
# 
# L, R  and A[i] will be an integer in the range [0, 10^9].
# The length of A will be in the range of [1, 50000].
# 
# 
#

# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        # Time  complexity: O(N)
        # Space complexity: O(1)
        def count(bound):
            ans = cur = 0
            for x in A:
                cur = cur + 1 if x <= bound else 0
                ans += cur
            return ans

        return count(R) - count(L - 1)
        
# @lc code=end

