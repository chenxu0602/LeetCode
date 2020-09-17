#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (49.38%)
# Likes:    522
# Dislikes: 57
# Total Accepted:    28.2K
# Total Submissions: 56.8K
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has
# piles[i] bananas.  The guards have gone and will come back in H hours.
# 
# Koko can decide her bananas-per-hour eating speed of K.  Each hour, she
# chooses some pile of bananas, and eats K bananas from that pile.  If the pile
# has less than K bananas, she eats all of them instead, and won't eat any more
# bananas during this hour.
# 
# Koko likes to eat slowly, but still wants to finish eating all the bananas
# before the guards come back.
# 
# Return the minimum integer K such that she can eat all the bananas within H
# hours.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: piles = [3,6,7,11], H = 8
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
# 
# 
# 
# Example 3:
# 
# 
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Binary Search
        # Time  complexity: O(NlogW), where N is the number of piles, and W is the maximum size of a pile.
        # Space complexity: O(1)
        def possible(K):
            return sum((p - 1) // K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
        
# @lc code=end

