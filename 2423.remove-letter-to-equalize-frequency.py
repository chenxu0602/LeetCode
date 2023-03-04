#
# @lc app=leetcode id=2423 lang=python3
#
# [2423] Remove Letter To Equalize Frequency
#

# @lc code=start
from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:

        counter = Counter(word)
        for c in word:
            counter[c] -= 1

            if counter[c] == 0:
                counter.pop(c)

            if len(set(counter.values())) == 1:
                return True 

            counter[c] += 1

        return False 
        
# @lc code=end

