#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#
# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
#
# algorithms
# Easy (42.64%)
# Likes:    866
# Dislikes: 113
# Total Accepted:    69.6K
# Total Submissions: 163.5K
# Testcase Example:  '[1,0,0,0,1,0,1]'
#
# In a row of seats, 1 represents a person sitting in that seat, and 0
# represents that the seat is empty. 
# 
# There is at least one empty seat, and at least one person sitting.
# 
# Alex wants to sit in the seat such that the distance between him and the
# closest person to him is maximized. 
# 
# Return that maximum distance to closest person.
# 
# 
# Example 1:
# 
# 
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has
# distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# 
# 
# Example 2:
# 
# 
# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# 2 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Next Array
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # N = len(seats)
        # left, right = [N] * N, [N] * N

        # for i in range(N):
        #     if seats[i] == 1: 
        #         left[i] = 0
        #     elif i > 0:
        #         left[i] = left[i - 1] + 1

        # for i in range(N - 1, -1, -1):
        #     if seats[i] == 1:
        #         right[i] = 0
        #     elif i < N - 1:
        #         right[i] = right[i + 1] + 1

        # return max(min(left[i], right[i]) for i, seat in enumerate(seats) if not seat)


        # Two Pointers
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # people = (i for i, seat in enumerate(seats) if seat)
        # prev, future = None, next(people)

        # ans = 0
        # for i, seat in enumerate(seats):
        #     if seat:
        #         prev = i
        #     else:
        #         while future is not None and future < i:
        #             future = next(people, None)

        #         left = float("inf") if prev is None else i - prev
        #         right = float("inf") if future is None else future - i
        #         ans = max(ans, min(left, right))

        # return ans


        # Group by Zero
        # Time  complexity: O(N)
        # Space complexity: O(1)
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K + 1) // 2)

        return max(ans, seats.index(1), seats[::-1].index(1))


        
# @lc code=end

