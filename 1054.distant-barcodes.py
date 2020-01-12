#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#
# https://leetcode.com/problems/distant-barcodes/description/
#
# algorithms
# Medium (39.31%)
# Likes:    161
# Dislikes: 10
# Total Accepted:    8.1K
# Total Submissions: 20.2K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# In a warehouse, there is a row of barcodes, where the i-th barcode is
# barcodes[i].
# 
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may
# return any answer, and it is guaranteed an answer exists.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,2,1,2,1]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
# 
# 
# 
# 
# 
#
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        i, n = 0, len(barcodes)
        res = [0] * n
        for k, v in Counter(barcodes).most_common():
            for _ in range(v):
                res[i] = k
                i += 2
                if i >= n:
                    i = 1
        return res
        """

        count = Counter(barcodes)
        barcodes.sort(key=lambda a: (count[a], a))
        barcodes[1::2], barcodes[::2] = barcodes[:len(barcodes)//2], barcodes[len(barcodes)//2:]
        return barcodes
        

