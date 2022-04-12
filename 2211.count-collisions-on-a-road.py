#
# @lc app=leetcode id=2211 lang=python3
#
# [2211] Count Collisions on a Road
#

# @lc code=start
class Solution:
    def countCollisions(self, directions: str) -> int:

        n = len(directions)
        res = carsFromRight = 0

        i = 0
        while i < n and directions[i] == 'L':
            i += 1

        for j in range(i, n):
            if directions[j] == 'R':
                carsFromRight += 1
            else:
                res += carsFromRight if directions[j] == 'S' else carsFromRight + 1
                carsFromRight = 0

        return res
        
# @lc code=end

