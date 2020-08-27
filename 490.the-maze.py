#
# @lc app=leetcode id=490 lang=python3
#
# [490] The Maze
#
# https://leetcode.com/problems/the-maze/description/
#
# algorithms
# Medium (50.07%)
# Likes:    597
# Dislikes: 63
# Total Accepted:    52.2K
# Total Submissions: 104.3K
# Testcase Example:  '[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n[0,4]\n[4,4]'
#
# There is a ball in a maze with empty spaces and walls. The ball can go
# through empty spaces by rolling up, down, left or right, but it won't stop
# rolling until hitting a wall. When the ball stops, it could choose the next
# direction.
# 
# Given the ball's start position, the destination and the maze, determine
# whether the ball could stop at the destination.
# 
# The maze is represented by a binary 2D array. 1 means the wall and 0 means
# the empty space. You may assume that the borders of the maze are all walls.
# The start and destination coordinates are represented by row and column
# indexes.
# 
# 
# 
# Example 1:
# 
# 
# Input 1: a maze represented by a 2D array
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
# 
# Output: true
# 
# Explanation: One possible way is : left -> down -> left -> down -> right ->
# down -> right.
# 
# 
# 
# Example 2:
# 
# 
# Input 1: a maze represented by a 2D array
# 
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
# 
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
# 
# Output: false
# 
# Explanation: There is no way for the ball to stop at the destination.
# 
# 
# 
# 
# 
# Note:
# 
# 
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not
# be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example
# pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of
# the maze won't exceed 100.
# 
# 
#

# @lc code=start
from functools import lru_cache
from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # Depth First Search
        # Time  complexity: O(mn)
        # Space complexity: O(mn)
        # @lru_cache(None)
        # def dfs(i, j):
        #     if (i, j) in seen:
        #         return False

        #     if [i, j] == destination:
        #         return True

        #     seen.add((i, j))

        #     for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
        #         x, y = i, j
        #         while 0 <= x + dx < m and 0 <= y + dy < n and not maze[x+dx][y+dy]:
        #             x, y = x + dx, y + dy
        #         if dfs(x, y):
        #             return True

        #     return False

        # m, n = map(len, (maze, maze[0]))
        # seen = set()
        # return dfs(*start)
        

        # Breadth First Search
        # Time  complexity: O(mn)
        # Space complexity: O(mn)
        m, n = map(len, (maze, maze[0]))
        seen = set()
        queue = deque([tuple(start)])

        while queue:
            q = queue.popleft()
            if q[0] == destination[0] and q[1] == destination[1]:
                return True

            for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
                x, y = q
                while 0 <= x + dx < m and 0 <= y + dy < n and not maze[x+dx][y+dy]:
                    x, y = x + dx, y + dy

                if not (x, y) in seen:
                    queue.append((x, y))
                    seen.add((x, y))

        return False

# @lc code=end

