#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#
# https://leetcode.com/problems/longest-turbulent-subarray/description/
#
# algorithms
# Medium (46.51%)
# Likes:    430
# Dislikes: 94
# Total Accepted:    31.4K
# Total Submissions: 67.5K
# Testcase Example:  '[9,4,2,10,7,8,8,1,9]'
#
# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only
# if:
# 
# 
# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is
# even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is
# odd.
# 
# 
# That is, the subarray is turbulent if the comparison sign flips between each
# adjacent pair of elements in the subarray.
# 
# Return the length of a maximum size turbulent subarray of A.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# 
# 
# 
# Example 2:
# 
# 
# Input: [4,8,12,16]
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: [100]
# Output: 1
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9
# 
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        # Sliding Window
        # Time  complexity: O(N)
        # Space complexity: O(1)
        def cmp(a, b):
            return (a > b) - (a < b)

        N, ans, anchor = len(A), 1, 0

        for i in range(1, N):
            c = cmp(A[i - 1], A[i])
            if c == 0:
                anchor = i
            elif i == N - 1 or c * cmp(A[i], A[i + 1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i

        return ans


        # best = clen = 0
        # for i in range(len(A)):
        #     if i >= 2 and (A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]):
        #         clen += 1
        #     elif i >= 1 and A[i - 1] != A[i]:
        #         clen = 2
        #     else:
        #         clen = 1

        #     best = max(best, clen)
        # return best
        
# @lc code=end

