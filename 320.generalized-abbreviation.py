#
# @lc app=leetcode id=320 lang=python3
#
# [320] Generalized Abbreviation
#
# https://leetcode.com/problems/generalized-abbreviation/description/
#
# algorithms
# Medium (48.82%)
# Likes:    282
# Dislikes: 28
# Total Accepted:    37.9K
# Total Submissions: 77.6K
# Testcase Example:  '"word"'
#
# Write a function to generate the generalized abbreviations of a word. 
# 
# Note: The order of the output does not matter.
# 
# Example:
# 
# 
# Input: "word"
# Output:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 
# 
# 
# 
#
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:

        """
        def dfs(word, pos, cur, count, result):
            if len(word) == pos:
                result.append(cur + str(count) if count > 0 else cur)
            else:
                dfs(word, pos + 1, cur, count + 1, result)
                dfs(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, result)


        result = []
        dfs(word, 0, '', 0, result)
        return result
        """

        def dfs(word, pos, cur, count):
            if pos == len(word):
                result.append(cur + str(count) if count > 0 else cur)
            else:
                dfs(word, pos + 1, cur, count + 1)
                dfs(word, pos + 1, (cur + str(count) if count > 0 else cur) + word[pos], 0)

        result = []
        dfs(word, 0, "", 0)
        return result
        

