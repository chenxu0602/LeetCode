#
# @lc app=leetcode id=2768 lang=python3
#
# [2768] Number of Black Blocks
#

# @lc code=start
from collections import Counter 

class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:

        dict1 = Counter()

        for i, j in coordinates:
            for x in range(i - 1, i + 1):
                for y in range(j - 1, j + 1):
                    if 0 <= x < m - 1 and 0 <= y < n - 1:
                        dict1[(x, y)] += 1

        
        dict2 = Counter(dict1.values())

        return [
            (m - 1) * (n - 1) - sum(dict2.values()),
            dict2[1],
            dict2[2],
            dict2[3],
            dict2[4],
        ]
        
# @lc code=end

