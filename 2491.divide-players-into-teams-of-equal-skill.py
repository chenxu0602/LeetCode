#
# @lc app=leetcode id=2491 lang=python3
#
# [2491] Divide Players Into Teams of Equal Skill
#

# @lc code=start
from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        s = 2 * sum(skill) // len(skill)
        chemistry = 0
        cnt = Counter(skill)

        for v, c in cnt.items():
            if c != cnt[s - v]:
                return -1

            chemistry += c * v * (s - v) 

        return chemistry // 2
        
# @lc code=end

