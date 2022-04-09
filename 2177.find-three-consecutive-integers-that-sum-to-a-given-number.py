#
# @lc app=leetcode id=2177 lang=python3
#
# [2177] Find Three Consecutive Integers That Sum to a Given Number
#

# @lc code=start
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0: return []
        a = num // 3
        return [a - 1, a, a + 1]
        
# @lc code=end

