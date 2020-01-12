#
# @lc app=leetcode id=672 lang=python3
#
# [672] Bulb Switcher II
#
# https://leetcode.com/problems/bulb-switcher-ii/description/
#
# algorithms
# Medium (50.19%)
# Likes:    97
# Dislikes: 729
# Total Accepted:    10.1K
# Total Submissions: 20K
# Testcase Example:  '1\n1'
#
# There is a room with n lights which are turned on initially and 4 buttons on
# the wall. After performing exactly m unknown operations towards buttons, you
# need to return how many different kinds of status of the n lights could be.
# 
# Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4
# buttons are given below:
# 
# 
# Flip all the lights.
# Flip lights with even numbers.
# Flip lights with odd numbers.
# Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: n = 1, m = 1.
# Output: 2
# Explanation: Status can be: [on], [off]
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: n = 2, m = 1.
# Output: 3
# Explanation: Status can be: [on, off], [off, on], [off, off]
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: n = 3, m = 1.
# Output: 4
# Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off],
# [off, on, on].
# 
# 
# 
# 
# Note: n and m both fit in range [0, 1000].
# 
#
import itertools

class Solution:
    def flipLights(self, n: int, m: int) -> int:
        seen = set()
        for cand in itertools.product((0, 1), repeat=4):
            if sum(cand) % 2 == m % 2 and sum(cand) <= m:
                A = []
                for i in range(min(n, 3)):
                    light = 1
                    light ^= cand[0]
                    light ^= cand[1] and i % 2
                    light ^= cand[2] and i % 2 == 0
                    light ^= cand[3] and i % 3 == 0
                    A.append(light)
                seen.add(tuple(A))

        return len(seen)
        """

        n = min(n, 3)
        if m == 0: return 1
        if m == 1: return [2, 3, 4][n-1]
        if m == 2: return [2, 4, 7][n-1]
        return [2, 4, 8][n-1]
        """

        

