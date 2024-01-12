#
# @lc app=leetcode id=2942 lang=python3
#
# [2942] Find Words Containing Character
#

# @lc code=start
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        res = []
        for i in range(len(words)):
            if x in words[i]:
                res += i,

        return res
    
        
# @lc code=end

