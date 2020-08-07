#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (40.77%)
# Likes:    2916
# Dislikes: 146
# Total Accepted:    327.8K
# Total Submissions: 801.9K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Backtracking
        # Time  complexity: O(E + V^2), where E is the number of dependencies, V is the number of courses.
        # Space complexity: O(E + V)
        # def isCyclic(currCourse, courseDict, path):
        #     """
        #     backtracking method to check that no cycle would be formed starting from currCourse
        #     """
        #     if path[currCourse]:
        #         return True

        #     path[currCourse] = True

        #     ret = False
        #     for child in courseDict[currCourse]:
        #         ret = isCyclic(child, courseDict, path)
        #         if ret: break

        #     path[currCourse] = False
        #     return ret


        # courseDict = defaultdict(list)

        # for relation in prerequisites:
        #     nextCourse, prevCourse = relation[0], relation[1]
        #     courseDict[prevCourse].append(nextCourse)

        # path = [False] * numCourses

        # for currCourse in range(numCourses):
        #     if isCyclic(currCourse, courseDict, path):
        #         return False
        # return True


        # Postorder DFS (Depth-First Search)
        # Time  complexity: O(E + V)
        # Space complexity: O(E + V)
        # def isCyclic(currCourse, courseDict, checked, path):
        #     if checked[currCourse]:
        #         return False

        #     if path[currCourse]:
        #         return True

        #     path[currCourse] = True

        #     ret = False
        #     for child in courseDict[currCourse]:
        #         ret = isCyclic(child, courseDict, checked, path)
        #         if ret: break

        #     path[currCourse] = False

        #     checked[currCourse] = True
        #     return ret

        # courseDict = defaultdict(list)

        # for relation in prerequisites:
        #     nextCourse, prevCourse = relation[0], relation[1]
        #     courseDict[prevCourse].append(nextCourse)

        # checked = [False] * numCourses
        # path = [False] * numCourses

        # for currCourse in range(numCourses):
        #     if isCyclic(currCourse, courseDict, checked, path):
        #         return False
        # return True


        # Topological Sort
        # Time  complexity: O(E + V)
        # Space complexity: O(E + V)
        # There are two possible outcomes:
        # 1). If there are still some edges left in the graph, then these edges must have formed certain cycles, which is similar to the deadlock situation. It is due to these cyclic dependencies that we cannot remove them during the above processes.
        # 2). Otherwise, i.e. we have removed all the edges from the graph, and we got ourselves a topological order of the graph.
        graph = defaultdict(list)
        v = [0] * numCourses

        for to, start in prerequisites:
            graph[start].append(to)
            v[to] += 1

        stack = deque(i for i, val in enumerate(v) if not val)

        while stack:
            top = stack.pop()
            for node in graph[top]:
                v[node] -= 1
                if not v[node]:
                    stack.append(node)

            del graph[top]

        return not bool(graph)


        
# @lc code=end

