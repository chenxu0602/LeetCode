#
# @lc app=leetcode id=2171 lang=python3
#
# [2171] Removing Minimum Number of Magic Beans
#

# @lc code=start
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:

        return sum(beans) - max((len(beans) - i) * n for i, n in enumerate(sorted(beans)))
        
# @lc code=end

