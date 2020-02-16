#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (40.61%)
# Likes:    1356
# Dislikes: 81
# Total Accepted:    162.9K
# Total Submissions: 400.1K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# 
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
# 
# 
# Empty cells are indicated by the character '.'.
# 
# 
# A sudoku puzzle...
# 
# 
# ...and its solution numbers marked in red.
# 
# Note:
# 
# 
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
# 
# 
#

# @lc code=start
from collections import deque, defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        triples = defaultdict(set)
        to_be_visited = deque([])

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r//3, c//3)].add(board[r][c])
                else:
                    to_be_visited.append((r, c))

        def dfs():
            if not to_be_visited:
                return True
            r, c = to_be_visited[0]
            t = (r // 3, c // 3)

            for i in range(1, 10):
                if str(i) not in rows[r] and str(i) not in cols[c] and str(i) not in triples[t]:
                    board[r][c] = str(i)
                    rows[r].add(str(i))
                    cols[c].add(str(i))
                    triples[t].add(str(i))
                    to_be_visited.popleft()

                    if dfs():
                        return True
                    else:
                        board[r][c] = '.'
                        rows[r].discard(str(i))
                        cols[c].discard(str(i))
                        triples[t].discard(str(i))
                        to_be_visited.appendleft((r, c))

            return False

        dfs()
        
# @lc code=end

