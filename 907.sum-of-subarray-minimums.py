#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#
# https://leetcode.com/problems/sum-of-subarray-minimums/description/
#
# algorithms
# Medium (28.73%)
# Likes:    659
# Dislikes: 46
# Total Accepted:    14.6K
# Total Submissions: 50.1K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array of integers A, find the sum of min(B), where B ranges over
# every (contiguous) subarray of A.
# 
# Since the answer may be large, return the answer modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2],
# [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000
# 
# 
# 
# 
# 
# 
#
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        """
        MOD = 10 ** 9 + 7

        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c

            stack.append((y, count))
            dot += y * count
            ans += dot

        return ans % MOD
        """

        MOD = 10 ** 9 + 7
        N = len(A)

        stack = []
        prev = [None] * N
        for i in range(N):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        next_ = [None] * N
        for k in range(N-1, -1, -1):
            while stack and A[k] < A[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else N
            stack.append(k)

        return sum((i - prev[i]) * (next_[i] - i) * A[i]
                    for i in range(N)) % MOD
        

