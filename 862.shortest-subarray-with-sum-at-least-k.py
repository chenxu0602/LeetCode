#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (23.20%)
# Likes:    765
# Dislikes: 23
# Total Accepted:    21.9K
# Total Submissions: 94.6K
# Testcase Example:  '[1]\n1'
#
# Return the length of the shortest, non-empty, contiguous subarray of A with
# sum at least K.
# 
# If there is no non-empty subarray with sum at least K, return -1.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1], K = 1
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [1,2], K = 4
# Output: -1
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,-1,2], K = 3
# Output: 3
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import deque
import itertools

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # Time  complexity: O(N)
        # Space complexity: O(N)
        N = len(A)
        P = [0] + list(itertools.accumulate(A))

        ans = N + 1
        monoq = deque()

        for y, Py in enumerate(P):
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)
        
        return ans if ans < N + 1 else -1
# @lc code=end

