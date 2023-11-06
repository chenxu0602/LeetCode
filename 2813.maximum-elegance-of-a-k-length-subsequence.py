#
# @lc app=leetcode id=2813 lang=python3
#
# [2813] Maximum Elegance of a K-Length Subsequence
#

# @lc code=start
from collections import defaultdict, deque
import heapq

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:


        # Greedy
        # Time  complexity: O(nlogn)
        # Space complexity: O(n)
        # items.sort(key=lambda x: x[0], reverse=True)

        # groups = defaultdict(list)
        # curSum = 0
        # for profit, category in items[:k]:
        #     groups[category] += profit,
        #     curSum += profit

        # duplicates = []
        # for category, group in groups.items():
        #     group.sort(reverse=True)
        #     if len(group) > 1:
        #         duplicates.extend(groups[category][1:])

        # heapq.heapify(duplicates)

        # res = curSum + len(groups) ** 2

        # for profit, category in items[k:]:
        #     if category in groups: continue
        #     if not duplicates: break

        #     duplicate = heapq.heappop(duplicates)
        #     curSum -= duplicate
        #     curSum += profit
        #     groups[category] += profit,

        #     res = max(res, curSum + len(groups) ** 2)

        # return res


        items.sort(reverse=True)
        sm, seenCats, dups = 0, set(), deque()

        for headPrf, headCat in items[:k]:
            sm += headPrf

            if headCat in seenCats:
                dups.append(headPrf)
            else:
                seenCats.add(headCat)

        numCats = len(seenCats)

        ans = sm = sm + numCats ** 2

        for tailPrf, tailCat in items[k:]:
            if not dups or tailCat in seenCats:
                continue

            numCats += 1
            diff = tailPrf - dups.pop() + 2 * numCats - 1  # a**2 - (a-1)**2 = 2*a - 1

            sm += diff
            ans = max(ans, sm)

            seenCats.add(tailCat)

        return ans 


        
# @lc code=end

