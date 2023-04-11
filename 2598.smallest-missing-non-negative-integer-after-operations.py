#
# @lc app=leetcode id=2598 lang=python3
#
# [2598] Smallest Missing Non-negative Integer After Operations
#

# @lc code=start
from collections import Counter

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:

        """
        m = Counter([n % value for n in nums])
        for i in range(len(nums)):
            if m[i % value] == 0:
                return i

            m[i % value] -= 1
        return len(nums)
        """

        count = Counter(n % value for n in nums)
        stop = 0
        for i in range(value):
            if count[i] < count[stop]:
                stop = i

        return value * count[stop] + stop


        
# @lc code=end

