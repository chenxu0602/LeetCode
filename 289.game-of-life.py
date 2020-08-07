#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (50.90%)
# Likes:    1380
# Dislikes: 240
# Total Accepted:    153.8K
# Total Submissions: 301.8K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
# 
# Example:
# 
# 
# Input: 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output: 
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Rule 1: Any live cell with fewer than two live neighbors dies, as if caused by under-population. Hence, change the value of cell to -1. This means the cell was live before but now dead.
        # Rule 2: Any live cell with two or three live neighbors lives on to the next generation. Hence, no change in the value.
        # Rule 3: Any live cell with more than three live neighbors dies, as if by over-population. Hence, change the value of cell to -1. This means the cell was live before but now dead. Note that we don't need to differentiate between the rule 1 and 3. The start and end values are the same. Hence, we use the same dummy value.
        # Rule 4: Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. Hence, change the value of cell to 2. This means the cell was dead before but now live.
        # Time  complexity: O(M x N)
        # Space complexity: O(1)
        # neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        # rows, cols = map(len, (board, board[0]))

        # for row in range(rows):
        #     for col in range(cols):
        #         live_neighbors = 0
        #         for neighbor in neighbors:
        #             r = row + neighbor[0]
        #             c = col + neighbor[1]

        #             if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
        #                 live_neighbors += 1

        #         if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
        #             board[row][col] = -1

        #         if board[row][col] == 0 and live_neighbors == 3:
        #             board[row][col] = 2

        # for row in range(rows):
        #     for col in range(cols):
        #         if board[row][col] > 0:
        #             board[row][col] = 1
        #         else:
        #             board[row][col] = 0



        # Infinite Board
        # we obtain only the live cells from the entire board and then apply the different rules using only the live cells and finally we update the board in-place. The only problem with this solution would be when the entire board cannot fit into memory. If that is indeed the case, then we would have to approach this problem in a different way. For that scenario, we assume that the contents of the matrix are stored in a file, one row at a time.
        def gameOfLifeInfinite(live):
            ctr = Counter((I, J)
                          for i, j in live
                          for I in range(i-1, i+2)
                          for J in range(j-1, j+2)
                          if I != i or J != j)
            return {ij
                    for ij in ctr
                    if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)
        
# @lc code=end

