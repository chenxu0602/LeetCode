#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#
# https://leetcode.com/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (75.37%)
# Likes:    281
# Dislikes: 12
# Total Accepted:    13.8K
# Total Submissions: 18.5K
# Testcase Example:  '"AAB"'
#
# You have a set of tiles, where each tile has one letter tiles[i] printed on
# it.  Return the number of possible non-empty sequences of letters you can
# make.
# 
# 
# 
# Example 1:
# 
# 
# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
# "ABA", "BAA".
# 
# 
# 
# Example 2:
# 
# 
# Input: "AAABBC"
# Output: 188
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
# 
#
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        """
        res = set()
        def dfs(path, t):
            if path:
                res.add(path)
            for i in range(len(t)):
                dfs(path+t[i], t[:i] + t[i+1:])

        dfs("", tiles)
        return len(res)
        """

        res = {""}
        for c in tiles:
            res |= {d[:i] + c + d[i:] for d in res for i in range(len(d)+1)}
        return len(res) - 1
        

