#
# @lc app=leetcode id=3280 lang=python3
#
# [3280] Convert Date to Binary
#

# @lc code=start
class Solution:
    def convertDateToBinary(self, date: str) -> str:

        return '-'.join(map(lambda x: bin(int(x))[2:], date.split('-')))
        
# @lc code=end

