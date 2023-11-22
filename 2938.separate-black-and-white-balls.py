#
# @lc app=leetcode id=2938 lang=python3
#
# [2938] Separate Black and White Balls
#

# @lc code=start
class Solution:
    def minimumSteps(self, s: str) -> int:

        # The problem is equivalent to determining the number of swaps to move all 0s to the left.
        # Thus, that number of moves is the difference between the sum of the indices of the 0s' in their present positions and the sum of the indices of the same count of the leftmost positions in the string.
        # indices = [i for i, v in enumerate(s) if v == '0']
        # sm, cnt = sum(indices), len(indices)
        # return sm - cnt * (cnt - 1) // 2


        # Every 0 should be swapped with every 1 before it. So we count numbers of 1 (swaps variable) and when meet next 0 just add to result number of previous 1s.
        res, swaps = 0, 0
        for c in s:
            if c == '1':
                swaps += 1
            else:
                res += swaps

        return res
        
# @lc code=end

