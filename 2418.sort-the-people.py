#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        _, names = zip(*sorted(zip(heights, names), reverse=True))
        return list(names)
        
# @lc code=end

