#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (50.07%)
# Likes:    299
# Dislikes: 466
# Total Accepted:    55.8K
# Total Submissions: 111.4K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# 
# 
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
# 
# 
# 
#
from collections import Counter, defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # return sum(
        #     n*(n-1)
        #     for x0, y0 in points for n in Counter((x-x0)**2 + (y-y0)**2 for x, y in points).values()
        # )

        res = 0
        for p in points:
            cmap = defaultdict(int)
            for q in points:
                f = p[0] - q[0]
                s = p[1] - q[1]
                cmap[f**2+s**2] += 1

            for k, v in cmap.items():
                res += v * (v-1)

        return res

