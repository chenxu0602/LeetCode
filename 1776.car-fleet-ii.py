#
# @lc app=leetcode id=1776 lang=python3
#
# [1776] Car Fleet II
#
# https://leetcode.com/problems/car-fleet-ii/description/
#
# algorithms
# Hard (33.10%)
# Likes:    69
# Dislikes: 2
# Total Accepted:    1.1K
# Total Submissions: 3.2K
# Testcase Example:  '[[1,2],[2,1],[4,3],[7,2]]'
#
# There are n cars traveling at different speeds in the same direction along a
# one-lane road. You are given an array cars of length n, where cars[i] =
# [positioni, speedi] represents:
# 
# 
# positioni is the distance between the i^th car and the beginning of the road
# in meters. It is guaranteed that positioni < positioni+1.
# speedi is the initial speed of the i^th car in meters per second.
# 
# 
# For simplicity, cars can be considered as points moving along the number
# line. Two cars collide when they occupy the same position. Once a car
# collides with another car, they unite and form a single car fleet. The cars
# in the formed fleet will have the same position and the same speed, which is
# the initial speed of the slowest car in the fleet.
# 
# Return an array answer, where answer[i] is the time, in seconds, at which the
# i^th car collides with the next car, or -1 if the car does not collide with
# the next car. Answers within 10^-5 of the actual answers are accepted.
# 
# 
# Example 1:
# 
# 
# Input: cars = [[1,2],[2,1],[4,3],[7,2]]
# Output: [1.00000,-1.00000,3.00000,-1.00000]
# Explanation: After exactly one second, the first car will collide with the
# second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds,
# the third car will collide with the fourth car, and form a car fleet with
# speed 2 m/s.
# 
# 
# Example 2:
# 
# 
# Input: cars = [[3,4],[5,4],[6,3],[9,1]]
# Output: [2.00000,1.00000,1.50000,-1.00000]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= cars.length <= 10^5
# 1 <= positioni, speedi <= 10^6
# positioni < positioni+1
# 
# 
#

# @lc code=start
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:

        result, stack = [], []
        for pos, spd in cars[::-1]:
            while stack and (spd <= stack[-1][1] or (stack[-1][0] - pos) / (spd - stack[-1][1]) >= stack[-1][2]):
                stack.pop()

            if not stack:
                stack.append((pos, spd, float("inf")))
                result.append(-1)
            else:
                collideTime = (stack[-1][0] - pos) / (spd - stack[-1][1])
                stack.append((pos, spd, collideTime))
                result.append(collideTime)

        return result[::-1]
            


        
# @lc code=end

