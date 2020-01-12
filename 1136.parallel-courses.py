#
# @lc app=leetcode id=1136 lang=python3
#
# [1136] Parallel Courses
#
# https://leetcode.com/problems/parallel-courses/description/
#
# algorithms
# Hard (59.05%)
# Likes:    39
# Dislikes: 3
# Total Accepted:    2.2K
# Total Submissions: 3.6K
# Testcase Example:  '3\n[[1,3],[2,3]]'
#
# There are N courses, labelled from 1 to N.
# 
# We are given relations[i] = [X, Y], representing a prerequisite relationship
# between course X and course Y: course X has to be studied before course Y.
# 
# In one semester you can study any number of courses as long as you have
# studied all the prerequisites for the course you are studying.
# 
# Return the minimum number of semesters needed to study all courses.  If there
# is no way to study all the courses, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: N = 3, relations = [[1,3],[2,3]]
# Output: 2
# Explanation: 
# In the first semester, courses 1 and 2 are studied. In the second semester,
# course 3 is studied.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: N = 3, relations = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: 
# No course can be studied because they depend on each other.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 5000
# 1 <= relations.length <= 5000
# relations[i][0] != relations[i][1]
# There are no repeated relations in the input.
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        indegree = [0] * (N+1)
        graph = defaultdict(list)

        for pre, post in relations:
            indegree[post] += 1
            graph[pre].append(post)

        init = [(i, 1) for i, c in enumerate(indegree[1:], 1) if c == 0]
        sem, completed, queue = 1, 0, deque(init)
        while queue:
            nxt, _sem = queue.popleft()
            sem = max(sem, _sem)
            for out in graph[nxt]:
                indegree[out] -= 1
                if indegree[out] == 0:
                    queue.append((out, _sem+1))
            completed += 1

        return sem if completed == N else -1

        
# @lc code=end

