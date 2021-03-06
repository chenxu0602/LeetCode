#
# @lc app=leetcode id=891 lang=python3
#
# [891] Sum of Subsequence Widths
#
# https://leetcode.com/problems/sum-of-subsequence-widths/description/
#
# algorithms
# Hard (31.82%)
# Likes:    243
# Dislikes: 102
# Total Accepted:    8.8K
# Total Submissions: 27.4K
# Testcase Example:  '[2,1,3]'
#
# Given an array of integers A, consider all non-empty subsequences of A.
# 
# For any sequence S, let the width of S be the difference between the maximum
# and minimum element of S.
# 
# Return the sum of the widths of all subsequences of A. 
# 
# As the answer may be very large, return the answer modulo 10^9 + 7.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [2,1,3]
# Output: 6
# Explanation:
# Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
# The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
# The sum of these widths is 6.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 1 <= A[i] <= 20000
# 
# 
# 
#

# @lc code=start
class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        # Mathematical
        # Sum_{j > i} (2^(j - i - 1)) x (A_j - A_i) = Sum_{i = 0}^{n - 1} (2^i - 2^(N - i - 1)) x A_i
        # Time  complexity: O(NlogN), where N is the length of A.
        # Space complexity: O(N)
        MOD = 10**9 + 7
        N = len(A)
        A.sort()

        pow2 = [1]
        for i in range(1, N):
            pow2.append(pow2[-1] * 2 % MOD)

        ans = 0
        for i, x in enumerate(A):
            ans = (ans + (pow2[i] - pow2[N - i - 1]) * x) % MOD 

        return ans

        
# @lc code=end

