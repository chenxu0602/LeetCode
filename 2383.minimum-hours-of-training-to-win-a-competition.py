#
# @lc app=leetcode id=2383 lang=python3
#
# [2383] Minimum Hours of Training to Win a Competition
#

# @lc code=start
from mimetypes import init


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:

        en, ex = 0, 0
        an, ax = 0, 0

        for ener, expr in zip(energy, experience):
            if ener >= en:
                an += (ener - en + 1)
                en += (ener - en + 1)

            if expr >= ex:
                ax += (expr - ex + 1)
                ex += (expr - ex + 1)

            en -= ener
            ex += expr

        return max(0, (an - initialEnergy)) + max(0, (ax - initialExperience))
        
# @lc code=end

