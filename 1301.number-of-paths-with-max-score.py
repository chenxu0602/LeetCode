#
# @lc app=leetcode id=1301 lang=python3
#
# [1301] Number of Paths with Max Score
#
# https://leetcode.com/problems/number-of-paths-with-max-score/description/
#
# algorithms
# Hard (36.34%)
# Likes:    73
# Dislikes: 4
# Total Accepted:    3K
# Total Submissions: 8.4K
# Testcase Example:  '["E23","2X2","12S"]\r'
#
# You are given a square board of characters. You can move on the board
# starting at the bottom right square marked with the character 'S'.
# 
# You need to reach the top left square marked with the character 'E'. The rest
# of the squares are labeled either with a numeric character 1, 2, ..., 9 or
# with an obstacle 'X'. In one move you can go up, left or up-left (diagonally)
# only if there is no obstacle there.
# 
# Return a list of two integers: the first integer is the maximum sum of
# numeric characters you can collect, and the second is the number of such
# paths that you can take to get that maximum sum, taken modulo 10^9 + 7.
# 
# In case there is no path, return [0, 0].
# 
# 
# Example 1:
# Input: board = ["E23","2X2","12S"]
# Output: [7,1]
# Example 2:
# Input: board = ["E12","1X1","21S"]
# Output: [4,2]
# Example 3:
# Input: board = ["E11","XXX","11S"]
# Output: [0,0]
# 
# 
# Constraints:
# 
# 
# 2 <= board.length == board[i].length <= 100
# 
#

# @lc code=start
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n, MOD = len(board), 10**9 + 7
        dp = [[[float("-inf"), 0] for _ in range(n + 1)] for _ in range(n + 1)]
        dp[n - 1][n - 1] = [0, 1]

        for x in range(n - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                if board[x][y] in "XS":
                    continue
                for i, j in (0, 1), (1, 0), (1, 1):
                    if dp[x][y][0] < dp[x + i][y + j][0]:
                        dp[x][y] = [dp[x + i][y + j][0], 0]
                    if dp[x][y][0] == dp[x + i][y + j][0]:
                        dp[x][y][1] += dp[x + i][y + j][1]

                dp[x][y][0] += int(board[x][y]) if x or y else 0

        return [dp[0][0][0] if dp[0][0][1] else 0, dp[0][0][1] % MOD]
        
# @lc code=end

