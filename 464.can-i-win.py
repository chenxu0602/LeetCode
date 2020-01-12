#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (27.42%)
# Likes:    633
# Dislikes: 110
# Total Accepted:    37.2K
# Total Submissions: 135.5K
# Testcase Example:  '10\n11'
#
# In the "100 game," two players take turns adding, to a running total, any
# integer from 1..10. The player who first causes the running total to reach or
# exceed 100 wins. 
# 
# What if we change the game so that players cannot re-use integers? 
# 
# For example, two players might take turns drawing from a common pool of
# numbers of 1..15 without replacement until they reach a total >= 100.
# 
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players
# play optimally. 
# 
# You can always assume that maxChoosableInteger will not be larger than 20 and
# desiredTotal will not be larger than 300.
# 
# 
# Example
# 
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# Output:
# false
# 
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
# 
# 
#
from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        """
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False

        self.memo = {}
        return self.helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)
        """

        @lru_cache(None)
        def helper(nums_str, desiredTotal):
            nums = list(map(int, nums_str.split(',')))
            if nums[-1] >= desiredTotal: return True
            for i in range(len(nums)):
                new_nums_str = ",".join(map(str, nums[:i] + nums[i+1:]))
                if not helper(new_nums_str, desiredTotal - nums[i]):
                    return True
            return False

        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal: return False

        return helper(",".join(map(str, range(1, maxChoosableInteger+1))), desiredTotal)


    """
    def helper(self, nums, desiredTotal):
        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                self.memo[hash] = True
                return True

        self.memo[hash] = False
        return False
    """


        
        

