#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#
# https://leetcode.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (44.46%)
# Likes:    365
# Dislikes: 28
# Total Accepted:    13.5K
# Total Submissions: 30K
# Testcase Example:  '[[0,1],[1,0]]'
#
# In a given 2D binary array A, there are two islands.  (An island is a
# 4-directionally connected group of 1s not connected to any other 1s.)
# 
# Now, we may change 0s to 1s so as to connect the two islands together to form
# 1 island.
# 
# Return the smallest number of 0s that must be flipped.  (It is guaranteed
# that the answer is at least 1.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [[0,1],[1,0]]
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length = A[0].length <= 100
# A[i][j] == 0 or A[i][j] == 1
# 
# 
# 
# 
# 
# 
# 
#
from collections import deque

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        print(source, target)
        queue = deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target:
                return d - 1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)
            

        

