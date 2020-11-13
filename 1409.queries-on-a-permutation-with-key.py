#
# @lc app=leetcode id=1409 lang=python3
#
# [1409] Queries on a Permutation With Key
#
# https://leetcode.com/problems/queries-on-a-permutation-with-key/description/
#
# algorithms
# Medium (81.09%)
# Likes:    143
# Dislikes: 272
# Total Accepted:    21.8K
# Total Submissions: 26.9K
# Testcase Example:  '[3,1,2,1]\n5'
#
# Given the array queries of positive integers between 1 and m, you have to
# process all queries[i] (from i=0 to i=queries.length-1) according to the
# following rules:
# 
# 
# In the beginning, you have the permutation P=[1,2,3,...,m].
# For the current i, find the position of queries[i] in the permutation P
# (indexing from 0) and then move this at the beginning of the permutation P.
# Notice that the position of queries[i] in P is the result for queries[i].
# 
# 
# Return an array containing the result for the given queries.
# 
# 
# Example 1:
# 
# 
# Input: queries = [3,1,2,1], m = 5
# Output: [2,1,2,1] 
# Explanation: The queries are processed as follow: 
# For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move 3
# to the beginning of P resulting in P=[3,1,2,4,5]. 
# For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move 1
# to the beginning of P resulting in P=[1,3,2,4,5]. 
# For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move 2
# to the beginning of P resulting in P=[2,1,3,4,5]. 
# For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move 1
# to the beginning of P resulting in P=[1,2,3,4,5]. 
# Therefore, the array containing the result is [2,1,2,1].  
# 
# 
# Example 2:
# 
# 
# Input: queries = [4,1,2,2], m = 4
# Output: [3,1,2,0]
# 
# 
# Example 3:
# 
# 
# Input: queries = [7,5,5,8,3], m = 8
# Output: [6,5,0,7,5]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m <= 10^3
# 1 <= queries.length <= m
# 1 <= queries[i] <= m
# 
#

# @lc code=start
class Fenwick:
    def __init__(self, n):
        sz = 1
        while sz <= n:
            sz *= 2
        self.size = sz
        self.data = [0] * sz

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        fenw = Fenwick(2 * m)
        vimap = {}

        for i in range(1, m + 1):
            fenw.add(i + m, 1)
            vimap[i] = i + m
        cur = m

        ans = []
        for q in queries:
            i = vimap.pop(q)
            rank = fenw.sum(i - 1)
            ans.append(rank)

            vimap[q] = cur
            fenw.add(i, -1)
            fenw.add(cur, 1)
            cur -= 1

        return ans
        
# @lc code=end

