#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

from collections import defaultdict, deque

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        """
        def could_place(d, row, col):
            return not (d in rows[row] or d in cols[col] or d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_numbers(row, col):
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)

                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
            

        n = 3
        N = n * n
        box_index = lambda i, j: (i // n) * n + j // n

        rows  = [defaultdict(int) for i in range(N)]
        cols  = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]

        for i in range(N):
            for j in range(N):
                num = board[i][j]
                if num != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        backtrack()
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

        


    
   
