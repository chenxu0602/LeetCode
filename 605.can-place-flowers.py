#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (31.04%)
# Likes:    495
# Dislikes: 277
# Total Accepted:    66.2K
# Total Submissions: 212.8K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# Suppose you have a long flowerbed in which some of the plots are planted and
# some are not. However, flowers cannot be planted in adjacent plots - they
# would compete for water and both would die.
# 
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means
# empty and 1 means not empty), and a number n, return if n new flowers can be
# planted in it without violating the no-adjacent-flowers rule.
# 
# Example 1:
# 
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# 
# 
# 
# Note:
# 
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
# 
# 
#
from itertools import groupby

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # O(n) / O(1)
        # i, count = 0, 0
        # while i < len(flowerbed):
        #     if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
        #         flowerbed[i] = 1
        #         i += 1
        #         count += 1
        #     if count >= n:
        #         return True

        #     i += 1
        # return False


        zero = 1
        for slot in flowerbed:
            if slot == 0:
                zero += 1
            else:
                n -= (zero - 1) // 2
                zero = 0

        n -= zero // 2
        return n <= 0


        # groups = groupby([0] + flowerbed + [0])
        # count = 0
        # for i, v in groups:
        #     if i == 0:
        #         count += (len(list(v)) - 1) // 2

        # return count >= n
        

