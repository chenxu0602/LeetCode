#
# @lc app=leetcode id=499 lang=python3
#
# [499] The Maze III
#
# https://leetcode.com/problems/the-maze-iii/description/
#
# algorithms
# Hard (37.53%)
# Likes:    115
# Dislikes: 35
# Total Accepted:    10.5K
# Total Submissions: 28K
# Testcase Example:  '[[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]\n[4,3]\n[0,1]'
#
# There is a ball in a maze with empty spaces and walls. The ball can go
# through empty spaces by rolling up (u), down (d), left (l) or right (r), but
# it won't stop rolling until hitting a wall. When the ball stops, it could
# choose the next direction. There is also a hole in this maze. The ball will
# drop into the hole if it rolls on to the hole.
# 
# Given the ball position, the hole position and the maze, find out how the
# ball could drop into the hole by moving the shortest distance. The distance
# is defined by the number of empty spaces traveled by the ball from the start
# position (excluded) to the hole (included). Output the moving directions by
# using 'u', 'd', 'l' and 'r'. Since there could be several different shortest
# ways, you should output the lexicographically smallest way. If the ball
# cannot reach the hole, output "impossible".
# 
# The maze is represented by a binary 2D array. 1 means the wall and 0 means
# the empty space. You may assume that the borders of the maze are all walls.
# The ball and the hole coordinates are represented by row and column
# indexes.
# 
# 
# 
# Example 1:
# 
# 
# Input 1: a maze represented by a 2D array
# 
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
# 
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (0, 1)
# 
# Output: "lul"
# 
# Explanation: There are two shortest ways for the ball to drop into the hole.
# The first way is left -> up -> left, represented by "lul".
# The second way is up -> left, represented by 'ul'.
# Both ways have shortest distance 6, but the first way is lexicographically
# smaller because 'l' < 'u'. So the output is "lul".
# 
# 
# 
# Example 2:
# 
# 
# Input 1: a maze represented by a 2D array
# 
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
# 
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (3, 0)
# 
# Output: "impossible"
# 
# Explanation: The ball cannot reach the hole.
# 
# 
# 
# 
# 
# Note:
# 
# 
# There is only one ball and one hole in the maze.
# Both the ball and hole exist on an empty space, and they will not be at the
# same position initially.
# The given maze does not contain border (like the red rectangle in the example
# pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and the width and the height of
# the maze won't exceed 30.
# 
# 
#
# test again

import heapq

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        ball, hole = tuple(ball), tuple(hole)
        R, C = len(maze), len(maze[0])

        def neighbors(r, c):
            for dr, dc, di in [(-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd')]:
                cr, cc, dist = r, c, 0
                while 0 <= cr + dr < R and 0 <= cc + dc < C and not maze[cr+dr][cc+dc]:
                    cr += dr
                    cc += dc
                    dist += 1
                    if (cr, cc) == hole:
                        break 
                yield (cr, cc), di, dist

        pq = [(0, '', ball)]
        seen = set()
        while pq:
            dist, path, node = heapq.heappop(pq)
            if node in seen: continue
            if node == hole: return path
            seen.add(node)
            for nei, di, nei_dist in neighbors(*node):
                heapq.heappush(pq, (dist+nei_dist, path+di, nei))

        return "impossible"


        

