#
# @lc app=leetcode id=1135 lang=python3
#
# [1135] Connecting Cities With Minimum Cost
#
# https://leetcode.com/problems/connecting-cities-with-minimum-cost/description/
#
# algorithms
# Medium (50.66%)
# Likes:    93
# Dislikes: 5
# Total Accepted:    4.4K
# Total Submissions: 8K
# Testcase Example:  '3\n[[1,2,5],[1,3,6],[2,3,1]]'
#
# There are N cities numbered from 1 to N.
# 
# You are given connections, where each connections[i] = [city1, city2, cost]
# represents the cost to connect city1 and city2 together.  (A connection is
# bidirectional: connecting city1 and city2 is the same as connecting city2 and
# city1.)
# 
# Return the minimum cost so that for every pair of cities, there exists a path
# of connections (possibly of length 1) that connects those two cities
# together.  The cost is the sum of the connection costs used. If the task is
# impossible, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
# Output: 6
# Explanation: 
# Choosing any 2 edges will connect all cities so we choose the minimum 2.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: N = 4, connections = [[1,2,3],[3,4,4]]
# Output: -1
# Explanation: 
# There is no way to connect all cities even if all edges are used.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10000
# 1 <= connections.length <= 10000
# 1 <= connections[i][0], connections[i][1] <= N
# 0 <= connections[i][2] <= 10^5
# connections[i][0] != connections[i][1]
# 
# 
#

# @lc code=start
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # Kruskal’s Minimum Spanning Tree Algorithm with Union Find
        # O((E + V) x logV)
        parents = list(range(N))
        ranks = [1] * N

        def find(u):
            while u != parents[u]:
                parents[u] = parents[parents[u]]
                u = parents[u]
            return u

        def union(u, v):
            root_u, root_v = find(u), find(v)
            if root_u == root_v: return False
            if ranks[root_v] > ranks[root_u]:
                root_u, root_v = root_v, root_u
            parents[root_v] = root_u
            ranks[root_u] += ranks[root_v]
            return True

        connections.sort(key=lambda x: x[2])
        ans = 0
        for u, v, val in connections:
            if union(u-1, v-1):
                ans += val

        groups = len({find(x) for x in parents})
        return ans if groups == 1 else -1
        
# @lc code=end

