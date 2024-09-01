#
# @lc app=leetcode id=3209 lang=python3
#
# [3209] Number of Subarrays With AND Value of K
#

# @lc code=start
from collections import Counter

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        cnts = Counter()
        total = 0
        for num in nums:
            cnts2 = Counter()
            cnts2[num] = 1
            for a, b in cnts.items():
                cnts2[a & num] += b 
            total += cnts2[k]
            cnts = cnts2 

        return total 
    
        
# @lc code=end

