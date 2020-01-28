#
# @lc app=leetcode id=774 lang=python3
#
# [774] Minimize Max Distance to Gas Station
#
# https://leetcode.com/problems/minimize-max-distance-to-gas-station/description/
#
# algorithms
# Hard (42.72%)
# Likes:    245
# Dislikes: 36
# Total Accepted:    10.8K
# Total Submissions: 25.1K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n9'
#
# On a horizontal number line, we have gas stations at positions stations[0],
# stations[1], ..., stations[N-1], where N = stations.length.
# 
# Now, we add K more gas stations so that D, the maximum distance between
# adjacent gas stations, is minimized.
# 
# Return the smallest possible value of D.
# 
# Example:
# 
# 
# Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
# Output: 0.500000
# 
# 
# Note:
# 
# 
# stations.length will be an integer in range [10, 2000].
# stations[i] will be an integer in range [0, 10^8].
# K will be an integer in range [1, 10^6].
# Answers within 10^-6 of the true value will be accepted as correct.
# 
# 
#
import math
import heapq

class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        def possible(D):
            return sum(((stations[i+1] - stations[i]) // D) for i in range(len(stations) - 1)) <= K

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo

        """
        max_heap = []
        for i in range(1, len(stations)):
            heapq.heappush(max_heap, (-float(stations[i] - stations[i-1]), i, 1))

        added = 0
        while added < K:
            cur_dist, i, cur_added = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-float(stations[i] - stations[i-1]) / (cur_added + 1), i, cur_added + 1))
            added += 1

        return -max_heap[0][0]
        """

        """
        bound = (stations[-1] - stations[0]) / (K + 1)
        added = 0
        max_heap = []

        for i in range(1, len(stations)):
            needed = math.ceil((stations[i] - stations[i-1]) / bound) - 1
            heapq.heappush(max_heap, (-(stations[i] - stations[i-1]) / (needed + 1), i, needed))
            added += needed

        while added < K:
            cur, i, needed = heapq.heappop(max_heap)
            needed += 1
            heapq.heappush(max_heap, (-(stations[i] - stations[i-1]) / (needed + 1), i, needed))
            added += 1

        return -max_heap[0][0]
        """
        

