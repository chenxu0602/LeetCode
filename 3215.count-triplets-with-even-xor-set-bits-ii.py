#
# @lc app=leetcode id=3215 lang=python3
#
# [3215] Count Triplets with Even XOR Set Bits II
#

# @lc code=start
from collections import Counter

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:

        c_a = Counter([(x.bit_count() % 2) for x in a])
        c_b = Counter([(x.bit_count() % 2) for x in b])
        c_c = Counter([(x.bit_count() % 2) for x in c])

        ans = 0
        ans += (c_a[0] * c_b[0] * c_c[0])
        ans += (c_a[1] * c_b[1] * c_c[0])
        ans += (c_a[1] * c_b[0] * c_c[1])
        ans += (c_a[0] * c_b[1] * c_c[1])

        return ans
        
# @lc code=end

