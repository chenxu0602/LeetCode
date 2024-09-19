#
# @lc app=leetcode id=3256 lang=python3
#
# [3256] Maximum Value Sum by Placing Three Rooks I
#

# @lc code=start
from heapq import nlargest
from itertools import chain, combinations

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:


        # Take top3 elements in each row, 3n elements.
        # Take top3 elements in each col, 3m elements.
        # Take the intersection s of top3 in rows and top3 in cols.

        # Then take top 11 elements of s.
        # 11 elements must have at least 3 different cols and 3 different rows.


        m, n = map(len, (board, board[0]))
        rows = [nlargest(3, [(board[i][j], i, j) for j in range(n)]) for i in range(m)]
        cols = [nlargest(3, [(board[i][j], i, j) for i in range(m)]) for j in range(n)]
        s = nlargest(11, set(chain(*rows)) & set(chain(*cols)))
        return max(sum(a[0] for a in c) for c in combinations(s, 3) if len({a[1] for a in c}) == 3 and len({a[2] for a in c}) == 3)
        
# @lc code=end

