#
# @lc app=leetcode id=2452 lang=python3
#
# [2452] Words Within Two Edits of Dictionary
#

# @lc code=start
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        words = []
        for q in queries:
            if any(sum(c1 != c2 for c1, c2 in zip(q, d)) <= 2 for d in dictionary):
                words.append(q)
        return words
        
# @lc code=end

