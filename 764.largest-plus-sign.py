#
# @lc app=leetcode id=764 lang=python3
#
# [764] Largest Plus Sign
#
# https://leetcode.com/problems/largest-plus-sign/description/
#
# algorithms
# Medium (44.02%)
# Likes:    298
# Dislikes: 67
# Total Accepted:    14.7K
# Total Submissions: 33.3K
# Testcase Example:  '5\n[[4,2]]'
#
# 
# In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those
# cells in the given list mines which are 0.  What is the largest axis-aligned
# plus sign of 1s contained in the grid?  Return the order of the plus sign.
# If there is none, return 0.
# 
# An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1
# along with 4 arms of length k-1 going up, down, left, and right, and made of
# 1s.  This is demonstrated in the diagrams below.  Note that there could be 0s
# or 1s beyond the arms of the plus sign, only the relevant area of the plus
# sign is checked for 1s.
# 
# 
# Examples of Axis-Aligned Plus Signs of Order k:
# Order 1:
# 000
# 010
# 000
# 
# Order 2:
# 00000
# 00100
# 01110
# 00100
# 00000
# 
# Order 3:
# 0000000
# 0001000
# 0001000
# 0111110
# 0001000
# 0001000
# 0000000
# 
# 
# Example 1:
# Input: N = 5, mines = [[4, 2]]
# Output: 2
# Explanation:
# 11111
# 11111
# 11111
# 11111
# 11011
# In the above grid, the largest plus sign can only be order 2.  One of them is
# marked in bold.
# 
# 
# Example 2:
# Input: N = 2, mines = []
# Output: 1
# Explanation:
# There is no plus sign of order 2, but there is of order 1.
# 
# 
# Example 3:
# Input: N = 1, mines = [[0, 0]]
# Output: 0
# Explanation:
# There is no plus sign, so return 0.
# 
# 
# Note:
# N will be an integer in the range [1, 500].
# mines will have length at most 5000.
# mines[i] will be length 2 and consist of integers in the range [0, N-1].
# (Additionally, programs submitted in C, C++, or C# will be judged with a
# slightly smaller time limit.)
# 
#
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        # O(N^2 + N x |mines|)
        # g = [[min(i, N-i-1, j, N-j-1) + 1 for j in range(N)] for i in range(N)]
        # for x, y in mines:
        #     for i in range(N):
        #         g[i][y] = min(g[i][y], abs(i-x))
        #         g[x][i] = min(g[x][i], abs(i-y))
        # return max(max(row) for row in g)

        # O(N^2)
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0

        for r in range(N):
            count = 0
            for c in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count

            count = 0
            for c in range(N-1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

        for c in range(N):
            count = 0
            for r in range(N):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

            count = 0
            for r in range(N-1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

                if dp[r][c] > ans:
                    ans = dp[r][c]

        return ans
        

