#
# @lc app=leetcode id=2354 lang=python3
#
# [2354] Number of Excellent Pairs
#

# @lc code=start
from collections import Counter

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        # The Inclusion-Exclusion Principle
        # bits(num1 OR num2) + bits(num1 AND num2) = bits(num1) + bits(num2)
        count = Counter(map(int.bit_count, set(nums)))
        return sum(count[a] * count[b] for a in count for b in count if a + b >= k)

        
# @lc code=end

