#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#
# https://leetcode.com/problems/dungeon-game/description/
#
# algorithms
# Hard (32.16%)
# Likes:    1720
# Dislikes: 40
# Total Accepted:    108.9K
# Total Submissions: 338K
# Testcase Example:  '[[-2,-3,3],[-5,-10,1],[10,30,-5]]'
#
# table.dungeon, .dungeon th, .dungeon td {
# ⁠ border:3px solid black;
# }
# 
# ⁠.dungeon th, .dungeon td {
# ⁠   text-align: center;
# ⁠   height: 70px;
# ⁠   width: 70px;
# }
# 
# The demons had captured the princess (P) and imprisoned her in the
# bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid
# out in a 2D grid. Our valiant knight (K) was initially positioned in the
# top-left room and must fight his way through the dungeon to rescue the
# princess.
# 
# The knight has an initial health point represented by a positive integer. If
# at any point his health point drops to 0 or below, he dies immediately.
# 
# Some of the rooms are guarded by demons, so the knight loses health (negative
# integers) upon entering these rooms; other rooms are either empty (0's) or
# contain magic orbs that increase the knight's health (positive integers).
# 
# In order to reach the princess as quickly as possible, the knight decides to
# move only rightward or downward in each step.
# 
# 
# 
# Write a function to determine the knight's minimum initial health so that he
# is able to rescue the princess.
# 
# For example, given the dungeon below, the initial health of the knight must
# be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN ->
# DOWN.
# 
# 
# 
# 
# -2 (K)
# -3
# 3
# 
# 
# -5
# -10
# 1
# 
# 
# 10
# 30
# -5 (P)
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight
# enters and the bottom-right room where the princess is imprisoned.
# 
# 
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        # Time  complexity: O(M x N)
        # Space complexity: O(M x N)
        # m, n = map(len, (dungeon, dungeon[0]))
        # dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        # dp[m][n-1] = dp[m-1][n] = 1

        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
        #         dp[i][j] = max(1, need)

        # return dp[0][0]


        # Time  complexity: O(M x N)
        # Space complexity: O(N)
        n = len(dungeon[0])
        need = [float("inf")] * (n - 1) + [1]

        for row in dungeon[::-1]:
            for j in range(n)[::-1]:
                need[j] = max(min(need[j:j+2]) - row[j], 1)

        return need[0]
        
# @lc code=end

