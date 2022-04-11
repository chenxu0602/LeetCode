#
# @lc app=leetcode id=2197 lang=python3
#
# [2197] Replace Non-Coprime Numbers in Array
#

# @lc code=start
import math 

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        res = []
        for x in nums:
            while True:
                g = math.gcd(res[-1] if res else 1, x)
                if g == 1: break
                x = math.lcm(x, res.pop())
            res.append(x)

        return res

        # stk = []
        # for num in nums:
        #     stk.append(num)
        #     while len(stk) > 1 and math.gcd(stk[-1], stk[-2]) > 1:
        #         stk.append(math.lcm(stk.pop(), stk.pop()))

        # return stk

        
# @lc code=end

