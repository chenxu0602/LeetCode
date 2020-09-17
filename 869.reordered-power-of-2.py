#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#
# https://leetcode.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (53.14%)
# Likes:    216
# Dislikes: 95
# Total Accepted:    15.1K
# Total Submissions: 28.2K
# Testcase Example:  '1'
#
# Starting with a positive integer N, we reorder the digits in any order
# (including the original order) such that the leading digit is not zero.
# 
# Return true if and only if we can do this in a way such that the resulting
# number is a power of 2.
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
# Input: 1
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: 24
# Output: false
# 
# 
# 
# Example 5:
# 
# 
# Input: 46
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter
import itertools

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # Time  complexity: O((logN)! x logN)
        # Space complexity: O(logN)
        # return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1 for cand in itertools.permutations(str(N)))

        # Counting
        # Time  complexity: O(logN ^ 2). There are logN different candidate powers of 2, 
        # and each comparison has O(logN) time complexity:
        # Space complexity: O(logN)
        count = Counter(str(N))
        return any(count == Counter(str(1 << b)) for b in range(32))
        
# @lc code=end

