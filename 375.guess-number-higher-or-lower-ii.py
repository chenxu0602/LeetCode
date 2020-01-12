#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/
#
# algorithms
# Medium (37.74%)
# Likes:    516
# Dislikes: 737
# Total Accepted:    44.8K
# Total Submissions: 118.4K
# Testcase Example:  '1'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number I picked is
# higher or lower.
# 
# However, when you guess a particular number x, and you guess wrong, you pay
# $x. You win the game when you guess the number I picked.
# 
# Example:
# 
# 
# n = 10, I pick 8.
# 
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
# 
# Game over. 8 is the number I picked.
# 
# You end up paying $5 + $7 + $9 = $21.
# 
# 
# Given a particular n ≥ 1, find out how much money you need to have to
# guarantee a win.
#
class Solution:
    def getMoneyAmount(self, n: int) -> int:

        """
        dp = [[0] * (n+1) for _ in range(n+1)]

        for l in range(2, n+1):
            for start in range(1, n-l+2):
                minres = 100000000000000
                for piv in range(start, start+l-1):
                    res = piv + max(dp[start][piv-1], dp[piv+1][start+l-1])
                    minres = min(res, minres)
                dp[start][start+l-1] = minres

        return dp[1][n]
        """

        """
        class Need(dict):
            def __missing__(self, (lo, hi)):
                if lo >= hi:
                    return 0
                ret = self[lo, hi] = min(x + max(self[lo, x-1], self[x+1, hi]) for x in range(lo, hi))

                return ret

        return Need()[1, n]
        """

        need = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi]) for x in range(lo, hi))
        return need[1][n]




