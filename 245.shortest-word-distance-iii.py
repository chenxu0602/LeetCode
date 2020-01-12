#
# @lc app=leetcode id=245 lang=python3
#
# [245] Shortest Word Distance III
#
# https://leetcode.com/problems/shortest-word-distance-iii/description/
#
# algorithms
# Medium (53.87%)
# Likes:    144
# Dislikes: 60
# Total Accepted:    43K
# Total Submissions: 79.2K
# Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"makes"\n"coding"'
#
# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
# 
# word1 and word2 may be the same and they represent two individual words in
# the list.
# 
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# 
# Input: word1 = “makes”, word2 = “coding”
# Output: 1
# 
# 
# 
# Input: word1 = "makes", word2 = "makes"
# Output: 3
# 
# 
# Note:
# You may assume word1 and word2 are both in the list.
# 
#

# @lc code=start
class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        
# @lc code=end

