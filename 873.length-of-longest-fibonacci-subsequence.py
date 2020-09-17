#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#
# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/
#
# algorithms
# Medium (47.73%)
# Likes:    792
# Dislikes: 32
# Total Accepted:    31.8K
# Total Submissions: 66.3K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# A sequence X_1, X_2, ..., X_n is fibonacci-like if:
# 
# 
# n >= 3
# X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
# 
# 
# Given a strictly increasing array A of positive integers forming a sequence,
# find the length of the longest fibonacci-like subsequence of A.  If one does
# not exist, return 0.
# 
# (Recall that a subsequence is derived from another sequence A by deleting any
# number of elements (including none) from A, without changing the order of the
# remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6,
# 7, 8].)
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation:
# The longest subsequence that is fibonacci-like: [1,2,3,5,8].
# 
# 
# Example 2:
# 
# 
# Input: [1,3,7,11,12,14,18]
# Output: 3
# Explanation:
# The longest subsequence that is fibonacci-like:
# [1,11,12], [3,11,14] or [7,11,18].
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= A.length <= 1000
# 1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
# (The time limit has been reduced by 50% for submissions in Java, C, and
# C++.)
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # Brute Force with Set
        # Time  complexity: O(N^2 x logM), where N is the length of A, 
        # and M is the maximum value of A.
        # Space complexity: O(N)
        # S, ans = set(A), 0
        # for i in range(len(A)):
        #     for j in range(i + 1, len(A)):
        #         x, y, l = A[j], A[i] + A[j], 2
        #         while y in S:
        #             x, y = y, x + y
        #             l += 1
        #         ans = max(ans, l)
        # return ans if ans >= 3 else 0


        # Dynamic Programming
        # Time  complexity: O(N^2)
        # Space complexity: O(NlogM), where M is the largest element of A.
        index = {x: i for i, x in enumerate(A)}
        longest = defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0
        
# @lc code=end

