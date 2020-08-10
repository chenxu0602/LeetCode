#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (32.10%)
# Likes:    1031
# Dislikes: 71
# Total Accepted:    92.8K
# Total Submissions: 288.5K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# The update(i, val) function modifies nums by updating the element at index i
# to val.
# 
# Example:
# 
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# Note:
# 
# 
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
# 
# 
#

# @lc code=start
class NumArray:
    # Segment Tree
    def __init__(self, nums: List[int]):
        # Time  complexity: O(n), n + n/2 + n/4 + n/8 + ... 1 = 2n
        # Space complexity: O(n)
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.buildTree(nums)
        
    def buildTree(self, nums: List[int]):
        i, j = self.n, 0
        while i < 2 * self.n:
            self.tree[i] = nums[j]
            i += 1; j += 1

        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]

    def update(self, i: int, val: int) -> None:
        # Time  complexity: O(logn)
        # Space complexity: O(1)
        i += self.n
        self.tree[i] = val
        while i > 0:
            left, right = i, i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i - 1

            self.tree[i // 2] = self.tree[left] + self.tree[right]
            i //= 2
        

    def sumRange(self, i: int, j: int) -> int:
        # Time  complexity: O(logn)
        # Space complexity: O(1)
        # Check if ll is right child of its parent PP
        # Check if rr is left child of its parent PP
        l, r, s = i + self.n, j + self.n, 0

        while l <= r:
            if l % 2 == 1:
                s += self.tree[l]
                l += 1
            if r % 2 == 0:
                s += self.tree[r]
                r -= 1

            l //= 2; r //= 2

        return s
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end

