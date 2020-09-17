#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (54.01%)
# Likes:    728
# Dislikes: 85
# Total Accepted:    51.9K
# Total Submissions: 95.6K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice has a hand of cards, given as an array of integers.
# 
# Now she wants to rearrange the cards into groups so that each group is size
# W, and consists of W consecutive cards.
# 
# Return true if and only if she can.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# 
# Example 2:
# 
# 
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length
# 
# Note: This question is the same as 1296:
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
#

# @lc code=start
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # Time  complexity: O(N x (N / W)), where N is the length of hand.
        # Space complexity: O(N)
        # count = Counter(hand)
        # while count:
        #     m = min(count)
        #     for k in range(m, m + W):
        #         v = count[k]
        #         if not v: return False
        #         if v == 1:
        #             del count[k]
        #         else:
        #             count[k] = v - 1
        # return True


        if len(hand) % W: return False
        count = Counter(hand)

        while count:
            m = min(count)
            num = count[m]
            for k in range(m, m + W):
                v = count[k]
                if v < num: return False
                if v == num:
                    del count[k]
                else:
                    count[k] = v - num

        return True

        
# @lc code=end

