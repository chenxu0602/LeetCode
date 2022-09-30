#
# @lc app=leetcode id=2410 lang=python3
#
# [2410] Maximum Matching of Players With Trainers
#

# @lc code=start
import heapq

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ans = 0
        trainers.sort()
        heapq.heapify(players)

        for t in trainers:
            if players and players[0] <= t:
                heapq.heappop(players)
                ans += 1

        return ans
        
# @lc code=end

