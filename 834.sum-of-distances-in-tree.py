#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#
# https://leetcode.com/problems/sum-of-distances-in-tree/description/
#
# algorithms
# Hard (43.49%)
# Likes:    884
# Dislikes: 36
# Total Accepted:    15K
# Total Submissions: 33.9K
# Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
#
# An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are
# given.
# 
# The ith edge connects nodes edges[i][0] and edges[i][1] together.
# 
# Return a list ans, where ans[i] is the sum of the distances between node i
# and all other nodes.
# 
# Example 1:
# 
# 
# Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: 
# Here is a diagram of the given tree:
# ⁠ 0
# ⁠/ \
# 1   2
# ⁠  /|\
# ⁠ 3 4 5
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
# 
# 
# Note: 1 <= N <= 10000
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        # Subtree Sum and Count
        # Time  complexity: O(N)
        # Space complexity: O(N)
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N
        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans
        
# @lc code=end

