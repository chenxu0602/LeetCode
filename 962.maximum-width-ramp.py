#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#
# https://leetcode.com/problems/maximum-width-ramp/description/
#
# algorithms
# Medium (45.22%)
# Likes:    605
# Dislikes: 18
# Total Accepted:    20.5K
# Total Submissions: 44.9K
# Testcase Example:  '[6,0,8,2,1,5]'
#
# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and
# A[i] <= A[j].  The width of such a ramp is j - i.
# 
# Find the maximum width of a ramp in A.  If one doesn't exist, return 0.
# 
# 
# 
# Example 1:
# 
# 
# Input: [6,0,8,2,1,5]
# Output: 4
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] =
# 5.
# 
# 
# 
# Example 2:
# 
# 
# Input: [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] =
# 1.
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
# 2 <= A.length <= 50000
# 0 <= A[i] <= 50000
# 
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
import bisect

class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # Sort
        # Time  complexity: O(NlogN), where N is the length of A.
        # Space complexity: O(N)
        ans = 0
        m = float("inf")
        for i in sorted(range(len(A)), key=A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans


        # Binary Search Candidates
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        # N = len(A)

        # ans = 0
        # candidates = [(A[N - 1], N - 1)]

        # for i in range(N - 2, -1, -1):
        #     jx = bisect.bisect_right(candidates, (A[i],))
        #     if jx < len(candidates):
        #         ans = max(ans, candidates[jx][1] - i)
        #     else:
        #         candidates.append((A[i], i))

        # return ans
        
# @lc code=end

