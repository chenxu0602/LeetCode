#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows  = [{} for _ in range(9)]
        # cols  = [{} for _ in range(9)]
        # boxes = [{} for _ in range(9)]

        # for i in range(9):
        #     for j in range(9):
        #         num = board[i][j]
        #         if num != '.':
        #             num = int(num)
        #             box_index = (i // 3) * 3 + j // 3

        #             rows[i][num] = rows[i].get(num, 0) + 1
        #             cols[j][num] = cols[j].get(num, 0) + 1
        #             boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

        #             if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
        #                 return False


        # return True

        rows  = [{} for _ in range(9)]
        cols  = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                        return False

        return True


