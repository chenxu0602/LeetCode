#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#
# https://leetcode.com/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (75.42%)
# Likes:    789
# Dislikes: 30
# Total Accepted:    37.4K
# Total Submissions: 49.6K
# Testcase Example:  '"AAB"'
#
# You have n  tiles, where each tile has one letter tiles[i] printed on it.
# 
# Return the number of possible non-empty sequences of letters you can make
# using the letters printed on those tiles.
# 
# 
# Example 1:
# 
# 
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
# "ABA", "BAA".
# 
# 
# Example 2:
# 
# 
# Input: tiles = "AAABBC"
# Output: 188
# 
# 
# Example 3:
# 
# 
# Input: tiles = "V"
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # def dfs(path, t):
        #     if path: res.add(path)
        #     for i in range(len(t)):
        #         dfs(path + t[i], t[:i] + t[i+1:])

        # res = set()
        # dfs("", tiles)
        # return len(res)


        res = {""}
        for c in tiles:
            res |= {d[:i] + c + d[i:] for d in res for i in range(len(d) + 1)}
        return len(res) - 1


        
# @lc code=end

