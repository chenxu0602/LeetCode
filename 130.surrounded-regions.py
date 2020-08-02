#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (25.31%)
# Likes:    1185
# Dislikes: 542
# Total Accepted:    186.7K
# Total Submissions: 734.8K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#

# @lc code=start
import itertools
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS (Depth-First Search)
        # Time/Space complexity: O(N)   N is the number of cells in the board.

        # if not board or not board[0]:
        #     return 

        # m, n = map(len, (board, board[0]))
        # borders = list(itertools.product(range(m), [0, n - 1])) \
        #         + list(itertools.product([0, m - 1], range(n)))

        # def dfs(board, r, c):
        #     if board[r][c] != 'O':
        #         return
        #     board[r][c] = 'E'
        #     if c < n - 1: dfs(board, r, c + 1)
        #     if r < m - 1: dfs(board, r + 1, c)
        #     if c > 0: dfs(board, r, c - 1)
        #     if r > 0: dfs(board, r - 1, c)

        # for r, c in borders:
        #     dfs(board, r, c)

        # for r in range(m):
        #     for c in range(n):
        #         if board[r][c] == 'O':
        #             board[r][c] = 'X'
        #         elif board[r][c] == 'E':
        #             board[r][c] = 'O'

        # BFS (Breath-First Search)
        # Time/Space complexity: O(N)   N is the number of cells in the board.

        if not board or not board[0]:
            return 

        m, n = map(len, (board, board[0]))
        borders = list(itertools.product(range(m), [0, n - 1])) \
                + list(itertools.product([0, m - 1], range(n)))

        def bfs(board, r, c):
            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                if board[r][c] != 'O':
                    continue
                board[r][c] = 'E'
                if c < n - 1: queue.append((r, c + 1))
                if r < m - 1: queue.append((r + 1, c))
                if c > 0: queue.append((r, c - 1))
                if r > 0: queue.append((r - 1, c))


        for r, c in borders:
            bfs(board, r, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
        
# @lc code=end

