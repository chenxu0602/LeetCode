#
# @lc app=leetcode id=2595 lang=python3
#
# [2595] Number of Even and Odd Bits
#

# @lc code=start
class Solution:
    def evenOddBit(self, n: int) -> List[int]:

        return [(n & 0b10101010101).bit_count(), (n & 0b01010101010).bit_count()]
        
# @lc code=end

