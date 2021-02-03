#
# @lc app=leetcode id=1734 lang=python3
#
# [1734] Decode XORed Permutation
#
# https://leetcode.com/problems/decode-xored-permutation/description/
#
# algorithms
# Medium (49.81%)
# Likes:    212
# Dislikes: 6
# Total Accepted:    4K
# Total Submissions: 8K
# Testcase Example:  '[3,1]'
#
# There is an integer array perm that is a permutation of the first n positive
# integers, where n is always odd.
# 
# It was encoded into another integer array encoded of length n - 1, such that
# encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then
# encoded = [2,1].
# 
# Given the encoded array, return the original array perm. It is guaranteed
# that the answer exists and is unique.
# 
# 
# Example 1:
# 
# 
# Input: encoded = [3,1]
# Output: [1,2,3]
# Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
# 
# 
# Example 2:
# 
# 
# Input: encoded = [6,5,4,6]
# Output: [2,4,1,5,3]
# 
# 
# 
# Constraints:
# 
# 
# 3 <= n < 10^5
# n is odd.
# encoded.length == n - 1
# 
# 
#

# @lc code=start
from functools import reduce 
import itertools, operator

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        first = 0
        n = len(encoded) + 1
        for i in range(1, n + 1):
            first = first ^ i

        for i in range(1, n, 2):
            first = first ^ encoded[i]

        perm = [0] * n
        perm[0] = first

        for i in range(n - 1):
            perm[i + 1] = perm[i] ^ encoded[i]

        return perm


        # first = reduce(operator.ixor, encoded[::-2] + list(range(len(encoded) + 2)))
        # return list(itertools.accumulate([first] + encoded, operator.ixor))

        
# @lc code=end

