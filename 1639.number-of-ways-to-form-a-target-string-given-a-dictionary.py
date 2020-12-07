#
# @lc app=leetcode id=1639 lang=python3
#
# [1639] Number of Ways to Form a Target String Given a Dictionary
#
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/
#
# algorithms
# Hard (39.08%)
# Likes:    103
# Dislikes: 5
# Total Accepted:    3.1K
# Total Submissions: 8K
# Testcase Example:  '["acca","bbbb","caca"]\n"aba"'
#
# You are given a list of strings of the same length words and a string
# target.
# 
# Your task is to form target using the given words under the following
# rules:
# 
# 
# target should be formed from left to right.
# To form the i^th character (0-indexed) of target, you can choose the k^th
# character of the j^th string in words if target[i] = words[j][k].
# Once you use the k^th character of the j^th string of words, you can no
# longer use the x^th character of any string in words where x <= k. In other
# words, all characters to the left of or at index k become unusuable for every
# string.
# Repeat the process until you form the string target.
# 
# 
# Notice that you can use multiple characters from the same string in words
# provided the conditions above are met.
# 
# Return the number of ways to form target from words. Since the answer may be
# too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: words = ["acca","bbbb","caca"], target = "aba"
# Output: 6
# Explanation: There are 6 ways to form target.
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
# 
# 
# Example 2:
# 
# 
# Input: words = ["abba","baab"], target = "bab"
# Output: 4
# Explanation: There are 4 ways to form target.
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
# "bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
# "bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
# 
# 
# Example 3:
# 
# 
# Input: words = ["abcd"], target = "abcd"
# Output: 1
# 
# 
# Example 4:
# 
# 
# Input: words = ["abab","baba","abba","baab"], target = "abba"
# Output: 16
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# All strings in words have the same length.
# 1 <= target.length <= 1000
# words[i] and target contain only lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter
from functools import lru_cache

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # O(m x n)
        # MOD = 10**9 + 7
        # m, n = len(words[0]), len(target)
        # charAtIndexCnt = [[0] * m for _ in range(128)]
        # for word in words:
        #     for i, c in enumerate(word):
        #         charAtIndexCnt[ord(c)][i] += 1

        # @lru_cache(None)
        # def dp(k, i):
        #     if i == n: return 1
        #     if k == m: return 0
        #     c = target[i]
        #     ans = dp(k + 1, i) # Skip the kth index words
        #     if charAtIndexCnt[ord(c)][k] > 0:
        #         ans += dp(k + 1, i + 1) * charAtIndexCnt[ord(c)][k]
        #         ans %= MOD
        #     return ans

        # return dp(0, 0)



        # res[j] means the number of ways to form target j first characters
        # Time  complexity: O(S(W + N))
        # Space compleixty: O(N + S)
        # where N = target.length
        # S = words[i].length
        # W = words.length
        n, MOD = len(target), 10**9 + 7
        res = [1] + [0] * n
        for i in range(len(words[0])):
            count = Counter(w[i] for w in words)
            for j in range(n - 1, -1, -1):
                res[j + 1] += res[j] * count[target[j]] % MOD
        return res[n] % MOD


        
# @lc code=end

