#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#
# https://leetcode.com/problems/furthest-building-you-can-reach/description/
#
# algorithms
# Medium (54.18%)
# Likes:    284
# Dislikes: 24
# Total Accepted:    10.3K
# Total Submissions: 19.3K
# Testcase Example:  '[4,2,7,6,9,14,12]\n5\n1'
#
# You are given an integer array heights representing the heights of buildings,
# some bricks, and some ladders.
# 
# You start your journey from building 0 and move to the next building by
# possibly using bricks or ladders.
# 
# While moving from building i to building i+1 (0-indexed),
# 
# 
# If the current building's height is greater than or equal to the next
# building's height, you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you
# can either use one ladder or (h[i+1] - h[i]) bricks.
# 
# 
# Return the furthest building index (0-indexed) you can reach if you use the
# given ladders and bricks optimally.
# 
# 
# Example 1:
# 
# 
# Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
# Output: 4
# Explanation: Starting at building 0, you can follow these steps:
# - Go to building 1 without using ladders nor bricks since 4 >= 2.
# - Go to building 2 using 5 bricks. You must use either bricks or ladders
# because 2 < 7.
# - Go to building 3 without using ladders nor bricks since 7 >= 6.
# - Go to building 4 using your only ladder. You must use either bricks or
# ladders because 6 < 9.
# It is impossible to go beyond building 4 because you do not have any more
# bricks or ladders.
# 
# 
# Example 2:
# 
# 
# Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
# Output: 7
# 
# 
# Example 3:
# 
# 
# Input: heights = [14,3,19,3], bricks = 17, ladders = 0
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= heights.length <= 10^5
# 1 <= heights[i] <= 10^6
# 0 <= bricks <= 10^9
# 0 <= ladders <= heights.length
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Min-Heap
        # Time  complexity: O(NlogN) or O(NlogL)
        # Space compleixty: O(N) or O(L)
        # ladder_allocations = []
        # for i in range(len(heights) - 1):
        #     climb = heights[i + 1] - heights[i]
        #     if climb <= 0: continue
        #     heapq.heappush(ladder_allocations, climb)

        #     if len(ladder_allocations) <= ladders:
        #         continue

        #     bricks -= heapq.heappop(ladder_allocations)

        #     if bricks < 0:
        #         return i

        # return len(heights) - 1


        heap = []
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)

            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)

            if bricks < 0:
                return i

        return len(heights) - 1


        # Binary Search for Final Reachable Building
        # Time  complexity: O(N(logN)^2)
        # Space complexity: O(N)
        # def is_reachable(building_index):
        #     climbs = []
        #     for h1, h2 in zip(heights[:building_index], heights[1:building_index + 1]):
        #         if h2 - h1 > 0:
        #             climbs.append(h2 - h1)
        #     climbs.sort()

        #     bricks_remaining, ladders_remaining = bricks, ladders
        #     for climb in climbs:
        #         if climb <= bricks_remaining:
        #             bricks_remaining -= climb
        #         elif ladders_remaining >= 1:
        #             ladders_remaining -= 1
        #         else:
        #             return False
        #     return True

        # lo, hi = 0, len(heights) - 1
        # while lo < hi:
        #     mid = lo + (hi - lo + 1) // 2
        #     if is_reachable(mid):
        #         lo = mid
        #     else:
        #         hi = mid - 1
        # return hi



        # Binary Search on Threshold (Advanced)
        # Time  complexity: O(Nlog(maxClimb))
        # Space complexity: O(1)
        # def solveWithGivenThreshold(K):
        #     ladders_remaining = ladders
        #     bricks_remaining = bricks
        #     ladders_used_on_threshold = 0

        #     for i in range(len(heights) - 1):
        #         climb = heights[i + 1] - heights[i]
        #         if climb <= 0:
        #             continue

        #         # Make resource allocations
        #         if climb == K:
        #             ladders_used_on_threshold += 1
        #             ladders_remaining -= 1
        #         elif climb > K:
        #             ladders_remaining -= 1
        #         else:
        #             bricks_remaining -= climb

        #         # Handle negative resources.
        #         if ladders_remaining < 0:
        #             if ladders_used_on_threshold:
        #                 ladders_used_on_threshold -= 1
        #                 ladders_remaining += 1
        #                 bricks_remaining -= K
        #             else:
        #                 return [i, ladders_remaining, bricks_remaining]

        #         if bricks_remaining < 0:
        #             return [i, ladders_remaining, bricks_remaining]

        #     return [len(heights) - 1, ladders_remaining, bricks_remaining]

        # # Find the minimum climb and maximum climbs
        # lo, hi = float("inf"), float("-inf")
        # for i in range(len(heights) - 1):
        #     climb = heights[i + 1] - heights[i]
        #     if climb <= 0:
        #         continue
        #     lo = min(lo, climb)
        #     hi = max(hi, climb)

        # if lo == float("inf"):
        #     return len(heights) - 1

        # # Carry out the binary search.
        # while lo <= hi:
        #     mid = lo + (hi - lo) // 2
        #     index_reached, ladders_remaining, bricks_remaining = solveWithGivenThreshold(mid)
        #     # Did we get all the way?
        #     if index_reached == len(heights) - 1:
        #         return len(heights) - 1
        #     # Otherwise, if we have a ladder remaining, it has to be too high.
        #     if ladders_remaining > 0:
        #         hi = mid - 1
        #         continue

        #     # Otherwise, check for the other optimal conditions.
        #     next_climb = heights[index_reached + 1] - heights[index_reached]
        #     if bricks_remaining < next_climb and bricks_remaining < mid:
        #         return index_reached

        #     # Otherwise, it must have been too low.
        #     lo = mid + 1

         
# @lc code=end

