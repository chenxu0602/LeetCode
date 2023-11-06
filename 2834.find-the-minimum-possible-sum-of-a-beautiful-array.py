#
# @lc app=leetcode id=2834 lang=python3
#
# [2834] Find the Minimum Possible Sum of a Beautiful Array
#

# @lc code=start
from itertools import chain

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:

        return sum(list(chain(range(1, target // 2 + 1), range(target, n + target // 2 + 1)))[:n])

        
# @lc code=end

