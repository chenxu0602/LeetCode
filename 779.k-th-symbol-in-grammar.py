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
        # self.mapping = ((0, 1), (1, 0))
        # if N == 1:
        #     return 0
        # return self.mapping[self.kthGrammar(N-1, K//2+K%2)][(K-1)%2]

        # if N == 1: return 0
        # return (1-K%2) ^ self.kthGrammar(N-1, (K+1)//2)

        # return bin(K-1).count('1') % 2


        # In general, the Kth digit's parent is going to be (K+1) / 2. If the parent is 0, then the digit will be the same as 1 - (K%2). If the parent is 1, the digit will be the opposite, ie. K%2.
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # if N == 1: return 0
        # return (1 - K % 2) ^ self.kthGrammar(N - 1, (K + 1) // 2)


        # We notice a pattern: the second half is always the first half "flipped".
        # This leads to the following algorithm idea: if K is in the second half, then we could put K -= (1 << N-2) so that it is in the first half, and flip the final answer.
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # if N == 1: return 0
        # if K <= 2 ** (N - 2):
        #     return self.kthGrammar(N - 1, K)
        # return self.kthGrammar(N - 1, K - 2 ** (N - 2)) ^ 1


        # When the indexes K are written in binary (now indexing from zero), indexes of the second half of a row are ones with the first bit set to 1.
        # This means when applying the algorithm in Approach #3 virtually, the number of times we will flip the final answer is just the number of 1s in the binary representation of K-1.
        # Time  complexity: O(logN)
        # Space complexity: O(1)
        return bin(K - 1).count('1') % 2
        

