#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (37.87%)
# Likes:    1551
# Dislikes: 104
# Total Accepted:    208.8K
# Total Submissions: 550.7K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Using Depth First Search
        # Time  complexity: O(N) 
        # Space complexity: O(N) 
        # adj_list = defaultdict(list)

        # for dest, src in prerequisites:
        #     adj_list[src].append(dest)

        # topological_sorted_order = []
        # is_possible = True

        # color = {k: Solution.WHITE for k in range(numCourses)}
        # def dfs(node):
        #     nonlocal is_possible

        #     if not is_possible:
        #         return

        #     color[node] = Solution.GRAY

        #     if node in adj_list:
        #         for neighbor in adj_list[node]:
        #             if color[neighbor] == Solution.WHITE:
        #                 dfs(neighbor)
        #             elif color[neighbor] == Solution.GRAY:
        #                 is_possible = False

        #     color[node] = Solution.BLACK
        #     topological_sorted_order.append(node)

        # for vertex in range(numCourses):
        #     if color[vertex] == Solution.WHITE:
        #         dfs(vertex)

        # return topological_sorted_order[::-1] if is_possible else []


        # O(E + V)
        graph = defaultdict(list)
        v = [0] * numCourses

        for to, start in prerequisites:
            graph[start].append(to)
            v[to] += 1

        stack = deque(i for i, val in enumerate(v) if not val)

        res = []

        while stack:
            top = stack.pop()
            for node in graph[top]:
                v[node] -= 1
                if not v[node]:
                    stack.append(node)

            del graph[top]
            res.append(top)

        return res if not bool(graph) else []

# @lc code=end

