#
# @lc app=leetcode id=2448 lang=python3
#
# [2448] Minimum Cost to Make Array Equal
#

# @lc code=start
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        """
        def f(x):
            return sum(abs(a - x) * c for a, c in zip(nums, cost))
        
        l, r = min(nums), max(nums)
        res = f(l)

        while l < r:
            x = (l + r) // 2
            y1, y2 = f(x), f(x + 1)
            res = min(y1, y2)
            if y1 < y2:
                r = x
            else:
                l = x + 1

        return res
        """

        # LC 462
        arr = sorted(zip(nums, cost))
        total, cnt = sum(cost), 0
        for num, c in arr:
            cnt += c
            if cnt > total // 2:
                target = num
                break
        
        return sum(c * abs(num - target) for num, c in arr)
        
# @lc code=end

