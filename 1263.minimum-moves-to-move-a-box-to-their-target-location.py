#
# @lc app=leetcode id=1263 lang=python3
#
# [1263] Minimum Moves to Move a Box to Their Target Location
#
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/description/
#
# algorithms
# Hard (40.94%)
# Likes:    238
# Dislikes: 9
# Total Accepted:    5K
# Total Submissions: 11.9K
# Testcase Example:  '[["#","#","#","#","#","#"],["#","T","#","#","#","#"],["#",".",".","B",".","#"],["#",".","#","#",".","#"],["#",".",".",".","S","#"],["#","#","#","#","#","#"]]'
#
# Storekeeper is a game in which the player pushes boxes around in a warehouse
# trying to get them to target locations.
# 
# The game is represented by a grid of size m x n, where each element is a
# wall, floor, or a box.
# 
# Your task is move the box 'B' to the target position 'T' under the following
# rules:
# 
# 
# Player is represented by character 'S' and can move up, down, left, right in
# the grid if it is a floor (empy cell).
# Floor is represented by character '.' that means free cell to walk.
# Wall is represented by character '#' that means obstacle  (impossible to walk
# there). 
# There is only one box 'B' and one target cell 'T' in the grid.
# The box can be moved to an adjacent free cell by standing next to the box and
# then moving in the direction of the box. This is a push.
# The player cannot walk through the box.
# 
# 
# Return the minimum number of pushes to move the box to the target. If there
# is no way to reach the target, return -1.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid = [["#","#","#","#","#","#"],
# ⁠              ["#","T","#","#","#","#"],
# ["#",".",".","B",".","#"],
# ["#",".","#","#",".","#"],
# ["#",".",".",".","S","#"],
# ["#","#","#","#","#","#"]]
# Output: 3
# Explanation: We return only the number of times the box is pushed.
# 
# Example 2:
# 
# 
# Input: grid = [["#","#","#","#","#","#"],
# ⁠              ["#","T","#","#","#","#"],
# ["#",".",".","B",".","#"],
# ["#","#","#","#",".","#"],
# ["#",".",".",".","S","#"],
# ["#","#","#","#","#","#"]]
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: grid = [["#","#","#","#","#","#"],
# ["#","T",".",".","#","#"],
# ["#",".","#","B",".","#"],
# ["#",".",".",".",".","#"],
# ["#",".",".",".","S","#"],
# ["#","#","#","#","#","#"]]
# Output: 5
# Explanation:  push the box down, left, left, up and up.
# 
# 
# Example 4:
# 
# 
# Input: grid = [["#","#","#","#","#","#","#"],
# ["#","S","#",".","B","T","#"],
# ["#","#","#","#","#","#","#"]]
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m <= 20
# 1 <= n <= 20
# grid contains only characters '.', '#',  'S' , 'T', or 'B'.
# There is only one character 'S', 'B' and 'T' in the grid.
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        # Heuristic (an under-estimate of the remaining moves required) is the Manhattan distance between box and target.
        # A state consist of box and person locations together.
        # Repeatedly pop the state with the lowest heuristic + previous moves off the heap.
        # Attempt to move the person in all 4 directions.
        # If any direction moves the person to the box, check if the box can move to the nex position in the grid.
        rows, cols = map(len, (grid, grid[0]))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'T':
                    target = (r, c)
                if grid[r][c] == 'B':
                    start_box = (r, c)
                if grid[r][c] == 'S':
                    start_person = (r, c)

        def heuristic(box):
            return abs(target[0] - box[0]) + abs(target[1] - box[1])

        def out_bounds(location):
            r, c = location
            if r < 0 or r >= rows:
                return True
            if c < 0 or c >= cols:
                return True
            return grid[r][c] == '#'

        heap = [[heuristic(start_box), 0, start_person, start_box]]
        visited = set()

        while heap:
            _, moves, person, box = heapq.heappop(heap)
            if box == target:
                return moves

            if (person, box) in visited:
                continue 

            visited.add((person, box))

            for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0):
                new_person = (person[0] + dr, person[1] + dc)
                if out_bounds(new_person):
                    continue

                if new_person == box:
                    new_box = (box[0] + dr, box[1] + dc)
                    if out_bounds(new_box):
                        continue

                    heapq.heappush(heap, [heuristic(new_box) + moves + 1, moves + 1, new_person, new_box])
                else:
                    heapq.heappush(heap, [heuristic(box) + moves, moves, new_person, box])

        return -1

                

        
# @lc code=end

