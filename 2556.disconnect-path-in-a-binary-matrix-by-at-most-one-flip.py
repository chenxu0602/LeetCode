#
# @lc app=leetcode id=2556 lang=python3
#
# [2556] Disconnect Path in a Binary Matrix by at Most One Flip
#

# @lc code=start
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:

        # In the first traversal we will simply set all trqavesed node to 0
        # By doing this, if there is any alternate path thats not depends on the first one then
        # its not possible to flip a single value to 0 and we won't be reaching.

        m, n = map(len, (grid, grid[0]))

        def dfs(i, j):
            if i + 1 == m and j + 1 == n:
                return True

            if i >= m or j >= n or grid[i][j] == 0:
                return False

            grid[i][j] = 0

            return dfs(i + 1, j) or dfs(i, j + 1)

        if dfs(0, 0) is False:
            return True

        grid[0][0] = 1
        return not dfs(0, 0)
        
# @lc code=end

