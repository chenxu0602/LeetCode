#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#
# https://leetcode.com/problems/course-schedule-iv/description/
#
# algorithms
# Medium (43.90%)
# Likes:    288
# Dislikes: 15
# Total Accepted:    13.2K
# Total Submissions: 30.1K
# Testcase Example:  '2\r\n[[1,0]]\r\n[[0,1],[1,0]]\r'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have direct prerequisites, for example, to take course 0 you
# have first to take course 1, which is expressed as a pair: [1,0]
# 
# Given the total number of courses n, a list of direct prerequisite pairs and
# a list of queries pairs.
# 
# You should answer for each queries[i] whether the course queries[i][0] is a
# prerequisite of the course queries[i][1] or not.
# 
# Return a list of boolean, the answers to the given queries.
# 
# Please note that if course a is a prerequisite of course b and course b is a
# prerequisite of course c, then, course a is a prerequisite of course c.
# 
# 
# Example 1:
# 
# 
# Input: n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: course 0 is not a prerequisite of course 1 but the opposite is
# true.
# 
# 
# Example 2:
# 
# 
# Input: n = 2, prerequisites = [], queries = [[1,0],[0,1]]
# Output: [false,false]
# Explanation: There are no prerequisites and each course is independent.
# 
# 
# Example 3:
# 
# 
# Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# Output: [true,true]
# 
# 
# Example 4:
# 
# 
# Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
# Output: [false,true]
# 
# 
# Example 5:
# 
# 
# Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries =
# [[0,4],[4,0],[1,3],[3,0]]
# Output: [true,false,true,false]
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 100
# 0 <= prerequisite.length <= (n * (n - 1) / 2)
# 0 <= prerequisite[i][0], prerequisite[i][1] < n
# prerequisite[i][0] != prerequisite[i][1]
# The prerequisites graph has no cycles.
# The prerequisites graph has no repeated edges.
# 1 <= queries.length <= 10^4
# queries[i][0] != queries[i][1]
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Floyd–Warshall Algorithm 
        # Time  complexity: O(n^3)
        # Space complexity: O(n^2)
        # connected = [[False] * n for _ in range(n)]
        # for i, j in prerequisites:
        #     connected[i][j] = True

        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])

        # return [connected[i][j] for i, j in queries]


        # Topological sort
        # Time  complexity: O(P x N)
        # Space complexity: O(N^2)
        graph = defaultdict(list)
        in_degree = [0] * n
        pres = [set() for _ in range(n)]

        for pre, course in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
            pres[course].add(pre)

        queue = deque(course for course, degree in enumerate(in_degree) if degree == 0)

        while queue:
            pre = queue.popleft()
            for course in graph[pre]:
                pres[course] |= pres[pre]
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        return [pre in pres[course] for pre, course in queries]

        


        
# @lc code=end

