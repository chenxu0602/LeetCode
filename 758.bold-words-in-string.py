#
# @lc app=leetcode id=758 lang=python3
#
# [758] Bold Words in String
#
# https://leetcode.com/problems/bold-words-in-string/description/
#
# algorithms
# Easy (42.79%)
# Likes:    99
# Dislikes: 58
# Total Accepted:    8.1K
# Total Submissions: 18.8K
# Testcase Example:  '["ab","bc"]\n"aabcd"'
#
# 
# Given a set of keywords words and a string S, make all appearances of all
# keywords in S bold.  Any letters between <b> and </b> tags become bold.
# 
# The returned string should use the least number of tags possible, and of
# course the tags should form a valid combination.
# 
# 
# For example, given that words = ["ab", "bc"] and  S = "aabcd", we should
# return "a<b>abc</b>d".  Note that returning "a<b>a<b>b</b>c</b>d" would use
# more tags, so it is incorrect.
# 
# 
# Note:
# words has length in range [0, 50].
# words[i] has length in range [1, 10].
# S has length in range [0, 500].
# All characters in words[i] and S are lowercase letters.
# 
#
from itertools import groupby

class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        N = len(S)
        mask = [False] * N
        for i in range(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, min(i+len(word), N)):
                        mask[j] = True

        ans = []
        for incl, grp in groupby(zip(S, mask), lambda z: z[1]):
            if incl: ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl: ans.append("</b>")
        return "".join(ans)

        

