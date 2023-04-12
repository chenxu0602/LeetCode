#
# @lc app=leetcode id=2609 lang=python3
#
# [2609] Find the Longest Balanced Substring of a Binary String
#

# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:

        st = ''
        for i in range(25):
            st = '0' + st + '1'
            if st not in s:
                return 2 * i
        
        return 50
        
# @lc code=end

