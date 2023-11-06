#
# @lc app=leetcode id=2829 lang=python3
#
# [2829] Determine the Minimum Sum of a k-avoiding Array
#

# @lc code=start
class Solution:
    def minimumSum(self, n: int, k: int) -> int:

        numSet = set()
        i = 1
        while len(numSet) < n:
            if k - i not in numSet:
                numSet.add(i)
            i += 1

        return sum(numSet)
        
# @lc code=end

