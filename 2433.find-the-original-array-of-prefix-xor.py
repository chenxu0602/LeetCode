#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#

# @lc code=start
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:

        """
        for i in range(len(pref) - 1, 0, -1):
            pref[i] ^= pref[i - 1]
        return pref
        """

        return map(xor, pref, [0] + pref[:-1])
        
# @lc code=end

