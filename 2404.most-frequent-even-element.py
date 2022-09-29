#
# @lc app=leetcode id=2404 lang=python3
#
# [2404] Most Frequent Even Element
#

# @lc code=start
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        mp = {}
        val, freq = 10**6, 0
        for i in nums:
            if i % 2 == 0:
                mp[i] = mp.get(i, 0) + 1

                if mp[i] > freq or mp[i] == freq and i < val:
                    val, freq = i, mp[i]

        return -1 if freq == 0 else val

        
# @lc code=end

