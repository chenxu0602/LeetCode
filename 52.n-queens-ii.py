#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (57.61%)
# Likes:    534
# Dislikes: 154
# Total Accepted:    135.5K
# Total Submissions: 234.9K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# Example:
# 
# 
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown
# below.
# [
# [".Q..",  // Solution 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // Solution 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:

        def valid(nums, n):
            for i in range(n):
                if nums[i] == nums[n] or abs(nums[n] - nums[i]) == n - i:
                    return False
            return True

        def backtrack(nums, index):
            if index == len(nums):
                self.res += 1
                return
            
            for i in range(len(nums)):
                nums[index] = i
                if valid(nums, index):
                    backtrack(nums, index + 1)

        self.res = 0
        backtrack([-1] * n, 0)
        return self.res
        
# @lc code=end

