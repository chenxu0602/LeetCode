#
# @lc app=leetcode id=1735 lang=python3
#
# [1735] Count Ways to Make Array With Product
#
# https://leetcode.com/problems/count-ways-to-make-array-with-product/description/
#
# algorithms
# Hard (49.11%)
# Likes:    70
# Dislikes: 17
# Total Accepted:    1.7K
# Total Submissions: 3.5K
# Testcase Example:  '[[2,6],[5,1],[73,660]]'
#
# You are given a 2D integer array, queries. For each queries[i], where
# queries[i] = [ni, ki], find the number of different ways you can place
# positive integers into an array of size ni such that the product of the
# integers is ki. As the number of ways may be too large, the answer to the
# i^th query is the number of ways modulo 10^9 + 7.
# 
# Return an integer array answer where answer.length == queries.length, and
# answer[i] is the answer to the i^th query.
# 
# 
# Example 1:
# 
# 
# Input: queries = [[2,6],[5,1],[73,660]]
# Output: [4,1,50734910]
# Explanation: Each query is independent.
# [2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6],
# [2,3], [3,2], [6,1].
# [5,1]: There is 1 way to fill an array of size 5 that multiply to 1:
# [1,1,1,1,1].
# [73,660]: There are 1050734917 ways to fill an array of size 73 that multiply
# to 660. 1050734917 modulo 10^9 + 7 = 50734910.
# 
# 
# Example 2:
# 
# 
# Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# Output: [1,2,3,10,5]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= queries.length <= 10^4 
# 1 <= ni, ki <= 10^4
# 
# 
#

# @lc code=start
from collections import defaultdict
import math

class Solution:
    seive = list(range(10001))
    for i in range(2, 10001):
        if seive[i] == i:
            for j in range(i * i, 10001, i):
                seive[j] = i

    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        ans = []
        for n, k in queries:
            factors = defaultdict(int)
            while k > 1:
                factors[self.seive[k]] += 1
                k //= self.seive[k]

            cur = 1
            for f in factors.values():
                cur *= math.comb(f + n - 1, f)

            ans.append(cur % (10**9 + 7))

        return ans

        
# @lc code=end

