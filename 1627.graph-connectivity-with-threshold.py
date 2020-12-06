#
# @lc app=leetcode id=1627 lang=python3
#
# [1627] Graph Connectivity With Threshold
#
# https://leetcode.com/problems/graph-connectivity-with-threshold/description/
#
# algorithms
# Hard (37.32%)
# Likes:    134
# Dislikes: 16
# Total Accepted:    4.6K
# Total Submissions: 12.3K
# Testcase Example:  '6\n2\n[[1,4],[2,5],[3,6]]'
#
# We have n cities labeled from 1 to n. Two different cities with labels x and
# y are directly connected by a bidirectional road if and only if x and y share
# a common divisor strictly greater than some threshold. More formally, cities
# with labels x and y have a road between them if there exists an integer z
# such that all of the following are true:
# 
# 
# x % z == 0,
# y % z == 0, and
# z > threshold.
# 
# 
# Given the two integers, n and threshold, and an array of queries, you must
# determine for each queries[i] = [ai, bi] if cities ai and bi are connected
# (i.e. there is some path between them).
# 
# Return an array answer, where answer.length == queries.length and answer[i]
# is true if for the i^th query, there is a path between ai and bi, or
# answer[i] is false if there is no path.
# 
# 
# Example 1:
# 
# 
# Input: n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
# Output: [false,false,true]
# Explanation: The divisors for each number:
# 1:   1
# 2:   1, 2
# 3:   1, 3
# 4:   1, 2, 4
# 5:   1, 5
# 6:   1, 2, 3, 6
# Using the underlined divisors above the threshold, only cities 3 and 6 share
# a common divisor, so they are the
# only ones directly connected. The result of each query:
# [1,4]   1 is not connected to 4
# [2,5]   2 is not connected to 5
# [3,6]   3 is connected to 6 through path 3--6
# 
# 
# Example 2:
# 
# 
# Input: n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
# Output: [true,true,true,true,true]
# Explanation: The divisors for each number are the same as the previous
# example. However, since the threshold is 0,
# all divisors can be used. Since all numbers share 1 as a divisor, all cities
# are connected.
# 
# 
# Example 3:
# 
# 
# Input: n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]
# Output: [false,false,false,false,false]
# Explanation: Only cities 2 and 4 share a common divisor 2 which is strictly
# greater than the threshold 1, so they are the only ones directly connected.
# Please notice that there can be multiple queries for the same pair of nodes
# [x, y], and that the query [x, y] is equivalent to the query [y, x].
# 
# 
# 
# Constraints:
# 
# 
# 2 <= n <= 10^4
# 0 <= threshold <= n
# 1 <= queries.length <= 10^5
# queries[i].length == 2
# 1 <= ai, bi <= cities
# ai != bi
# 
# 
#

# @lc code=start

class Union:
    def __init__(self, n):
        self.par = list(range(n))
        self.rnk = [0] * n
        self.siz = [1] * n

    def find(self, x):
        if not x == self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr: return False
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        self.siz[xr] += self.siz[yr]
        return True

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = Union(n + 1)
        for i in range(threshold + 1, n + 1):
            for j in range(i * 2, n + 1, i):
                uf.union(i, j)

        ans = []
        for x, y in queries:
            xr, yr = map(uf.find, (x, y))
            ans.append(xr == yr)
        return ans
        
# @lc code=end

