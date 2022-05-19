#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (77.67%)
# Likes:    1062
# Dislikes: 74
# Total Accepted:    84.8K
# Total Submissions: 108.8K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed acyclic graph of N nodes. Find all possible paths from node
# 0 to node N-1, and return them in any order.
# 
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
# 
# 
# Example:
# Input: [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of
# nodes inside one path.
# 
# 
#

# @lc code=start
from collections import deque
from functools import lru_cache

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Backtracking
        # Time  complexity: O(2^N x N)
        # Space complexity: O(2^N x N)
        # target, results = len(graph) - 1, []

        # def backtrack(currNode, path):
        #     if currNode == target:
        #         results.append(path)
        #         return

        #     for nextNode in graph[currNode]:
        #         backtrack(nextNode, path + [nextNode])

        # path = [0]
        # backtrack(0, path)

        # return results


        # Top-Down Dynamic Programming
        # Time  complexity: O(2^N x N)
        # Space complexity: O(2^N x N)
        target = len(graph) - 1

        @lru_cache(None)
        def allPathsToTarget(currNode):
            if currNode == target:
                return [[target]]

            results = []
            for nextNode in graph[currNode]:
                for path in allPathsToTarget(nextNode):
                    results.append([currNode] + path)
                    
            return results

        return allPathsToTarget(0)

        
# @lc code=end

