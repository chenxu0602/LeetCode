#
# @lc app=leetcode id=691 lang=python3
#
# [691] Stickers to Spell Word
#
# https://leetcode.com/problems/stickers-to-spell-word/description/
#
# algorithms
# Hard (41.24%)
# Likes:    327
# Dislikes: 34
# Total Accepted:    12.8K
# Total Submissions: 30.9K
# Testcase Example:  '["with","example","science"]\n"thehat"'
#
# 
# We are given N different types of stickers.  Each sticker has a lowercase
# English word on it.
# 
# You would like to spell out the given target string by cutting individual
# letters from your collection of stickers and rearranging them.
# 
# You can use each sticker more than once if you want, and you have infinite
# quantities of each sticker.
# 
# What is the minimum number of stickers that you need to spell out the
# target?  If the task is impossible, return -1.
# 
# 
# Example 1:
# Input:
# ["with", "example", "science"], "thehat"
# 
# 
# Output:
# 3
# 
# 
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the
# target "thehat".
# Also, this is the minimum number of stickers necessary to form the target
# string.
# 
# 
# Example 2:
# Input:
# ["notice", "possible"], "basicbasic"
# 
# 
# Output:
# -1
# 
# 
# Explanation:
# We can't form the target "basicbasic" from cutting letters from the given
# stickers.
# 
# 
# Note:
# stickers has length in the range [1, 50].
# stickers consists of lowercase English words (without apostrophes).
# target has length in the range [1, 15], and consists of lowercase English
# letters.
# In all test cases, all words were chosen randomly from the 1000 most common
# US English words, and the target was chosen as a concatenation of two random
# words.
# The time limit may be more challenging than usual.  It is expected that a 50
# sticker test case can be solved within 35ms on average.
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Time  complexity: O(2^T x S x T) where S is the total number of letters in all stickers,
        # and T is the number of letters in the target word.
        # Space complexity: O(2^T)
        t_count = Counter(target)
        A = [Counter(sticker) & t_count for sticker in stickers]

        for i in range(len(A)-1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        stickers = ["".join(s_count.elements()) for s_count in A]
        dp = [-1] * (1 << len(target))
        dp[0] = 0
        for state in range(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break

                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]

        
# @lc code=end

