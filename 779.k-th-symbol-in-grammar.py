#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#
# https://leetcode.com/problems/k-th-symbol-in-grammar/description/
#
# algorithms
# Medium (37.64%)
# Likes:    251
# Dislikes: 91
# Total Accepted:    17.3K
# Total Submissions: 45.9K
# Testcase Example:  '1\n1'
#
# On the first row, we write a 0. Now in every subsequent row, we look at the
# previous row and replace each occurrence of 0 with 01, and each occurrence of
# 1 with 10.
# 
# Given row N and index K, return the K-th indexed symbol in row N. (The values
# of K are 1-indexed.) (1 indexed).
# 
# 
# Examples:
# Input: N = 1, K = 1
# Output: 0
# 
# Input: N = 2, K = 1
# Output: 0
# 
# Input: N = 2, K = 2
# Output: 1
# 
# Input: N = 4, K = 5
# Output: 1
# 
# Explanation:
# row 1: 0
# row 2: 01
# row 3: 0110
# row 4: 01101001
# 
# 
# Note:
# 
# 
# N will be an integer in the range [1, 30].
# K will be an integer in the range [1, 2^(N-1)].
# 
# 
#
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        """
        self.mapping = ((0, 1), (1, 0))
        if N == 1:
            return 0
        return self.mapping[self.kthGrammar(N-1, K//2+K%2)][(K-1)%2]
        """

        """
        if N == 1: return 0
        return (1-K%2) ^ self.kthGrammar(N-1, (K+1)//2)
        """

        return bin(K-1).count('1') % 2
        

