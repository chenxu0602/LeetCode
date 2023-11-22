#
# @lc app=leetcode id=2939 lang=python3
#
# [2939] Maximum Xor Product
#

# @lc code=start
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:

        # bt = 1
        # while bt < (1 << n):
        #     if a * b < (a ^ bt) * (b ^ bt):
        #         a ^= bt; b ^= bt
        #     bt <<= 1

        # return a * b % (10**9 + 7)


        mask = (1 << n) - 1
        d = (a ^ b) & mask
        MOD = 10**9 + 7
        a = (a | mask) & ~d 
        b = (b | mask) & ~d 

        if d == 0:
            return a * b % MOD

        h = 1 << (d.bit_length() - 1)
        return max((a ^ d) * b, a * (b ^ d), (a ^ d ^ h) * (b ^ h), (a ^ h) * (b ^ d ^ h)) % MOD
        
# @lc code=end

