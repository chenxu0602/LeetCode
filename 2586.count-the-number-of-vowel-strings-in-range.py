#
# @lc app=leetcode id=2586 lang=python3
#
# [2586] Count the Number of Vowel Strings in Range
#

# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        vowels = set("aeiou")
        return sum({w[0], w[-1]}.issubset(vowels) for w in words[left:right + 1])
        
# @lc code=end

