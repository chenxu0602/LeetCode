#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#
# https://leetcode.com/problems/friend-circles/description/
#
# algorithms
# Medium (58.39%)
# Likes:    2024
# Dislikes: 141
# Total Accepted:    176.9K
# Total Submissions: 301.5K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# There are N students in a class. Some of them are friends, while some are
# not. Their friendship is transitive in nature. For example, if A is a direct
# friend of B, and B is a direct friend of C, then A is an indirect friend of
# C. And we defined a friend circle is a group of students who are direct or
# indirect friends.
# 
# Given a N*N matrix M representing the friend relationship between students in
# the class. If M[i][j] = 1, then the ith and jth students are direct friends
# with each other, otherwise not. And you have to output the total number of
# friend circles among all the students.
# 
# Example 1:
# 
# 
# Input: 
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a
# friend circle. 
# The 2nd student himself is in a friend circle. So return 2.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd
# students are direct friends, 
# so the 0th and 2nd students are indirect friends. All of them are in the same
# friend circle, so return 1.
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= N <= 200
# M[i][i] == 1
# M[i][j] == M[j][i]
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # Depth First Search
        # Time  complexity: O(n^2)
        # Space complexity: O(n)
        def dfs(M, visited, i):
            for j in range(len(M[i])):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(M, visited, j)

        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(M, visited, i)
                count += 1

        return count


        # Union-Find Method
        # Time  complexity: O(n^2). We traverse over the complete matrix once. Union and find operations take O(n)O(n) time in the worst case.
        # Space complexity: O(n). parent array of size nn is used.
        # def find(i):
        #     if not parent[i] == i:
        #         parent[i] = find(parent[i])
        #     return parent[i]

        # def union(x, y):
        #     xr, yr = map(find, (x, y))
        #     if not xr == yr:
        #         parent[xr] = yr

        # parent = list(range(len(M)))
        # for i in range(len(M)):
        #     for j in range(len(M)):
        #         if M[i][j] == 1 and not i == j:
        #             union(i, j)

        # return sum(parent[i] == i for i in range(len(M)))

        # Breadth First Search
        # Time  complexity: O(n^2)
        # Space complexity: O(n)
        # visited = [0] * len(M)
        # count = 0
        # queue = deque()

        # for i in range(len(M)):
        #     if visited[i] == 0:
        #         queue.append(i)
        #         while queue:
        #             s = queue.popleft()
        #             visited[s] = 1
        #             for j in range(len(M)):
        #                 if M[s][j] == 1 and visited[j] == 0:
        #                     queue.append(j)

        #         count += 1
        # return count
        
# @lc code=end

