#
# @lc app=leetcode id=2475 lang=python3
#
# [2475] Number of Unequal Triplets in Array
#

# @lc code=start
import itertools 
from collections import Counter

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:

        # O(n)

        # count[v] counts the frequency of element a we have seen.
        # pairs is the number of pairwise distinct pairs
        # count[v] * (i - count[v])  --  distinct pairs that contains v
        # pairs - count[v] * (i - count[v])  --  distinct pairs that do not contain v
        # trips is the number of pairwise distinct triplet.
        trips = pairs = 0
        count = Counter()
        for i, v in enumerate(nums):
            trips += pairs - count[v] * (i - count[v])
            pairs += i - count[v]
            count[v] += 1

        return trips

        
        

# @lc code=end

