#
# @lc app=leetcode id=2856 lang=python3
#
# [2856] Minimum Array Length After Pair Removals
#

# @lc code=start
from collections import Counter

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:

        # scount = Counter(nums)
        # arr = sorted([scount[num] for num in sorted(scount.keys())], key=lambda x: -x)
        # return (arr[0] - sum(arr[1:])) if arr[0] > sum(arr[1:]) else sum(arr) % 2

        n = ans = len(nums)
        i, j = 0, (n + 1) // 2

        while i < n // 2 and j < n:
            if nums[i] < nums[j]:
                ans -= 2

                i += 1

            j += 1

        return ans 
    
    
        
# @lc code=end

