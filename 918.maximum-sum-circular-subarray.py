#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/
#
# algorithms
# Medium (32.48%)
# Likes:    400
# Dislikes: 22
# Total Accepted:    13.6K
# Total Submissions: 41.1K
# Testcase Example:  '[1,-2,3,-2]'
#
# Given a circular array C of integers represented by A, find the maximum
# possible sum of a non-empty subarray of C.
# 
# Here, a circular array means the end of the array connects to the beginning
# of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and
# C[i+A.length] = C[i] when i >= 0.)
# 
# Also, a subarray may only include each element of the fixed buffer A at most
# once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not
# exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
# 
# 
# 
# Example 2:
# 
# 
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
# 
# 
# 
# Example 3:
# 
# 
# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
# 
# 
# 
# Example 4:
# 
# 
# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
# 
# 
# Example 5:
# 
# 
# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
# 
# 
# 
# 
# Note: 
# 
# 
# -30000 <= A[i] <= 30000
# 1 <= A.length <= 30000
# 
# 
# 
# 
# 
# 
#
from collections import deque

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # Next Array
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # N = len(A)
        # ans = cur = float("-inf")
        # for x in A:
        #     cur = x + max(cur, 0)
        #     ans = max(ans, cur)

        # # ans is the answer for 1-interval subarrays.
        # # Now, let's consider all 2-interval subarrays.
        # # For each i, we want to know
        # # the maximum of sum(A[j:]) with j >= i+2
        # # rightsums[i] = sum(A[i:])
        # rightsums = [None] * N
        # rightsums[-1] = A[-1]
        # for i in range(N - 2, -1, -1):
        #     rightsums[i] = rightsums[i + 1] + A[i]

        # # maxright[i] = max_{j >= i} rightsums[j]
        # maxright = [None] * N
        # maxright[-1] = rightsums[-1]
        # for i in range(N - 2, -1, -1):
        #     maxright[i] = max(maxright[i + 1], rightsums[i])

        # leftsum = 0
        # for i in range(N - 2):
        #     leftsum += A[i]
        #     ans = max(ans, leftsum + maxright[i + 2])

        # return ans


        # Prefix Sums + Monoqueue
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # N = len(A)

        # # Compute P[j] = sum(B[:j]) for the fixed array B = A+A
        # P = [0]
        # for _ in range(2):
        #     for x in A:
        #         P.append(P[-1] + x)

        # # Want largest P[j] - P[i] with 1 <= j-i <= N
        # # For each j, want smallest P[i] with i >= j-N
        # ans = A[0]
        # queue = deque([0]) # i's, increasing by P[i]
        # for j in range(1, len(P)):
        #     # If the smallest i is too small, remove it.
        #     if queue[0] < j - N:
        #         queue.popleft()

        #     # The optimal i is deque[0], for cand. answer P[j] - P[i].
        #     ans = max(ans, P[j] - P[queue[0]])

        #     # Remove any i1's with P[i2] <= P[i1].
        #     while queue and P[j] <= P[queue[-1]]:
        #         queue.pop()

        #     queue.append(j)

        # return ans


        # Kadane's (Sign Variant)
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # def kadane(gen):
        #     ans = cur = float("-inf")
        #     for x in gen:
        #         cur = x + max(cur, 0)
        #         ans = max(ans, cur)
        #     return ans

        # S = sum(A)
        # ans1 = kadane(iter(A))
        # ans2 = S + kadane(-A[i] for i in range(1, len(A)))
        # ans3 = S + kadane(-A[i] for i in range(len(A) - 1))
        # return max(ans1, ans2, ans3)


        # Kadane's (Min Variant)
        # Time  complexity: O(N)
        # Space complexity: O(1)
        ans1 = cur = float("-inf")
        for x in A:
            cur = x + max(cur, 0)
            ans1 = max(ans1, cur)

        ans2 = cur = float("inf")
        for i in range(1, len(A)):
            cur = A[i] + min(cur, 0)
            ans2= min(ans2, cur)
        ans2 = sum(A) - ans2

        ans3 = cur = float("inf")
        for i in range(len(A) - 1):
            cur = A[i] + min(cur, 0)
            ans3 = min(ans3, 0)
        ans3 = sum(A) - ans3

        return max(ans1, ans2, ans3)

        # ****max*****|****min*******|*****max******


