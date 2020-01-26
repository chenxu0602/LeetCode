#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#
# https://leetcode.com/problems/cut-off-trees-for-golf-event/description/
#
# algorithms
# Hard (30.78%)
# Likes:    306
# Dislikes: 180
# Total Accepted:    18K
# Total Submissions: 57.5K
# Testcase Example:  '[[1,2,3],[0,0,4],[7,6,5]]'
#
# You are asked to cut off trees in a forest for a golf event. The forest is
# represented as a non-negative 2D map, in this map:
# 
# 
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through,
# and this positive number represents the tree's height.
# 
# 
# 
# 
# You are asked to cut off all the trees in this forest in the order of tree's
# height - always cut off the tree with lowest height first. And after cutting,
# the original place has the tree will become a grass (value 1).
# 
# You will start from the point (0, 0) and you should output the minimum steps
# you need to walk to cut off all the trees. If you can't cut off all the
# trees, output -1 in that situation.
# 
# You are guaranteed that no two trees have the same height and there is at
# least one tree needs to be cut off.
# 
# Example 1:
# 
# 
# Input: 
# [
# ⁠[1,2,3],
# ⁠[0,0,4],
# ⁠[7,6,5]
# ]
# Output: 6
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# ⁠[1,2,3],
# ⁠[0,0,0],
# ⁠[7,6,5]
# ]
# Output: -1
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: 
# [
# ⁠[2,3,4],
# ⁠[0,0,5],
# ⁠[8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in
# (0,0) directly without walking.
# 
# 
# 
# 
# Hint: size of the given matrix will not exceed 50x50.
# 
#
from collections import deque

class Solution:
    def hadlocks(self, forest, sr, sc, tr, tc):
        R, C = len(forest), len(forest[0])
        processed = set()
        queue = deque([(0, sr, sc)])
        while queue:
            detours, r, c = queue.popleft()
            if (r, c) not in processed:
                processed.add((r, c))
                if r == tr and c == tc:
                    return abs(sr-tr) + abs(sc-tc) + 2*detours
                for nr, nc, closer in ((r-1, c, r > tr), (r+1, c, r < tr),
                                       (r, c-1, c > tc), (r, c+1, c < tc)):
                    if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                        if closer:
                            queue.appendleft((detours, nr, nc))
                        else:
                            queue.append((detours+1, nr, nc))
        return -1


    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees = sorted((v, r, c) for r, row in enumerate(forest) for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0
        for _, tr, tc in trees:
            d = self.hadlocks(forest, sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans
        

