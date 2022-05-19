#
# @lc app=leetcode id=1901 lang=python3
#
# [1901] Find a Peak Element II
#

# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        top, bottom = 0, len(mat) - 1
        while top < bottom:
            mid = (top + bottom) // 2
            if max(mat[mid]) > max(mat[mid + 1]):
                bottom = mid
            else:
                top = mid + 1

        return [bottom, mat[bottom].index(max(mat[bottom]))]


        
# @lc code=end

