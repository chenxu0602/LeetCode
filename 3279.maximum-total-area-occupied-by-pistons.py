#
# @lc app=leetcode id=3279 lang=python3
#
# [3279] Maximum Total Area Occupied by Pistons
#

# @lc code=start
from collections import defaultdict
from itertools import pairwise

class Solution:
    def maxArea(self, height: int, positions: List[int], directions: str) -> int:

        n, u = len(positions), directions.count('U')
        ans = max_ = sum(positions)
        vertices = defaultdict(int, {0: 0})   # register the time when this piston would hit two ends

        for d, pos in zip(directions, positions):
            if d == 'U':
                vertices[height - pos] -= 1
                vertices[2 * height - pos] += 1
            else:
                vertices[height + pos] -= 1
                vertices[pos] += 1

        for left, right in pairwise(sorted(vertices)):
            max_ += (right - left) * (2 * u - n)
            if max_ >= ans: ans = max_
            u += vertices[right]

        return ans

        
# @lc code=end

