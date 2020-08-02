#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (51.96%)
# Likes:    1186
# Dislikes: 60
# Total Accepted:    259.1K
# Total Submissions: 496.5K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#

# @lc code=start
from functools import reduce

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # def backtrack(first=1, curr=[]):
        #     if len(curr) == k:
        #         output.append(curr[:])
        #         return
        #     for i in range(first, n + 1):
        #         curr.append(i)
        #         backtrack(i + 1, curr)
        #         curr.pop()

        # output = []
        # backtrack()
        # return output


        # nums = list(range(1, k + 1)) + [n + 1]

        # output, j = [], 0
        # while j < k:
        #     output.append(nums[:k])

        #     j = 0
        #     while j < k and nums[j + 1] == nums[j] + 1:
        #         nums[j] = j + 1
        #         j += 1
        #     nums[j] += 1

        # return output



        if k == 0: return [[]]
        return [pre + [i] for i in range(k, n + 1) for pre in  self.combine(i - 1, k - 1)]


        # combs = [[]]
        # for _ in range(k):
        #     combs = [[i] + c for c in combs for i in range(1, c[0] if c else n + 1)]
        # return combs


        # return reduce(lambda C, _: [[i] + c for c in C for i in range(1, c[0] if c else n + 1)], range(k), [[]])
        
# @lc code=end

