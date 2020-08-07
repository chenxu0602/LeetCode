#
# @lc app=leetcode id=254 lang=python3
#
# [254] Factor Combinations
#
# https://leetcode.com/problems/factor-combinations/description/
#
# algorithms
# Medium (44.77%)
# Likes:    460
# Dislikes: 20
# Total Accepted:    60.3K
# Total Submissions: 133.3K
# Testcase Example:  '1'
#
# Numbers can be regarded as product of its factors. For example,
# 
# 
# 8 = 2 x 2 x 2;
# ⁠ = 2 x 4.
# 
# 
# Write a function that takes an integer n and return all possible combinations
# of its factors.
# 
# Note:
# 
# 
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# 
# 
# Example 1: 
# 
# 
# Input: 1
# Output: []
# 
# 
# Example 2: 
# 
# 
# Input: 37
# Output:[]
# 
# Example 3: 
# 
# 
# Input: 12
# Output:
# [
# ⁠ [2, 6],
# ⁠ [2, 2, 3],
# ⁠ [3, 4]
# ]
# 
# Example 4: 
# 
# 
# Input: 32
# Output:
# [
# ⁠ [2, 16],
# ⁠ [2, 2, 8],
# ⁠ [2, 2, 2, 4],
# ⁠ [2, 2, 2, 2, 2],
# ⁠ [2, 4, 4],
# ⁠ [4, 8]
# ]
# 
# 
#

# @lc code=start
from math import sqrt 

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        # O(N^(logN))

        # self.res = []
        # def dfs(path, cur, biggest):
        #     for i in range(biggest, int(sqrt(cur)) + 1):
        #         if cur % i == 0:
        #             dfs(path + [i], cur // i, i)

        #     if path:
        #         self.res.append(path + [cur])

        # dfs([], n, 2)
        # return self.res


        def dfs(n, i, path, paths):
            while i * i <= n:
                if n % i == 0:
                    paths += path + [i, n // i],
                    dfs(n // i, i, path + [i], paths)
                i += 1
            return paths

        return dfs(n, 2, [], [])
        
# @lc code=end

