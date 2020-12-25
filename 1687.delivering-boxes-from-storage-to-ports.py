#
# @lc app=leetcode id=1687 lang=python3
#
# [1687] Delivering Boxes from Storage to Ports
#
# https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/description/
#
# algorithms
# Hard (29.55%)
# Likes:    50
# Dislikes: 4
# Total Accepted:    751
# Total Submissions: 2.5K
# Testcase Example:  '[[1,1],[2,1],[1,1]]\n2\n3\n3'
#
# You have the task of delivering some boxes from storage to their ports using
# only one ship. However, this ship has a limit on the number of boxes and the
# total weight that it can carry.
# 
# You are given an array boxes, where boxes[i] = [ports​​i​, weighti], and
# three integers portsCount, maxBoxes, and maxWeight.
# 
# 
# ports​​i is the port where you need to deliver the i^th box and weightsi is
# the weight of the i^th box.
# portsCount is the number of ports.
# maxBoxes and maxWeight are the respective box and weight limits of the
# ship.
# 
# 
# The boxes need to be delivered in the order they are given. The ship will
# follow these steps:
# 
# 
# The ship will take some number of boxes from the boxes queue, not violating
# the maxBoxes and maxWeight constraints.
# For each loaded box in order, the ship will make a trip to the port the box
# needs to be delivered to and deliver it. If the ship is already at the
# correct port, no trip is needed, and the box can immediately be
# delivered.
# The ship then makes a return trip to storage to take more boxes from the
# queue.
# 
# 
# The ship must end at storage after all the boxes have been delivered.
# 
# Return the minimum number of trips the ship needs to make to deliver all
# boxes to their respective ports.
# 
# 
# Example 1:
# 
# 
# Input: boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight =
# 3
# Output: 4
# Explanation: The optimal strategy is as follows: 
# - The ship takes all the boxes in the queue, goes to port 1, then port 2,
# then port 1 again, then returns to storage. 4 trips.
# So the total number of trips is 4.
# Note that the first and third boxes cannot be delivered together because the
# boxes need to be delivered in order (i.e. the second box needs to be
# delivered at port 2 before the third box).
# 
# 
# Example 2:
# 
# 
# Input: boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3,
# maxWeight = 6
# Output: 6
# Explanation: The optimal strategy is as follows: 
# - The ship takes the first box, goes to port 1, then returns to storage. 2
# trips.
# - The ship takes the second, third and fourth boxes, goes to port 3, then
# returns to storage. 2 trips.
# - The ship takes the fifth box, goes to port 3, then returns to storage. 2
# trips.
# So the total number of trips is 2 + 2 + 2 = 6.
# 
# 
# Example 3:
# 
# 
# Input: boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3,
# maxBoxes = 6, maxWeight = 7
# Output: 6
# Explanation: The optimal strategy is as follows:
# - The ship takes the first and second boxes, goes to port 1, then returns to
# storage. 2 trips.
# - The ship takes the third and fourth boxes, goes to port 2, then returns to
# storage. 2 trips.
# - The ship takes the fifth and sixth boxes, goes to port 3, then returns to
# storage. 2 trips.
# So the total number of trips is 2 + 2 + 2 = 6.
# 
# 
# Example 4:
# 
# 
# Input: boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]],
# portsCount = 5, maxBoxes = 5, maxWeight = 7
# Output: 14
# Explanation: The optimal strategy is as follows:
# - The ship takes the first box, goes to port 2, then storage. 2 trips.
# - The ship takes the second box, goes to port 2, then storage. 2 trips.
# - The ship takes the third and fourth boxes, goes to port 3, then storage. 2
# trips.
# - The ship takes the fifth box, goes to port 3, then storage. 2 trips.
# - The ship takes the sixth and seventh boxes, goes to port 3, then port 4,
# then storage. 3 trips. 
# - The ship takes the eighth and ninth boxes, goes to port 1, then port 5,
# then storage. 3 trips.
# So the total number of trips is 2 + 2 + 2 + 2 + 3 + 3 = 14.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= boxes.length <= 10^5
# 1 <= portsCount, maxBoxes, maxWeight <= 10^5
# 1 <= ports​​i <= portsCount
# 1 <= weightsi <= maxWeight
# 
# 
#

# @lc code=start
from collections import deque

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        queue = deque([(-1, 0)]) # monotonic queue. item: (division_position, trip_cost)
        pre = -1 # latest end of previous trip
        ws = 0 # maximal weights of current trip

        for i, (p, w) in enumerate(boxes):
            # update the earliest possible start of current trip:
            ws += w
            while i - pre > maxBoxes or ws > maxWeight:
                pre += 1
                ws -= boxes[pre][1]

            while queue[0][0] < pre:
                queue.popleft()

            # min cost of current trip. front of monotonic queue is always the minimal cost that meets the limitation
            mn = (2 if i + 1 < n and p == boxes[i + 1][0] else 1) + queue[0][1]

            while queue[-1][1] >= mn:
                queue.pop()

            queue.append((i, mn))

        base_trip = 1 # calc base trip cost
        for i in range(n - 1):
            if boxes[i][0] != boxes[i + 1][0]:
                base_trip += 1

        return base_trip + queue[-1][1]

        
# @lc code=end

