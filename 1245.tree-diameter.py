#
# @lc app=leetcode id=1245 lang=python3
#
# [1245] Tree Diameter
#
# https://leetcode.com/problems/tree-diameter/description/
#
# algorithms
# Medium (56.12%)
# Likes:    134
# Dislikes: 4
# Total Accepted:    4.3K
# Total Submissions: 7.7K
# Testcase Example:  '[[0,1],[0,2]]'
#
# Given an undirected tree, return its diameter: the number of edges in a
# longest path in that tree.
# 
# The tree is given as an array of edges where edges[i] = [u, v] is a
# bidirectional edge between nodes u and v.  Each node has labels in the set
# {0, 1, ..., edges.length}.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: edges = [[0,1],[0,2]]
# Output: 2
# Explanation: 
# A longest path of the tree is the path 1 - 0 - 2.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# Output: 4
# Explanation: 
# A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= edges.length < 10^4
# edges[i][0] != edges[i][1]
# 0 <= edges[i][j] <= edges.length
# The given edges form an undirected tree.
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        level = 0

        curr_level = {(u, None) for u, neighbors in graph.items() if len(neighbors) == 1}
        while curr_level:
            next_level = set()
            for u, pre in curr_level:
                for v in graph[u]:
                    if v != pre:
                        next_level.add((v, u))
            curr_level = next_level
            level += 1

        return max(level - 1, 0)
        
# @lc code=end

