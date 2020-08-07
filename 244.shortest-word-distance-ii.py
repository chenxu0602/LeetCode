#
# @lc app=leetcode id=244 lang=python3
#
# [244] Shortest Word Distance II
#
# https://leetcode.com/problems/shortest-word-distance-ii/description/
#
# algorithms
# Medium (48.48%)
# Likes:    249
# Dislikes: 93
# Total Accepted:    57.8K
# Total Submissions: 116.3K
# Testcase Example:  '["WordDistance","shortest","shortest"]\n' +
#
# Design a class which receives a list of words in the constructor, and
# implements a method that takes two words word1 and word2 and return the
# shortest distance between these two words in the list. Your method will be
# called repeatedly many times with different parameters. 
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
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are
# both in the list.
# 
#

# @lc code=start
from collections import defaultdict

class WordDistance:

    # O(N)

    def __init__(self, words: List[str]):
        self.locations = defaultdict(list)

        for i, w in enumerate(words):
            self.locations[w].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        loc1, loc2 = self.locations[word1], self.locations[word2]
        l1, l2 = 0, 0
        min_diff = float("inf")

        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1

        return min_diff
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
# @lc code=end

