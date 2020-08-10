#
# @lc app=leetcode id=320 lang=python3
#
# [320] Generalized Abbreviation
#
# https://leetcode.com/problems/generalized-abbreviation/description/
#
# algorithms
# Medium (51.87%)
# Likes:    418
# Dislikes: 70
# Total Accepted:    47.7K
# Total Submissions: 91.7K
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

# @lc code=start
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        # Backtracking
        # Time  complexity: O(n x 2^n)
        # All these recursive calls form a complete binary recursion tree with 2^n leaves and 2^n - 1 inner nodes.
        # For each leaf node, it needs O(n) time for converting builder to String; for each internal node, it needs only constant time. 
        # Space complexity: O(n)
        def backtrack(word, pos, cur, count, result):
            if len(word) == pos:
                result.append(cur + str(count) if count > 0 else cur)
            else:
                backtrack(word, pos + 1, cur, count + 1, result)
                backtrack(word, pos + 1, cur + (str(count) if count > 0 else "") + word[pos], 0, result)



        result = []
        backtrack(word, 0, "", 0, result)
        return result

        
# @lc code=end

