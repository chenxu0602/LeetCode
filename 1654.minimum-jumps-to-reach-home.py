#
# @lc app=leetcode id=1654 lang=python3
#
# [1654] Minimum Jumps to Reach Home
#
# https://leetcode.com/problems/minimum-jumps-to-reach-home/description/
#
# algorithms
# Medium (27.52%)
# Likes:    134
# Dislikes: 28
# Total Accepted:    4.1K
# Total Submissions: 15.4K
# Testcase Example:  '[14,4,18,1,15]\n3\n15\n9'
#
# A certain bug's home is on the x-axis at position x. Help them get there from
# position 0.
# 
# The bug jumps according to the following rules:
# 
# 
# It can jump exactly a positions forward (to the right).
# It can jump exactly b positions backward (to the left).
# It cannot jump backward twice in a row.
# It cannot jump to any forbidden positions.
# 
# 
# The bug may jump forward beyond its home, but it cannot jump to positions
# numbered with negative integers.
# 
# Given an array of integers forbidden, where forbidden[i] means that the bug
# cannot jump to the position forbidden[i], and integers a, b, and x, return
# the minimum number of jumps needed for the bug to reach its home. If there is
# no possible sequence of jumps that lands the bug on position x, return -1.
# 
# 
# Example 1:
# 
# 
# Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
# Output: 3
# Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
# 
# 
# Example 2:
# 
# 
# Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
# Output: 2
# Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will
# get the bug home.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= forbidden.length <= 1000
# 1 <= a, b, forbidden[i] <= 2000
# 0 <= x <= 2000
# All the elements in forbidden are distinct.
# Position x is not forbidden.
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        max_val = max([x] + forbidden) + a + b
        jumps = [0] + [float("inf")] * max_val

        for pos in forbidden:
            jumps[pos] = -1

        queue = deque([0])
        while queue:
            pos = queue.popleft()
            if pos + a <= max_val and jumps[pos + a] > jumps[pos] + 1:
                queue.append(pos + a)
                jumps[pos + a] = jumps[pos] + 1

            if pos - b > 0 and jumps[pos - b] > jumps[pos] + 1:
                jumps[pos - b] = jumps[pos] + 1
                if pos - b + a <= max_val and jumps[pos - b + a] > jumps[pos] + 2:
                    queue.append(pos - b + a)
                    jumps[pos - b + a] = jumps[pos] + 2

        return jumps[x] if jumps[x] < float("inf") else -1

        
# @lc code=end

