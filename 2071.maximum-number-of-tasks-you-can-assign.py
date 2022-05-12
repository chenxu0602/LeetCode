#
# @lc app=leetcode id=2071 lang=python3
#
# [2071] Maximum Number of Tasks You Can Assign
#

# @lc code=start
from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks, workers = sorted(tasks), sorted(workers)

        def check(k):
            W = SortedList(workers[-k:])
            tries = pills

            for elem in tasks[:k][::-1]:
                place = W.bisect_left(elem)
                if place < len(W):
                    W.pop(place)
                elif tries > 0:
                    place2 = W.bisect_left(elem - strength)
                    if place2 < len(W):
                        W.pop(place2)
                        tries -= 1
                else:
                    return False

            return len(W) == 0


        left, right = 0, min(len(workers), len(tasks)) 
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left
        
# @lc code=end

