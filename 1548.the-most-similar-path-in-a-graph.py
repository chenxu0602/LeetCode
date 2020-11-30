#
# @lc app=leetcode id=1548 lang=python3
#
# [1548] The Most Similar Path in a Graph
#
# https://leetcode.com/problems/the-most-similar-path-in-a-graph/description/
#
# algorithms
# Hard (55.40%)
# Likes:    76
# Dislikes: 39
# Total Accepted:    3.2K
# Total Submissions: 5.7K
# Testcase Example:  '5\n[[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]]\n' + '["ATL","PEK","LAX","DXB","HND"]\n' + '["ATL","DXB","HND","LAX"]'
#
# We have n cities and m bi-directional roads where roads[i] = [ai, bi]
# connects city ai with city bi. Each city has a name consisting of exactly 3
# upper-case English letters given in the string array names. Starting at any
# city x, you can reach any city y where y != x (i.e. the cities and the roads
# are forming an undirected connected graph).
# 
# You will be given a string array targetPath. You should find a path in the
# graph of the same length and with the minimum edit distance to targetPath.
# 
# You need to return the order of the nodes in the path with the minimum edit
# distance, The path should be of the same length of targetPath and should be
# valid (i.e. there should be a direct road between ans[i] and ans[i + 1]). If
# there are multiple answers return any one of them.
# 
# The edit distance is defined as follows:
# 
# 
# 
# Follow-up: If each node can be visited only once in the path, What should you
# change in your solution?
# 
# 
# Example 1:
# 
# 
# Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names =
# ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]
# Output: [0,2,4,2]
# Explanation: [0,2,4,2], [0,3,0,2] and [0,3,1,2] are accepted answers.
# [0,2,4,2] is equivalent to ["ATL","LAX","HND","LAX"] which has edit distance
# = 1 with targetPath.
# [0,3,0,2] is equivalent to ["ATL","DXB","ATL","LAX"] which has edit distance
# = 1 with targetPath.
# [0,3,1,2] is equivalent to ["ATL","DXB","PEK","LAX"] which has edit distance
# = 1 with targetPath.
# 
# 
# Example 2:
# 
# 
# Input: n = 4, roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], names =
# ["ATL","PEK","LAX","DXB"], targetPath =
# ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]
# Output: [0,1,0,1,0,1,0,1]
# Explanation: Any path in this graph has edit distance = 8 with targetPath.
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: n = 6, roads = [[0,1],[1,2],[2,3],[3,4],[4,5]], names =
# ["ATL","PEK","LAX","ATL","DXB","HND"], targetPath =
# ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
# Output: [3,4,5,4,3,2,1]
# Explanation: [3,4,5,4,3,2,1] is the only path with edit distance = 0 with
# targetPath.
# It's equivalent to ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 100
# m == roads.length
# n - 1 <= m <= (n * (n - 1) / 2)
# 0 <= ai, bi <= n - 1
# ai != bi 
# The graph is guaranteed to be connected and each pair of nodes may have at
# most one direct road.
# names.length == n
# names[i].length == 3
# names[i] consists of upper-case English letters.
# There can be two cities with the same name.
# 1 <= targetPath.length <= 100
# targetPath[i].length == 3
# targetPath[i] consists of upper-case English letters.
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        # dp[i][v] means the minimum edit distance for targetPath[:i+1] ending with city v.
        # dp[i][v] = min(dp[i-1][u] + edit_cost(v)) for all edges (u, v).
        
        # Time  complexity: O(N^2 x len(targetPath))
        # Space complexity: O(N x len(tp))
        # graph = defaultdict(list)
        # for u, v in roads:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # m = len(targetPath)
        # dp = [[m] * n for _ in range(m)]
        # prev = [[0] * n for _ in range(m)]

        # for i in range(n):
        #     dp[0][i] = names[i] != targetPath[0]

        # for i in range(1, m):
        #     for j in range(n):
        #         for k in graph[j]:
        #             if dp[i - 1][k] < dp[i][j]:
        #                 dp[i][j] = dp[i - 1][k]
        #                 prev[i][j] = k

        #         dp[i][j] += names[j] != targetPath[i]

        # path, min_dist = [0], m
        # for i in range(n):
        #     if dp[-1][i] < min_dist:
        #         min_dist = dp[-1][i]
        #         path[0] = i

        # for i in range(m - 1, 0, -1):
        #     j = prev[i][path[-1]]
        #     path.append(j)

        # return path[::-1]


        path_len = len(targetPath)
        graph = defaultdict(set)
        for road in roads:
            graph[road[0]].add(road[1])
            graph[road[1]].add(road[0])

        # since the first city in the path can be any of the n cities, add a
        # fictitious source city -1 to the graph to start from
        graph[-1] = set(range(n))

        # in a matrix, keep track of paths of length = path_length (columns)
        # that start from each of the n cities (rows)
        # each mat[row][col] contains the next city following city=row at path_index = col
        next_cities = [[-1] * path_len for _ in range(n)]

        queue = deque()
        queue.append((-1, -1))

        while queue:
            current_city, current_path_index = queue.popleft()
            if current_path_index == path_len - 1:
                ans, prev_index = [], path_len - 1
                while prev_index > -1:
                    ans.append(current_city)
                    # the previous city (at the previous index i) in the path
                    current_city = next_cities[current_city][prev_index]
                    prev_index -= 1
                # path was constructed from the last city on path
                return reversed(ans)

            # if we are not at the end of the path just yet, 
            # see what neighbors to visit at next index in the path
            for next_city in graph[current_city]:
                next_tuple = (next_city, current_path_index + 1)
                # don't visit if this city has been considered after the current at this index
                if next_cities[next_tuple[0]][next_tuple[1]] != -1: continue
                # record that we have been here and where we came from
                next_cities[next_tuple[0]][next_tuple[1]] = current_city
                # Now account for edit distance: it can only be 0 or 1
                if names[next_tuple[0]] == targetPath[next_tuple[1]]:
                    # when edit distance is 0, this city has priority for
                    # visiting next    
                    queue.appendleft(next_tuple)
                else:
                    queue.append(next_tuple)

        return []

            
                    

        
        
# @lc code=end

