#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#

# @lc code=start
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winners, losers, counter = [], [], {}
        for winner, loser in matches:
            counter[winner] = counter.get(winner, 0)
            counter[loser] = counter.get(loser, 0) + 1

        for k, v in counter.items():
            if v == 0:
                winners.append(k)
            
            if v == 1:
                losers.append(k)

        return [sorted(winners), sorted(losers)]
        
# @lc code=end

