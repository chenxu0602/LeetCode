#
# @lc app=leetcode id=1036 lang=python3
#
# [1036] Escape a Large Maze
#
# https://leetcode.com/problems/escape-a-large-maze/description/
#
# algorithms
# Hard (35.17%)
# Likes:    119
# Dislikes: 78
# Total Accepted:    5.7K
# Total Submissions: 16.2K
# Testcase Example:  '[[0,1],[1,0]]\n[0,0]\n[0,2]'
#
# In a 1 million by 1 million grid, the coordinates of each grid square are (x,
# y) with 0 <= x, y < 10^6.
# 
# We start at the source square and want to reach the target square.  Each
# move, we can walk to a 4-directionally adjacent square in the grid that isn't
# in the given list of blocked squares.
# 
# Return true if and only if it is possible to reach the target square through
# a sequence of moves.
# 
# 
# 
# Example 1:
# 
# 
# Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# Output: false
# Explanation: 
# The target square is inaccessible starting from the source square, because we
# can't walk outside the grid.
# 
# 
# Example 2:
# 
# 
# Input: blocked = [], source = [0,0], target = [999999,999999]
# Output: true
# Explanation: 
# Because there are no blocked cells, it's possible to reach the target
# square.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= blocked.length <= 200
# blocked[i].length == 2
# 0 <= blocked[i][j] < 10^6
# source.length == target.length == 2
# 0 <= source[i][j], target[i][j] < 10^6
# source != target
# 
# 
#
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        blocked = set(map(tuple, blocked))

        def dfs(x, y, target, seen):
            if not (0 <= x < 10**6 and 0 <= y < 10**6)  \
                or (x, y) in blocked or (x, y) in seen:
                return False

            seen.add((x, y))

            if len(seen) > 20000 or [x, y] == target:
                return True

            return dfs(x+1, y, target, seen) \
                or dfs(x-1, y, target, seen) \
                or dfs(x, y+1, target, seen) \
                or dfs(x, y-1, target, seen)

        return dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set())

        """
        blocked = {tuple(p) for p in blocked}

        def bfs(soruce, target):
            bfs, seen = [source], {tuple(source)}
            for x0, y0 in bfs:
                for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = x0 +i, y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target:
                            return True
                        bfs.append([x, y])
                        seen.add((x, y))
                if len(bfs) > 20000:
                    return True
            return False

        return bfs(source, target) and bfs(target, source)
        """
        

