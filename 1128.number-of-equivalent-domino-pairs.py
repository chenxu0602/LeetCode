#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
#
# algorithms
# Easy (44.44%)
# Likes:    83
# Dislikes: 47
# Total Accepted:    11.6K
# Total Submissions: 25.5K
# Testcase Example:  '[[1,2],[2,1],[3,4],[5,6]]'
#
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] =
# [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is,
# one domino can be rotated to be equal to another domino.
# 
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and
# dominoes[i] is equivalent to dominoes[j].
# 
# 
# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        """
        d = {}
        for domi in dominoes:
            p = tuple(sorted(domi))
            if p in d:
                d[p] += 1
            else:
                d[p] = 1

        c = 0 
        for n in d.values():
            s = n*(n-1)//2
            c += s
        return c
        """
        return sum(n * (n-1) // 2 for n in Counter(tuple(sorted(x)) for x in dominoes).values())


        
# @lc code=end

