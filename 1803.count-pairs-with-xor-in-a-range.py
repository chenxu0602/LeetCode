#
# @lc app=leetcode id=1803 lang=python3
#
# [1803] Count Pairs With XOR in a Range
#
# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/description/
#
# algorithms
# Hard (42.05%)
# Likes:    109
# Dislikes: 7
# Total Accepted:    2.5K
# Total Submissions: 5.8K
# Testcase Example:  '[1,4,2,7]\n2\n6'
#
# Given a (0-indexed) integer array nums and two integers low and high, return
# the number of nice pairs.
# 
# A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <=
# (nums[i] XOR nums[j]) <= high.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,4,2,7], low = 2, high = 6
# Output: 6
# Explanation: All nice pairs (i, j) are as follows:
# ⁠   - (0, 1): nums[0] XOR nums[1] = 5 
# ⁠   - (0, 2): nums[0] XOR nums[2] = 3
# ⁠   - (0, 3): nums[0] XOR nums[3] = 6
# ⁠   - (1, 2): nums[1] XOR nums[2] = 6
# ⁠   - (1, 3): nums[1] XOR nums[3] = 3
# ⁠   - (2, 3): nums[2] XOR nums[3] = 5
# 
# 
# Example 2:
# 
# 
# Input: nums = [9,8,4,2,1], low = 5, high = 14
# Output: 8
# Explanation: All nice pairs (i, j) are as follows:
# ​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
# - (0, 3): nums[0] XOR nums[3] = 11
# - (0, 4): nums[0] XOR nums[4] = 8
# - (1, 2): nums[1] XOR nums[2] = 12
# - (1, 3): nums[1] XOR nums[3] = 10
# - (1, 4): nums[1] XOR nums[4] = 9
# - (2, 3): nums[2] XOR nums[3] = 6
# - (2, 4): nums[2] XOR nums[4] = 5
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 2 * 10^4
# 1 <= low <= high <= 2 * 10^4
# 
# 
#

# @lc code=start
from collections import Counter 

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, val):
        node = self.root
        for i in reversed(range(15)):
            bit = (val >> i) & 1
            if bit not in node:
                node[bit] = {"cnt": 1}
            else:
                node[bit]["cnt"] += 1
            node = node[bit]

    def count(self, val, high):
        # if cmp == 1, then we know that all nodes having the same bit value as "val" will result this digit to be 0 after xor, which are guaranteed to be smaller than "high", so we can add all of those nodes and move onto the sub-trie that have different value than "bit" (1^bit is just a fancier way to say "change 0 to 1 and change 1 to 0")
        # otherwise, if cmp==0, we know all nodes that have different bit value as "val" will result something larger so we can ignore all those and only traverse the sub-trie that has the same value as "bit" (which, after xor, will result this digit to be zero)
        ans = 0
        node = self.root
        for i in reversed(range(15)):
            if not node: break
            bit = (val >> i) & 1
            cmp = (high >> i) & 1
            if cmp:
                if node.get(bit, {}):
                    ans += node[bit]["cnt"]
                node = node.get(1 ^ bit, {})
            else:
                node = node.get(bit, {})
        return ans

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()

        ans = 0
        for x in nums:
            ans += trie.count(x, high + 1) - trie.count(x, low)
            trie.insert(x)
        return ans


        # O(n)
        # def test(nums, x):
        #     count = Counter(nums)
        #     res = 0
        #     while x:
        #         if x & 1:
        #             res += sum(count[a] * count[(x - 1) ^ a] for a in count)
        #         count = Counter({a >> 1: count[a] + count[a ^ 1] for a in count})
        #         x >>= 1
        #     return res // 2
        
        # return test(nums, high + 1) - test(nums, low)
# @lc code=end

