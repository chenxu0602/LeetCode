#
# @lc app=leetcode id=2525 lang=python3
#
# [2525] Categorize Box According to Criteria
#

# @lc code=start
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        idx = int(length >= 1e4 or width >= 1e4 or height >= 1e4 or length * width * height >= 10**9) + 2 * (mass >= 100)

        return ("Neither", "Bulky", "Heavy", "Both")[idx]
        
# @lc code=end

