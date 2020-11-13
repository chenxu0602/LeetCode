#
# @lc app=leetcode id=1397 lang=python3
#
# [1397] Find All Good Strings
#
# https://leetcode.com/problems/find-all-good-strings/description/
#
# algorithms
# Hard (37.80%)
# Likes:    159
# Dislikes: 84
# Total Accepted:    2.6K
# Total Submissions: 6.8K
# Testcase Example:  '2\n"aa"\n"da"\n"b"'
#
# Given the strings s1 and s2 of size n, and the string evil. Return the number
# of good strings.
# 
# A good string has size n, it is alphabetically greater than or equal to s1,
# it is alphabetically smaller than or equal to s2, and it does not contain the
# string evil as a substring. Since the answer can be a huge number, return
# this modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
# Output: 51 
# Explanation: There are 25 good strings starting with 'a':
# "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c':
# "ca","cc","cd",...,"cz" and finally there is one good string starting with
# 'd': "da". 
# 
# 
# Example 2:
# 
# 
# Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
# Output: 0 
# Explanation: All strings greater than or equal to s1 and smaller than or
# equal to s2 start with the prefix "leet", therefore, there is not any good
# string.
# 
# 
# Example 3:
# 
# 
# Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# s1.length == n
# s2.length == n
# s1 <= s2
# 1 <= n <= 500
# 1 <= evil.length <= 50
# All strings consist of lowercase English letters.
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        # Simple DFS with KMP
        # Time  complexity: O(n x len(evil))
        # Space complexity: O(max(n, len(evil)))
        def srange(a, b):
            yield from (chr(i) for i in range(ord(a), ord(b) + 1))

        def failure(pat):
            res = [0]
            i, target = 1, 0
            while i < len(pat):
                if pat[i] == pat[target]:
                    target += 1
                    res += target,
                    i += 1
                elif target:
                    target = res[target - 1]
                else:
                    res += 0,
                    i += 1
            return res

        @lru_cache(None)
        def dfs(idx, max_matched=0, lb=True, rb=True):
            # idx: current_idx_on_s1_&_s2, 
			# max_matched: nxt_idx_to_match_on_evil, 
			# lb, rb: is_left_bound, is_right_bound
            if max_matched == len(evil):
                return 0 # evil found, break

            if idx == n:
                return 1 # base case

            l = s1[idx] if lb else 'a'
            r = s2[idx] if rb else 'z'

            candidates = [*srange(l, r)]

            res = 0
            for i, c in enumerate(candidates):
                nxt_matched = max_matched
                while evil[nxt_matched] != c and nxt_matched:
                    nxt_matched = f[nxt_matched - 1]
                res += dfs(idx + 1, nxt_matched + (c == evil[nxt_matched]),
                    lb=(lb and i == 0), rb=(rb and i == len(candidates) - 1))

            return res

        f = failure(evil)
        return dfs(0) % (10**9 + 7)

        
# @lc code=end

