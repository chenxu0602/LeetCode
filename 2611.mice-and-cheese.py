#
# @lc app=leetcode id=2611 lang=python3
#
# [2611] Mice and Cheese
#

# @lc code=start
import heapq

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:

        # Assume take all from the second array.
        # Check the difference sequence:
        # A[0] - B[0], A[1] - B[1], ...
        # Take k largest from the sequence and sum up.
        # Return the res = sum(B) + sum(k largest A[i]-B[i])

        return sum(reward2) + sum(heapq.nlargest(k, (a - b for a, b in zip(reward1, reward2))))
        
# @lc code=end

