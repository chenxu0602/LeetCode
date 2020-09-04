#
# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#
# https://leetcode.com/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (34.77%)
# Likes:    407
# Dislikes: 356
# Total Accepted:    28.2K
# Total Submissions: 81K
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
# 
# Constraints:
# 
# 
# 1 <= len(start) == len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.
# 
# 
#

# @lc code=start
import operator, itertools

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # if start.replace('X', '') != end.replace('X', ''):
        #     return False

        # for sym, op in ('L', operator.ge), ('R', operator.le):
        #     B = (i for i, c in enumerate(end) if c == sym)
        #     for i, c in enumerate(start):
        #         if c == sym and not op(i, next(B)):
        #             return False

        # return True


        # Time  complexity: O(N)
        # Space complexity: O(1)
        # if start.count('X') != end.count('X'):
        #     return False

        # n = len(start)
        # i = j = 0
        # while i < n and j < n:
        #     while i < n and start[i] == 'X':
        #         i += 1
        #     while j < n and end[j] == 'X':
        #         j += 1

        #     # i and j are the indices representing the next
        #     # occurrences of non-X characters
        #     if i == n or j == n:
        #         return i == n and j == n

        #     if start[i] != end[j]:
        #         return False

        #     if start[i] == 'L' and i < j:
        #         return False

        #     if start[i] == 'R' and i > j:
        #         return False

        #     i += 1; j += 1

        # return True


        
        for (i, x), (j, y) in itertools.zip_longest(
            ((i, x) for i, x in enumerate(start) if x != 'X'),
            ((j, y) for j, y in enumerate(end) if y != 'X'), fillvalue = (None, None)):

            if x != y or (x == 'L' and i < j) or (x == 'R' and i > j):
                return False

        return True


# @lc code=end

