#
# @lc app=leetcode id=3017 lang=python3
#
# [3017] Count the Number of Houses at a Certain Distance II
#

# @lc code=start
from itertools import accumulate

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:

        x, y = min(x, y), max(x, y)
        A = [0] * n
        for i in range(1, n + 1):
            A[0] += 2
            A[min(i - 1, abs(i - y) + x)] -= 1
            A[min(n - i, abs(i - x) + 1 + n - y)] -= 1
            A[min(abs(i - x), abs(y - i) + 1)] += 1
            A[min(abs(i - x) + 1, abs(y - i))] += 1
            r = max(x - i, 0) + max(i - y, 0)
            A[r + (y - x + 0) // 2] -= 1
            A[r + (y - x + 1) // 2] -= 1

        return list(accumulate(A))
        
        
# @lc code=end

