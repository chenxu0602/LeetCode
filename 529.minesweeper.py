#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#
# https://leetcode.com/problems/minesweeper/description/
#
# algorithms
# Medium (53.45%)
# Likes:    329
# Dislikes: 334
# Total Accepted:    35.9K
# Total Submissions: 67K
# Testcase Example:  '[["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]\n' +
#
# Let's play the minesweeper game (Wikipedia, online game)!
# 
# You are given a 2D char matrix representing the game board. 'M' represents an
# unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a
# revealed blank square that has no adjacent (above, below, left, right, and
# all 4 diagonals) mines, digit ('1' to '8') represents how many mines are
# adjacent to this revealed square, and finally 'X' represents a revealed
# mine.
# 
# Now given the next click position (row and column indices) among all the
# unrevealed squares ('M' or 'E'), return the board after revealing this
# position according to the following rules:
# 
# 
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it
# to revealed blank ('B') and all of its adjacent unrevealed squares should be
# revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then
# change it to a digit ('1' to '8') representing the number of adjacent
# mines.
# Return the board when no more squares will be revealed.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# 
# [['E', 'E', 'E', 'E', 'E'],
# ⁠['E', 'E', 'M', 'E', 'E'],
# ⁠['E', 'E', 'E', 'E', 'E'],
# ⁠['E', 'E', 'E', 'E', 'E']]
# 
# Click : [3,0]
# 
# Output: 
# 
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'M', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
# 
# Explanation:
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# 
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'M', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
# 
# Click : [1,2]
# 
# Output: 
# 
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'X', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# The range of the input matrix's height and width is [1,50].
# The click position will only be an unrevealed square ('M' or 'E'), which also
# means the input board contains at least one clickable square.
# The input board won't be a stage when game is over (some mines have been
# revealed).
# For simplicity, not mentioned rules should be ignored in this problem. For
# example, you don't need to reveal all the unrevealed mines when the game is
# over, consider any cases that you will win the game or flag any squares.
# 
# 
#
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j, m, n = *click, len(board), len(board[0])
        def dfs(i, j):
            if board[i][j] == 'E':
                neis = [(x,y) for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)) if 0 <= x < m and 0 <= y < n]
                cnt = sum(board[x][y] == 'M' for x, y in neis)
                if not cnt:
                    board[i][j] = 'B'
                    for x, y in neis:
                        dfs(x, y)
                else:
                    board[i][j] = str(cnt)


        if board[i][j] == 'M':
            board[i][j] = 'X'
        else:
            dfs(i, j)

        return board

