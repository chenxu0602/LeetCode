#
# @lc app=leetcode id=2751 lang=python3
#
# [2751] Robot Collisions
#

# @lc code=start
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        n = len(positions)
        ind = list(range(n))
        ind.sort(key=lambda x: positions[x])
        s = []
        for i in ind:
            if directions[i] == 'L':
                while s:
                    j = s[-1]
                    if healths[i] == healths[j]:
                        healths[i] = healths[j] = 0
                        s.pop()
                        break

                    if healths[i] > healths[j]:
                        healths[i] -= 1
                        healths[j] = 0
                        s.pop()
                    else:
                        healths[i] = 0
                        healths[j] -= 1
                        break
            else:
                s += i,

        return [h for h in healths if h]
        
# @lc code=end

