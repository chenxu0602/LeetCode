#
# @lc app=leetcode id=822 lang=python3
#
# [822] Card Flipping Game
#
# https://leetcode.com/problems/card-flipping-game/description/
#
# algorithms
# Medium (40.87%)
# Likes:    53
# Dislikes: 363
# Total Accepted:    6.8K
# Total Submissions: 16.5K
# Testcase Example:  '[1,2,4,4,7]\n[1,3,4,1,3]'
#
# On a table are N cards, with a positive integer printed on the front and back
# of each card (possibly different).
# 
# We flip any number of cards, and after we choose one card. 
# 
# If the number X on the back of the chosen card is not on the front of any
# card, then this number X is good.
# 
# What is the smallest number that is good?  If no number is good, output 0.
# 
# Here, fronts[i] and backs[i] represent the number on the front and back of
# card i. 
# 
# A flip swaps the front and back numbers, so the value on the front is now on
# the back and vice versa.
# 
# Example:
# 
# 
# Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
# Output: 2
# Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the
# backs are [1,2,4,1,3].
# We choose the second card, which has number 2 on the back, and it isn't on
# the front of any card, so 2 is good.
# 
# 
# 
# Note:
# 
# 
# 1 <= fronts.length == backs.length <= 1000.
# 1 <= fronts[i] <= 2000.
# 1 <= backs[i] <= 2000.
# 
# 
#
import itertools

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # O(N)
        # same = {x for i, x in enumerate(fronts) if x == backs[i]} 
        # ans = 9999

        # for x in itertools.chain(fronts, backs):
        #     if x not in same:
        #         ans = min(ans, x)

        # return ans % 9999


        same = {x for x, y in zip(fronts, backs) if x == y}
        return min([i for i in fronts + backs if i not in same] or [0])

