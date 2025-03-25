#
# @lc app=leetcode id=3340 lang=python3
#
# [3340] Check Balanced String
#

# @lc code=start
class Solution:
    def isBalanced(self, num: str) -> bool:

        num = list(map(int, num))
        return sum(num[0:len(num):2]) == sum(num[1:len(num):2])
        
# @lc code=end

