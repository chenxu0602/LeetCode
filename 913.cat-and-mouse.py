#
# @lc app=leetcode id=913 lang=python3
#
# [913] Cat and Mouse
#
# https://leetcode.com/problems/cat-and-mouse/description/
#
# algorithms
# Hard (29.06%)
# Likes:    210
# Dislikes: 48
# Total Accepted:    5.3K
# Total Submissions: 17.9K
# Testcase Example:  '[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]'
#
# A game on an undirected graph is played by two players, Mouse and Cat, who
# alternate turns.
# 
# The graph is given as follows: graph[a] is a list of all nodes b such that ab
# is an edge of the graph.
# 
# Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second,
# and there is a Hole at node 0.
# 
# During each player's turn, they must travel along one edge of the graph that
# meets where they are.  For example, if the Mouse is at node 1, it must travel
# to any node in graph[1].
# 
# Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)
# 
# Then, the game can end in 3 ways:
# 
# 
# If ever the Cat occupies the same node as the Mouse, the Cat wins.
# If ever the Mouse reaches the Hole, the Mouse wins.
# If ever a position is repeated (ie. the players are in the same position as a
# previous turn, and it is the same player's turn to move), the game is a
# draw.
# 
# 
# Given a graph, and assuming both players play optimally, return 1 if the game
# is won by Mouse, 2 if the game is won by Cat, and 0 if the game is a
# draw.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# Output: 0
# Explanation:
# 4---3---1
# |   |
# 2---5
# \ /
# 0
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= graph.length <= 50
# It is guaranteed that graph[1] is non-empty.
# It is guaranteed that graph[2] contains a non-zero element. 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        # Minimax / Percolate from Resolved States
        # m is the location of the mouse, c is the location of the cat, and t is 1 if it is the mouse's move, else 2.
        # Time  complexity: O(N^3)
        # Space complexity: O(N^2)
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 3 - t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3 - t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = defaultdict(int)

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m, c, 1] = len(graph[m])
                degree[m, c, 2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = deque([])
        for i in range(N):
            for t in range(1, 3):
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        # percolate
        while queue:
            # for nodes that are colored :
            i, j, t, c = queue.popleft()
            # for every parent of this node i, j, t :
            for i2, j2, t2 in parents(i, j, t):
                # if this parent is not colored :
                if color[i2, j2, t2] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c: # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]

        
# @lc code=end

