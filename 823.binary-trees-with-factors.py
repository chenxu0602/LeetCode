#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#
# https://leetcode.com/problems/binary-trees-with-factors/description/
#
# algorithms
# Medium (33.04%)
# Likes:    213
# Dislikes: 28
# Total Accepted:    8.1K
# Total Submissions: 24.3K
# Testcase Example:  '[2,4]'
#
# Given an array of unique integers, each integer is strictly greater than 1.
# 
# We make a binary tree using these integers and each number may be used for
# any number of times.
# 
# Each non-leaf node's value should be equal to the product of the values of
# it's children.
# 
# How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.
# 
# Example 1:
# 
# 
# Input: A = [2, 4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# 
# Example 2:
# 
# 
# Input: A = [2, 4, 5, 10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2,
# 5], [10, 5, 2].
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 1000.
# 2 <= A[i] <= 10 ^ 9.
# 
# 
#
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        """
        A.sort()
        dic = {num: 1 for num in A}
        for i in range(1, len(A)):
            for j in range(i):
                q, res = divmod(A[i], A[j])
                if res == 0 and q in dic:
                    dic[A[i]] += dic[q] * dic[A[j]]

        return sum(dic.values()) % (10 ** 9 + 7)
        """

        dp = {}
        for a in sorted(A):
            dp[a] = sum(dp[b] * dp.get(a // b, 0) for b in dp if a % b == 0) + 1
        return sum(dp.values()) % (10**9 + 7)
        

