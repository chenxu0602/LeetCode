#
# @lc app=leetcode id=2866 lang=python3
#
# [2866] Beautiful Towers II
#

# @lc code=start
from itertools import accumulate

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:

        # n, ans = len(maxHeights), 0
        # for i in range(n):
        #     ans = max(ans,   sum(accumulate(maxHeights[i::-1], min))
        #                    + sum(accumulate(maxHeights[i:], min))
        #                    - maxHeights[i])     # double counted maxHeights[i]

        # return ans

        n = len(maxHeights)
        
        def f(nums):
            res = [0] * n
            stack = [-1]
            for i in range(n):
                while len(stack) > 1 and nums[stack[-1]] > nums[i]:
                    j = stack.pop()

                res[i] = res[stack[-1]] + (i - stack[-1]) * nums[i]
                stack += i,
            return res
        
        return max(pre + suf - a for pre, suf, a in zip(f(maxHeights), f(maxHeights[::-1])[::-1], maxHeights))

        
# @lc code=end

