#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
#
# algorithms
# Medium (40.33%)
# Likes:    762
# Dislikes: 48
# Total Accepted:    72.4K
# Total Submissions: 179.4K
# Testcase Example:  '"9,3,4,#,#,1,#,#,2,#,6,#,#"'
#
# One way to serialize a binary tree is to use pre-order traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node,
# we record using a sentinel value such as #.
# 
# 
# ⁠    _9_
# ⁠   /   \
# ⁠  3     2
# ⁠ / \   / \
# ⁠4   1  #  6
# / \ / \   / \
# # # # #   # #
# 
# 
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
# 
# Given a string of comma separated values, verify whether it is a correct
# preorder traversal serialization of a binary tree. Find an algorithm without
# reconstructing the tree.
# 
# Each comma separated value in the string must be either an integer or a
# character '#' representing null pointer.
# 
# You may assume that the input format is always valid, for example it could
# never contain two consecutive commas such as "1,,3".
# 
# Example 1:
# 
# 
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# 
# Example 2:
# 
# 
# Input: "1,#"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: "9,#,#,1"
# Output: false
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        # Time  complexity: O(N)
        # Space complexity: O(N)
        # slots = 1

        # for node in preorder.split(','):
        #     # one node takes one slot
        #     slots -= 1

        #     # no more slots available
        #     if slots < 0:
        #         return False

        #     # non-empty node creates two children slots
        #     if node != '#':
        #         slots += 2

        # # all slots should be used up
        # return slots == 0
        


        # Time  complexity: O(N)
        # Space complexity: O(1)
        slots = 1

        prev = None # previous character
        for ch in preorder:
            if ch == ',':
                # one node takes one slot
                slots -= 1

                # no more slots available
                if slots < 0:
                    return False

                # non-empty node creates two children slots
                if prev != '#':
                    slots += 2

            prev = ch

        # the last node
        slots = slots + 1 if ch != '#' else slots - 1
        # all slots should be used up
        return slots == 0
        
# @lc code=end

