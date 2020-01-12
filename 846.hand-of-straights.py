#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (49.83%)
# Likes:    319
# Dislikes: 47
# Total Accepted:    22.6K
# Total Submissions: 45.1K
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
# Note:
# 
# 
# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length
# 
# 
#
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if len(hand) % W:
            return False

        counter = Counter(hand)

        while counter:
            elem = min(counter)
            for k in range(elem, elem+W):
                if k not in counter:
                    return False
                counter[k] -= 1
                if not counter[k]:
                    del counter[k]
        return True
        

