#
# @lc app=leetcode id=505 lang=python3
#
# [505] The Maze II
#
# https://leetcode.com/problems/the-maze-ii/description/
#
# algorithms
# Medium (44.43%)
# Likes:    352
# Dislikes: 14
# Total Accepted:    29.4K
# Total Submissions: 66.2K
# Testcase Example:  '[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n[0,4]\n[4,4]'
#
# There is a ball in a maze with empty spaces and walls. The ball can go
# through empty spaces by rolling up, down, left or right, but it won't stop
# rolling until hitting a wall. When the ball stops, it could choose the next
# direction.
# 
# Given the ball's start position, the destination and the maze, find the
# shortest distance for the ball to stop at the destination. The distance is
# defined by the number of empty spaces traveled by the ball from the start
# position (excluded) to the destination (included). If the ball cannot stop at
# the destination, return -1.
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
# Output: 12
# 
# Explanation: One shortest way is : left -> down -> left -> down -> right ->
# down -> right.
# ⁠            The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
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
# Output: -1
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
import heapq 

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        ball, hole = tuple(start), tuple(destination)
        R, C = len(maze), len(maze[0])

        def neighbors(r, c):
            for dr, dc, di in [(-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd')]:
                cr, cc, dist = r, c, 0
                while 0 <= cr + dr < R and 0 <= cc + dc < C and not maze[cr+dr][cc+dc]:
                    cr += dr
                    cc += dc
                    dist += 1
                yield (cr, cc), di, dist

        pq = [(0, '', ball)]
        seen = set()
        while pq:
            dist, path, node = heapq.heappop(pq)
            if node in seen: continue
            if node == hole: return dist
            seen.add(node)
            for nei, di, nei_dist in neighbors(*node):
                heapq.heappush(pq, (dist+nei_dist, path+di, nei))

        return -1
        

