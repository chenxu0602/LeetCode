#
# @lc app=leetcode id=3257 lang=python3
#
# [3257] Maximum Value Sum by Placing Three Rooks II
#

# @lc code=start
from heapq import nlargest
from itertools import chain, combinations

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:

        m, n = map(len, (board, board[0]))
        rows = [nlargest(3, [(board[i][j], i, j) for j in range(n)]) for i in range(m)]
        cols = [nlargest(3, [(board[i][j], i, j) for i in range(m)]) for j in range(n)]
        s = nlargest(11, set(chain(*rows)) & set(chain(*cols)))
        return max(sum(a[0] for a in c) for c in combinations(s, 3) if len({a[1] for a in c}) == 3 and len({a[2] for a in c}) == 3)
        
# @lc code=end

