#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (40.61%)
# Likes:    1759
# Dislikes: 69
# Total Accepted:    107.8K
# Total Submissions: 265.2K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# Example:
# 
# 
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
#

# @lc code=start
import bisect

# Nlog(N)

class BinarySearchTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.leftTreeSize = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val, root):
        if not root:
            self.root = BinarySearchTreeNode(val)
            return 0

        if val == root.val:
            root.count += 1
            return root.leftTreeSize

        if val < root.val:
            root.leftTreeSize += 1
            if not root.left:
                root.left = BinarySearchTreeNode(val)
                return 0
            return self.insert(val, root.left)

        if not root.right:
            root.right = BinarySearchTreeNode(val)
            return root.count + root.leftTreeSize

        return root.count + root.leftTreeSize + self.insert(val, root.right)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        # result, sortedList = [], []
        # for num in nums[::-1]:
        #     pos = bisect.bisect_left(sortedList, num)
        #     result.insert(0, pos)
        #     bisect.insort_left(sortedList, num)
        # return result


        tree = BinarySearchTree()
        return [
            tree.insert(nums[i], tree.root) for i in range(len(nums) - 1, -1, -1)
        ][::-1]

        
# @lc code=end

