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
import math, heapq

class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        # Dynamic Programming
        # Time  complexity: O(N x K^2)
        # Space complexity: O(N x K)
        # N = len(stations)
        # deltas = [stations[i + 1] - stations[i] for i in range(N - 1)]
        # dp = [[0.0] * (K + 1) for _ in range(N - 1)]
        # for i in range(K + 1):
        #     dp[0][i] = deltas[0] / float(i + 1)

        # for p in range(1, N - 1):
        #     for k in range(K + 1):
        #         dp[p][k] = min(max(deltas[p] / float(x + 1), dp[p - 1][k - x]) \
        #                         for x in range(k + 1))

        # return dp[-1][K]


        # Heap
        # Time  complexity: O(N + KlogN)
        # Space complexity: O(N)
        # pq = []
        # for i in range(len(stations) - 1):
        #     x, y = stations[i], stations[i + 1]
        #     pq.append((x - y, y - x, 1))
        # heapq.heapify(pq)

        # for _ in range(K):
        #     negnext, orig, parts = heapq.heappop(pq)
        #     parts += 1
        #     heapq.heappush(pq, (-(orig / float(parts)), orig, parts))

        # return -pq[0][0]

        
        # Binary Search
        # Time  complexity: O(NlogW)
        # Space complexity: O(1)
        def possible(D):
            return sum(int((stations[i + 1] - stations[i]) // D) for i in range(len(stations) - 1)) <= K

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi

        return lo

