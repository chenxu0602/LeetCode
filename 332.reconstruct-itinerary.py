#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (33.91%)
# Likes:    1252
# Dislikes: 787
# Total Accepted:    117.9K
# Total Submissions: 347.5K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
# 
# Note:
# 
# 
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# 
# 
# Example 1:
# 
# 
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# 
# 
# Example 2:
# 
# 
# Input:
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Backtracking + Greedy
        # Time  complexity: O(E^d) where E is the number of total flights and is the maximum number of flights from an airporpt.
        # Space complexity: O(V + E) where V is the number of airports and E is the number of flights. 
        # self.flightMap = defaultdict(list)

        # for origin, dest in tickets:
        #     self.flightMap[origin].append(dest)

        # self.visitBitmap = {}

        # # sort the itinerary based on the lexical order
        # for origin, itinerary in self.flightMap.items():
        #     itinerary.sort()
        #     self.visitBitmap[origin] = [False] * len(itinerary)

        # def backtracking(origin, route):
        #     if len(route) == self.flights + 1:
        #         self.result = route
        #         return True

        #     for i, nextDest in enumerate(self.flightMap[origin]):
        #         if not self.visitBitmap[origin][i]:
        #             # mark the visit before the next recursion
        #             self.visitBitmap[origin][i] = True
        #             ret = backtracking(nextDest, route + [nextDest])
        #             self.visitBitmap[origin][i] = False
        #             if ret:
        #                 return True

        #     return False

        # self.flights = len(tickets)
        # self.result = []
        # route = ["JFK"]
        # backtracking("JFK", route)

        # return self.result
        


        # Hierholzer's Algorithm
        # In graph theory, an Eulerian trail (or Eulerian path) is a trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices).
        # Similarly, an Eulerian circuit or Eulerian cycle is an Eulerian trail that starts and ends on the same vertex.
        # Postorder DFS traversal
        # Time  complexity: O(E x log(E/V))
        # self.flightMap = defaultdict(list)

        # for origin, dest in tickets:
        #     self.flightMap[origin].append(dest)

        # for origin, itinerary in self.flightMap.items():
        #     itinerary.sort(reverse=True)

        # def dfs(origin):
        #     destList = self.flightMap[origin]
        #     while destList:
        #         #while we visit the edge, we trim it off from graph.
        #         nextDest = destList.pop()
        #         dfs(nextDest)
        #     self.result.append(origin)

        # self.result = [] 
        # dfs("JFK")
        # return self.result[::-1]



        # targets = defaultdict(list)
        # for a, b in sorted(tickets)[::-1]:
        #     targets[a] += b,

        # route = []
        # def visit(airport):
        #     while targets[airport]:
        #         visit(targets[airport].pop())
        #     route.append(airport)

        # visit("JFK")
        # return route[::-1]


        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,

        route, stack = [], ["JFK"]
        while stack:
            while targets[stack[-1]]:
                stack.append(targets[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]
# @lc code=end

