#
# @lc app=leetcode id=800 lang=python3
#
# [800] Similar RGB Color
#
# https://leetcode.com/problems/similar-rgb-color/description/
#
# algorithms
# Easy (61.31%)
# Likes:    60
# Dislikes: 374
# Total Accepted:    10.4K
# Total Submissions: 16.9K
# Testcase Example:  '"#09f166"'
#
# In the following, every capital letter represents some hexadecimal digit from
# 0 to f.
# 
# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.
# For example, "#15c" is shorthand for the color "#1155cc".
# 
# Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB -
# UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
# 
# Given the color "#ABCDEF", return a 7 character color that is most similar to
# #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"
# 
# 
# Example 1:
# Input: color = "#09f166"
# Output: "#11ee66"
# Explanation:  
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64
# -9 -0 = -73.
# This is the highest among any shorthand color.
# 
# 
# Note:
# 
# 
# color is a string of length 7.
# color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0
# to f
# Any answer which has the same (highest) similarity as the best answer will be
# accepted.
# All inputs and outputs should use lowercase letters, and the output is 7
# characters.
# 
# 
#

# @lc code=start
class Solution:
    def similarRGB(self, color: str) -> str:
        # O(1)

        # def similarity(hex1, hex2):
        #     r1, g1, b1 = hex1 >> 16, (hex1 >> 8) % 256, hex1 % 256
        #     r2, g2, b2 = hex2 >> 16, (hex2 >> 8) % 256, hex2 % 256
        #     return -(r1 - r2)**2 - (g1 - g2)**2 - (b1 - b2)**2

        # hex1 = int(color[1:], 16)
        # ans = 0
        # for r in range(16):
        #     for g in range(16):
        #         for b in range(16):
        #             hex2 = 17 * r * (1 << 16) + 17 * g * (1 << 8) + 17 * b
        #             if similarity(hex1, hex2) > similarity(hex1, ans):
        #                 ans = hex2

        # return '#{:06x}'.format(ans)


        # Rounding By Component
        def f(comp):
            q, r = divmod(int(comp, 16), 17)
            if r > 8: q += 1
            return '{:02x}'.format(17 * q)

        return '#' + f(color[1:3]) + f(color[3:5]) + f(color[5:])
        
# @lc code=end

