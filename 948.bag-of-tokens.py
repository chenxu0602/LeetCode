#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#
# https://leetcode.com/problems/bag-of-tokens/description/
#
# algorithms
# Medium (40.72%)
# Likes:    253
# Dislikes: 197
# Total Accepted:    13.9K
# Total Submissions: 33.9K
# Testcase Example:  '[100]\n50'
#
# You have an initial power P, an initial score of 0 points, and a bag of
# tokens.
# 
# Each token can be used at most once, has a value token[i], and has
# potentially two ways to use it.
# 
# 
# If we have at least token[i] power, we may play the token face up, losing
# token[i] power, and gaining 1 point.
# If we have at least 1 point, we may play the token face down, gaining
# token[i] power, and losing 1 point.
# 
# 
# Return the largest number of points we can have after playing any number of
# tokens.
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
# Input: tokens = [100], P = 50
# Output: 0
# 
# 
# 
# Example 2:
# 
# 
# Input: tokens = [100,200], P = 150
# Output: 1
# 
# 
# 
# Example 3:
# 
# 
# Input: tokens = [100,200,300,400], P = 200
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# tokens.length <= 1000
# 0 <= tokens[i] < 10000
# 0 <= P < 10000
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        # Greedy
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        tokens.sort()
        queue = deque(tokens)
        ans = bns = 0
        while queue and (P >= queue[0] or bns):
            while queue and P >= queue[0]:
                P -= queue.popleft()
                bns += 1
            ans = max(ans, bns)

            if queue and bns:
                P += queue.pop()
                bns -= 1

        return ans
        
# @lc code=end

