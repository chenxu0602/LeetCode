#
# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#
# https://leetcode.com/problems/circular-array-loop/description/
#
# algorithms
# Medium (27.71%)
# Likes:    161
# Dislikes: 946
# Total Accepted:    19.7K
# Total Submissions: 71K
# Testcase Example:  '[2,-1,1,2,2]'
#
# You are given a circular array nums of positive and negative integers. If a
# number k at an index is positive, then move forward k steps. Conversely, if
# it's negative (-k), move backward k steps. Since the array is circular, you
# may assume that the last element's next element is the first element, and the
# first element's previous element is the last element.
# 
# Determine if there is a loop (or a cycle) in nums. A cycle must start and end
# at the same index and the cycle's length > 1. Furthermore, movements in a
# cycle must all follow a single direction. In other words, a cycle must not
# consist of both forward and backward movements.
# 
# 
# 
# Example 1:
# 
# 
# Input: [2,-1,1,2,2]
# Output: true
# Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's
# length is 3.
# 
# 
# Example 2:
# 
# 
# Input: [-1,2]
# Output: false
# Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because
# the cycle's length is 1. By definition the cycle's length must be greater
# than 1.
# 
# 
# Example 3:
# 
# 
# Input: [-2,1,-1,-2,-2]
# Output: false
# Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle,
# because movement from index 1 -> 2 is a forward movement, but movement from
# index 2 -> 1 is a backward movement. All movements in a cycle must follow a
# single direction.
# 
# 
# 
# Note:
# 
# 
# -1000 ≤ nums[i] ≤ 1000
# nums[i] ≠ 0
# 1 ≤ nums.length ≤ 5000
# 
# 
# 
# 
# Follow up:
# 
# Could you solve it in O(n) time complexity and O(1) extra space complexity?
#
class Solution:
    def getIndex(self, i, nums):
        n = len(nums)
        if i + nums[i] >= 0:
            return (i + nums[i]) % n
        else:
            return n - (abs(i + nums[i]) % n)

    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        n = len(nums)

        if n == 1: return False

        for i, v in enumerate(nums):
            if v == 0:
                continue


            j, k = i, self.getIndex(i, nums)
            while nums[k] * nums[i] > 0 and nums[self.getIndex(k, nums)] * nums[i] > 0:
                if j == k:
                    if j == self.getIndex(j, nums):
                        break
                    return True

                j = self.getIndex(j, nums)
                k = self.getIndex(self.getIndex(k, nums), nums)

            j = i
            val = nums[i]
            while nums[j] * val > 0:
                next = self.getIndex(j, nums) 
                j = next

        return False
        """

        """
        N, i, bads = len(nums), 0, set()

        def isLoop(i, visiting, direction):
            if i in visiting:
                return True
            visiting.add(i)

            if (i + nums[i]) % N == i or nums[i] // abs(nums[i]) != direction:
                bads.update(visiting)
                return False
            return isLoop((i+nums[i])%N, visiting, direction)


        for i, v in enumerate(nums):
            if isLoop(i, set(), v//abs(v)):
                return True
        return False
        """

        s, l = [], len(nums)
        for i, n in enumerate(nums):
            if i in s:
                continue
            d = []
            while n * nums[i] > 0:
                if i in d:
                    if d[-1] != i:
                        return True
                    break
                d.append(i)
                s.append(i)
                i = (i + nums[i]) % l
        return False

        

        

