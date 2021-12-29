#
# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#
# https://leetcode.com/problems/bus-routes/description/
#
# algorithms
# Hard (42.43%)
# Likes:    822
# Dislikes: 22
# Total Accepted:    39.4K
# Total Submissions: 92.3K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus
# repeats forever. For example if routes[0] = [1, 5, 7], this means that the
# first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->...
# forever.
# 
# We start at bus stop S (initially not on a bus), and we want to go to bus
# stop T. Travelling by buses only, what is the least number of buses we must
# take to reach our destination? Return -1 if it is not possible.
# 
# 
# Example:
# Input: 
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation: 
# The best strategy is take the first bus to the bus stop 7, then take the
# second bus to the bus stop 6.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 10^5.
# 0 <= routes[i][j] < 10 ^ 6.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # Breadth First Search 
        # Time  complexity: Let NN denote the number of buses, and b_i the number of stops on the ith bus.
        # Creating the graph is O(N x Sum(b_i)) and search is O(N^2)
        # Space complexity: O(N^2 + sum(b_i))
        if S == T: return 0
        routes = list(map(set, routes))
        graph = defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))

        return -1
        
# @lc code=end

