#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (71.07%)
# Likes:    455
# Dislikes: 38
# Total Accepted:    32.9K
# Total Submissions: 46.2K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed, acyclic graph of N nodes.  Find all possible paths from
# node 0 to node N-1, and return them in any order.
# 
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
# 
# 
# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# Note:
# 
# 
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of
# nodes inside one path.
# 
#
class Solution:
    def __init__(self):
        self.memo = {}

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        N = len(graph)

        def solve(node):
            if node == N - 1:
                return [[N - 1]]
            ans = []
            for nei in graph[node]:
                for path in solve(nei):
                    ans.append([node] + path)
            return ans

        return solve(0)
        """

        self.memo = {len(graph) - 1: [[len(graph) - 1]]}

        def calc(N):
            if N in self.memo:
                return self.memo[N]
            ans = []
            for n in graph[N]:
                for path in calc(n):
                    ans.append([N] + path)
            self.memo[N] = ans
            return ans

        return calc(0)
        

