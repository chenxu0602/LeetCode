#
# @lc app=leetcode id=631 lang=python3
#
# [631] Design Excel Sum Formula
#
# https://leetcode.com/problems/design-excel-sum-formula/description/
#
# algorithms
# Hard (31.51%)
# Likes:    87
# Dislikes: 91
# Total Accepted:    4.2K
# Total Submissions: 13.1K
# Testcase Example:  '["Excel","get","set","get"]\n[[3,"C"],[1,"A"],[1,"A",1],[1,"A"]]'
#
# Your task is to design the basic function of Excel and implement the function
# of sum formula.  Specifically, you need to implement the following
# functions:
# 
# 
# 
# Excel(int H, char W): This is the constructor. The inputs represents the
# height and width of the Excel form. H is a positive integer, range from 1 to
# 26. It represents the height. W is a character range from 'A' to 'Z'. It
# represents that the width is the number of characters from 'A' to W. The
# Excel form content is represented by a height * width 2D integer array C, it
# should be initialized to zero. You should assume that the first row of C
# starts from 1, and the first column of C starts from 'A'.
# 
# 
# 
# void Set(int row, char column, int val): Change the value at C(row, column)
# to be val.
# 
# int Get(int row, char column): Return the value at C(row, column).
# 
# int Sum(int row, char column, List of Strings : numbers): This function
# calculate and set the value at C(row, column), where the value should be the
# sum of cells represented by numbers. This function return the sum result at
# C(row, column). This sum formula should exist until this cell is overlapped
# by another value or another sum formula.
# 
# numbers is a list of strings that each string represent a cell or a range of
# cells. If the string represent a single cell, then it has the following
# format : ColRow. For example, "F7" represents the cell at (7, F). 
# 
# If the string represent a range of cells, then it has the following format :
# ColRow1:ColRow2. The range will always be a rectangle, and ColRow1 represent
# the position of the top-left cell, and ColRow2 represents the position of the
# bottom-right cell. 
# 
# Example 1:
# 
# Excel(3,"C"); 
# // construct a 3*3 2D array with all zero.
# //   A B C
# // 1 0 0 0
# // 2 0 0 0
# // 3 0 0 0
# 
# Set(1, "A", 2);
# // set C(1,"A") to be 2.
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 0
# 
# Sum(3, "C", ["A1", "A1:B2"]);
# // set C(3,"C") to be the sum of value at C(1,"A") and the values sum of the
# rectangle range whose top-left cell is C(1,"A") and bottom-right cell is
# C(2,"B"). Return 4. 
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 4
# 
# Set(2, "B", 2);
# // set C(2,"B") to be 2. Note C(3, "C") should also be changed.
# //   A B C
# // 1 2 0 0
# // 2 0 2 0
# // 3 0 0 6
# 
# 
# 
# Note:
# 
# You could assume that there won't be any circular sum reference. For example,
# A1 = sum(B1) and B1 = sum(A1).
# ⁠The test cases are using double-quotes to represent a character.
# Please remember to RESET your class variables declared in class Excel, as
# static/class variables are persisted across multiple test cases. Please see
# here for more details.
# 
# 
#

# @lc code=start
from collections import Counter

class Excel:

    def __init__(self, H: int, W: str):
        self.M = [[{'v': 0, 'sum': None} for i in range(H)] for j in range(ord(W) - 64)]
        
    def set(self, r: int, c: str, v: int) -> None:
        self.M[r - 1][ord(c) - 65] = {'v': v, 'sum': None}
        
    def get(self, r: int, c: str) -> int:
        cell = self.M[r - 1][ord(c) - 65]
        if not cell['sum']:
            return cell['v']
        return sum(self.get(*pos) * cell['sum'][pos] for pos in cell['sum'])
        
    def sum(self, r: int, c: str, strs: List[str]) -> int:
        self.M[r - 1][ord(c) - 65]['sum'] = self.parse(strs)
        return self.get(r, c)

    def parse(self, strs):
        c = Counter()
        for s in strs:
            s, e = s.split(':')[0], s.split(':')[1] if ':' in s else s
            for i in range(int(s[1:]), int(e[1:]) + 1):
                for j in range(ord(s[0]) - 64, ord(e[0]) - 64 + 1):
                    c[(i, chr(j + 64))] += 1

        return c
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
# @lc code=end

