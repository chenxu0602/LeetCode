#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (32.04%)
# Likes:    2303
# Dislikes: 121
# Total Accepted:    340.5K
# Total Submissions: 1M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False

        def backtrack(board, i, j, word):
            if len(word) == 0: return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False

            tmp = board[i][j]
            board[i][j] = '#'

            res = backtrack(board, i + 1, j, word[1:]) or backtrack(board, i - 1, j, word[1:]) \
                or backtrack(board, i, j + 1, word[1:]) or backtrack(board, i, j - 1, word[1:])

            board[i][j] = tmp

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(board, i, j, word):
                    return True

        return False

        
# @lc code=end

