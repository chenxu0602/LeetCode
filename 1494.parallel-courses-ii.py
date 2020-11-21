#
# @lc app=leetcode id=1494 lang=python3
#
# [1494] Parallel Courses II
#
# https://leetcode.com/problems/parallel-courses-ii/description/
#
# algorithms
# Hard (30.90%)
# Likes:    271
# Dislikes: 27
# Total Accepted:    5.2K
# Total Submissions: 16.8K
# Testcase Example:  '4\n[[2,1],[3,1],[1,4]]\n2'
#
# Given the integer n representing the number of courses at some university
# labeled from 1 to n, and the array dependencies where dependencies[i] = [xi,
# yi]  represents a prerequisite relationship, that is, the course xi must be
# taken before the course yi.  Also, you are given the integer k.
# 
# In one semester you can take at most k courses as long as you have taken all
# the prerequisites for the courses you are taking.
# 
# Return the minimum number of semesters to take all courses. It is guaranteed
# that you can take all courses in some way.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
# Output: 3 
# Explanation: The figure above represents the given graph. In this case we can
# take courses 2 and 3 in the first semester, then take course 1 in the second
# semester and finally take course 4 in the third semester.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
# Output: 4 
# Explanation: The figure above represents the given graph. In this case one
# optimal way to take all courses is: take courses 2 and 3 in the first
# semester and take course 4 in the second semester, then take course 1 in the
# third semester and finally take course 5 in the fourth semester.
# 
# 
# Example 3:
# 
# 
# Input: n = 11, dependencies = [], k = 2
# Output: 6
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 15
# 1 <= k <= n
# 0 <= dependencies.length <= n * (n-1) / 2
# dependencies[i].length == 2
# 1 <= xi, yi <= n
# xi != yi
# All prerequisite relationships are distinct, that is, dependencies[i] !=
# dependencies[j].
# The given graph is a directed acyclic graph.
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # NP with O(3^n)

        reqs = [0] * n
        for u, v in dependencies:
            reqs[v - 1] |= 1 << (u - 1)

        dp = [n] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            avail = []
            for v in range(n):
                if mask & (1 << v) == 0 and mask & reqs[v] == reqs[v]: # all prerequisites are done except for v
                    avail.append(v)

            for choice in itertools.combinations(avail, min(k, len(avail))):
                mask2 = mask
                for u in choice:
                    mask2 |= (1 << u)

                dp[mask2] = min(dp[mask2], 1 + dp[mask])

        return dp[-1]
        
# @lc code=end

