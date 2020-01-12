#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#
# https://leetcode.com/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (33.61%)
# Likes:    237
# Dislikes: 225
# Total Accepted:    16.7K
# Total Submissions: 49.6K
# Testcase Example:  '"X"\n"L"'
#
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a
# move consists of either replacing one occurrence of "XL" with "LX", or
# replacing one occurrence of "RX" with "XR". Given the starting string start
# and the ending string end, return True if and only if there exists a sequence
# of moves to transform one string to the other.
# 
# Example:
# 
# 
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# 
# 
# Note:
# 
# 
# 1 <= len(start) = len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.
# 
# 
#
import operator, itertools

class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        """
        if start.replace('X', '') != end.replace('X', ''):
            return False

        for (symbol, op) in (('L', operator.ge), ('R', operator.le)):
            B = (i for i, c in enumerate(end) if c == symbol)
            for i, c in enumerate(start):
                if c == symbol and not op(i, next(B)):
                    return False
        return True
        """

        for (i, x), (j, y) in itertools.zip_longest(
            ((i, x) for i, x in enumerate(start) if x != 'X'),
            ((i, y) for i, y in enumerate(end) if y != 'X'),
            fillvalue = (None, None)):
            if x != y or (x == 'L' and i < j) or (x == 'R' and i > j):
                return False

        return True


        
        

