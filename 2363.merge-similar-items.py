#
# @lc app=leetcode id=2363 lang=python3
#
# [2363] Merge Similar Items
#

# @lc code=start
from collections import Counter

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        return sorted((Counter(dict(items1)) + Counter(dict(items2))).items())
        
# @lc code=end

