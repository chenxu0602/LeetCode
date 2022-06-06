#
# @lc app=leetcode id=2257 lang=python3
#
# [2257] Count Unguarded Cells in the Grid
#

# @lc code=start
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        dp = [[0] * n for _ in range(m)]
        for x, y in guards + walls:
            dp[x][y] = 1

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for x, y in guards:
            for dx, dy in directions:
                curr_x, curr_y = x, y


                while 0 <= curr_x + dx < m and 0 <= curr_y + dy < n and dp[curr_x + dx][curr_y + dy] != 1:
                    curr_x, curr_y = curr_x + dx, curr_y + dy
                    dp[curr_x][curr_y] = 2

        return sum(1 for i in range(m) for j in range(n) if dp[i][j] == 0)
        
# @lc code=end

