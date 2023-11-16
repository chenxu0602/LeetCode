#
# @lc app=leetcode id=2935 lang=python3
#
# [2935] Maximum Strong Pair XOR II
#

# @lc code=start
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        # Assume x >= y,
        # then x - y <= y
        # then x <= y * 2.

        # We use pref[p] to record the minimum a with a prefix p,
        # and use pref2[p] to record the maximum a with a prefix p.
        # The above condition become pref[x] <= pref2[y] * 2, where x and y is the prefix.

        res = 0
        for i in range(20, -1, -1):
            res <<= 1
            pref, pref2 = {}, {}
            for a in nums:
                p = a >> i
                if p not in pref:
                    pref[p] = pref2[p] = a
                pref[p] = min(pref[p], a)     # Only record the min and max values of the same prefix is enough
                pref2[p] = max(pref2[p], a)

            for x in pref:
                y = res ^ 1 ^ x   # x ^ y = res + '1'
                if x >= y and y in pref and pref[x] <= pref2[y] * 2:  
                    res |= 1
                    break

        return res
        
# @lc code=end

