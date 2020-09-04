#
# @lc app=leetcode id=699 lang=python3
#
# [699] Falling Squares
#
# https://leetcode.com/problems/falling-squares/description/
#
# algorithms
# Hard (41.69%)
# Likes:    273
# Dislikes: 52
# Total Accepted:    13.6K
# Total Submissions: 32.3K
# Testcase Example:  '[[1,2],[2,3],[6,1]]'
#
# On an infinite number line (x-axis), we drop given squares in the order they
# are given.
# 
# The i-th square dropped (positions[i] = (left, side_length)) is a square with
# the left-most point being positions[i][0] and sidelength positions[i][1].
# 
# The square is dropped with the bottom edge parallel to the number line, and
# from a higher height than all currently landed squares. We wait for each
# square to stick before dropping the next.
# 
# The squares are infinitely sticky on their bottom edge, and will remain fixed
# to any positive length surface they touch (either the number line or another
# square). Squares dropped adjacent to each other will not stick together
# prematurely.
# 
# 
# Return a list ans of heights. Each height ans[i] represents the current
# highest height of any square we have dropped, after dropping squares
# represented by positions[0], positions[1], ..., positions[i].
# 
# Example 1:
# 
# 
# Input: [[1, 2], [2, 3], [6, 1]]
# Output: [2, 5, 5]
# Explanation:
# 
# 
# After the first drop of positions[0] = [1, 2]: _aa _aa ------- The maximum
# height of any square is 2.
# 
# After the second drop of positions[1] = [2, 3]: __aaa __aaa __aaa _aa__ _aa__
# -------------- The maximum height of any square is 5. The larger square stays
# on top of the smaller square despite where its center of gravity is, because
# squares are infinitely sticky on their bottom edge.
# 
# After the third drop of positions[1] = [6, 1]: __aaa __aaa __aaa _aa _aa___a
# -------------- The maximum height of any square is still 5. Thus, we return
# an answer of [2, 5, 5].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [[100, 100], [200, 100]]
# Output: [100, 100]
# Explanation: Adjacent squares don't get stuck prematurely - only their bottom
# edge can stick to surfaces.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= positions.length <= 1000.
# 1 <= positions[i][0] <= 10^8.
# 1 <= positions[i][1] <= 10^6.
# 
# 
# 
# 
#

# @lc code=start
import bisect

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        # qans = [0] * len(positions)
        # for i, (left, size) in enumerate(positions):
        #     right = left + size
        #     qans[i] += size
        #     for j in range(i + 1, len(positions)):
        #         left2, size2 = positions[j]
        #         right2 = left2 + size2
        #         if left2 < right and left < right2:
        #             qans[j] = max(qans[j], qans[i])

        # ans = []
        # for x in qans:
        #     ans.append(max(ans[-1], x) if ans else x)
        # return ans
        

        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        heights, pos, res = [0], [0], []
        max_h = 0
        for left, side in positions:
            i = bisect.bisect_right(pos, left)
            j = bisect.bisect_left(pos, left + side)
            height = max(heights[i-1:j] or [0]) + side
            pos[i:j] = [left, left + side]
            heights[i:j] = [height, heights[j-1]]
            max_h = max(max_h, height)
            res.append(max_h)
        return res

# @lc code=end

