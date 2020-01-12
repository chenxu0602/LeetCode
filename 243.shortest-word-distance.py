#
# @lc app=leetcode id=243 lang=python3
#
# [243] Shortest Word Distance
#
# https://leetcode.com/problems/shortest-word-distance/description/
#
# algorithms
# Easy (58.09%)
# Likes:    319
# Dislikes: 30
# Total Accepted:    78K
# Total Submissions: 132.4K
# Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"coding"\n"practice"'
#
# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
# 
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# 
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# 
# 
# 
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# 
# 
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are
# both in the list.
# 
#

# @lc code=start
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:

        last_w1, last_w2, distance = None, None, len(words)

        for i, w in enumerate(words):
            if w == word1:
                if last_w2 is not None and i - last_w2 < distance:
                    distance = i - last_w2
                last_w1 = i

            if w == word2:
                if last_w1 is not None and i - last_w1 < distance:
                    distance= i - last_w1
                last_w2 = i

        return distance

        
# @lc code=end

