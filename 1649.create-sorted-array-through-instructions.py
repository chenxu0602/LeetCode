#
# @lc app=leetcode id=1649 lang=python3
#
# [1649] Create Sorted Array through Instructions
#
# https://leetcode.com/problems/create-sorted-array-through-instructions/description/
#
# algorithms
# Hard (42.39%)
# Likes:    84
# Dislikes: 13
# Total Accepted:    3.4K
# Total Submissions: 8.1K
# Testcase Example:  '[1,5,6,2]'
#
# Given an integer array instructions, you are asked to create a sorted array
# from the elements in instructions. You start with an empty container nums.
# For each element from left to right in instructions, insert it into nums. The
# cost of each insertion is the minimum of the following:
# 
# 
# The number of elements currently in nums that are strictly less than
# instructions[i].
# The number of elements currently in nums that are strictly greater than
# instructions[i].
# 
# 
# For example, if inserting element 3 into nums = [1,2,3,5], the cost of
# insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is
# greater than 3) and nums will become [1,2,3,3,5].
# 
# Return the total cost to insert all elements from instructions into nums.
# Since the answer may be large, return it modulo 10^9 + 7
# 
# 
# Example 1:
# 
# 
# Input: instructions = [1,5,6,2]
# Output: 1
# Explanation: Begin with nums = [].
# Insert 1 with cost min(0, 0) = 0, now nums = [1].
# Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
# Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
# Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
# The total cost is 0 + 0 + 0 + 1 = 1.
# 
# Example 2:
# 
# 
# Input: instructions = [1,2,3,6,5,4]
# Output: 3
# Explanation: Begin with nums = [].
# Insert 1 with cost min(0, 0) = 0, now nums = [1].
# Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
# Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
# Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
# Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
# Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
# The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.
# 
# 
# Example 3:
# 
# 
# Input: instructions = [1,3,3,3,2,4,2,1,2]
# Output: 4
# Explanation: Begin with nums = [].
# Insert 1 with cost min(0, 0) = 0, now nums = [1].
# Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
# Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
# Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
# Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
# Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
# ​​​​​​​Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
# ​​​​​​​Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
# ​​​​​​​Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
# The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= instructions.length <= 10^5
# 1 <= instructions[i] <= 10^5
# 
# 
#

# @lc code=start
import bisect
from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        # Segment Tree
        # M is the maximum value in instructions.
        # Time  complexity: O(N x logM)
        # Space complexity: O(M)
        def update(index, value, tree, m):
            index += m
            tree[index] += value
            while index > 1:
                index >>= 1
                tree[index] = tree[index << 1] + tree[(index << 1) + 1]

        def query(left, right, tree, m):
            result = 0
            left += m
            right += m
            while left < right:
                if left & 1:
                    result += tree[left]
                    left += 1
                left >>= 1
                if right & 1:
                    right -= 1
                    result += tree[right]
                right >>= 1
            return result

        MOD = 10**9 + 7
        m = max(instructions) + 1
        tree = [0] * (2 * m)
        cost = 0
        for x in instructions:
            left_cost = query(0, x, tree, m)
            right_cost = query(x + 1, m, tree, m)
            cost += min(left_cost, right_cost)
            update(x, 1, tree, m)
        return cost % MOD



        # O(N^2)
        # MOD = 10**9 + 7
        # current = []
        # cost = 0
        # for x in instructions:
        #     left_cost = bisect.bisect_left(current, x)
        #     right_cost = len(current) - bisect.bisect_right(current, x)
        #     cost += min(left_cost, right_cost)
        #     bisect.insort(current, x)
        #     cost %= MOD
        # return cost % MOD


        # O(N x logN)
        # sorted_list = SortedList()
        # MOD = 10**9 + 7
        # cost = 0

        # size = len(instructions)
        # for i in range(size):
        #     left_cost = sorted_list.bisect_left(instructions[i])
        #     right_cost = i - sorted_list.bisect_right(instructions[i])
        #     cost += min(left_cost, right_cost)
        #     sorted_list.add(instructions[i])
        # return cost % MOD

        
# @lc code=end

