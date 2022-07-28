#
# @lc app=leetcode id=2342 lang=python3
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#

# @lc code=start
class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        d, res = {}, -1
        for num in nums:
            s = sum([int(digit) for digit in str(num)])
            if not s in d:
                d[s] = num
            else:
                res = max(res, d[s] + num)
                d[s] = max(d[s], num)

        return res
        
# @lc code=end

