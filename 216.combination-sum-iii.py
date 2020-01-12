#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (52.55%)
# Likes:    739
# Dislikes: 41
# Total Accepted:    138.2K
# Total Submissions: 258.9K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
from itertools import combinations
from functools import reduce

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]
        """

        """
        def dfs(k, n, cap):
            if not k:
                return [[]] * (not n) # Success
            return [comb + [last] for last in range(1, cap) for comb in dfs(k-1, n-last, last)]
        return dfs(k, n, 10)
        """

        """
        combs = [[]]
        for _ in range(k):
            combs = [[first] + comb
                     for comb in combs
                     for first in range(1, comb[0] if comb else 10)]
        return [c for c in combs if sum(c) == n]
        """

        return [c for c in 
                reduce(lambda combs, _: [[first] + comb
                                         for comb in combs
                                         for first in range(1, comb[0] if comb else 10)],
                       range(k), [[]]) if sum(c) == n]


        
# @lc code=end

