#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#
# https://leetcode.com/problems/custom-sort-string/description/
#
# algorithms
# Medium (64.23%)
# Likes:    561
# Dislikes: 159
# Total Accepted:    50.6K
# Total Submissions: 78.8K
# Testcase Example:  '"cba"\n"abcd"'
#
# S and T are strings composed of lowercase letters. In S, no letter occurs
# more than once.
# 
# S was sorted in some custom order previously. We want to permute the
# characters of T so that they match the order that S was sorted. More
# specifically, if x occurs before y in S, then x should occur before y in the
# returned string.
# 
# Return any permutation of T (as a string) that satisfies this property.
# 
# 
# Example :
# Input: 
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b",
# and "a". 
# Since "d" does not appear in S, it can be at any position in T. "dcba",
# "cdba", "cbda" are also valid outputs.
# 
# 
# 
# 
# Note:
# 
# 
# S has length at most 26, and no character is repeated in S.
# T has length at most 200.
# S and T consist of lowercase letters only.
# 
# 
#

# @lc code=start
from collections import Counter, defaultdict

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        # count = Counter(T)
        # ans = []

        # for c in S:
        #     ans.append(c * count[c])
        #     count[c] = 0
        # for c in count:
        #     ans.append(c * count[c])

        # return "".join(ans)

#        return "".join(sorted(T, key=S.find))

        ordering = defaultdict(lambda: -1, ((v, k) for (k, v) in enumerate(S)))
        return "".join(sorted(T, key=ordering.__getitem__))
        
# @lc code=end

