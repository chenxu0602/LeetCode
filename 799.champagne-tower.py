#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#
# https://leetcode.com/problems/champagne-tower/description/
#
# algorithms
# Medium (35.58%)
# Likes:    429
# Dislikes: 27
# Total Accepted:    15.1K
# Total Submissions: 42K
# Testcase Example:  '1\n1\n1'
#
# We stack glasses in a pyramid, where the first row has 1 glass, the second
# row has 2 glasses, and so on until the 100th row.  Each glass holds one cup
# (250ml) of champagne.
# 
# Then, some champagne is poured in the first glass at the top.  When the top
# most glass is full, any excess liquid poured will fall equally to the glass
# immediately to the left and right of it.  When those glasses become full, any
# excess champagne will fall equally to the left and right of those glasses,
# and so on.  (A glass at the bottom row has it's excess champagne fall on the
# floor.)
# 
# For example, after one cup of champagne is poured, the top most glass is
# full.  After two cups of champagne are poured, the two glasses on the second
# row are half full.  After three cups of champagne are poured, those two cups
# become full - there are 3 full glasses total now.  After four cups of
# champagne are poured, the third row has the middle glass half full, and the
# two outside glasses are a quarter full, as pictured below.
# 
# 
# 
# Now after pouring some non-negative integer cups of champagne, return how
# full the j-th glass in the i-th row is (both i and j are 0 indexed.)
# 
# 
# 
# 
# Example 1:
# Input: poured = 1, query_glass = 1, query_row = 1
# Output: 0.0
# Explanation: We poured 1 cup of champange to the top glass of the tower
# (which is indexed as (0, 0)). There will be no excess liquid so all the
# glasses under the top glass will remain empty.
# 
# Example 2:
# Input: poured = 2, query_glass = 1, query_row = 1
# Output: 0.5
# Explanation: We poured 2 cups of champange to the top glass of the tower
# (which is indexed as (0, 0)). There is one cup of excess liquid. The glass
# indexed as (1, 0) and the glass indexed as (1, 1) will share the excess
# liquid equally, and each will get half cup of champange.
# 
# 
# 
# 
# Note:
# 
# 
# poured will be in the range of [0, 10 ^ 9].
# query_glass and query_row will be in the range of [0, 99].
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Instead of keeping track of how much champagne should end up in a glass, 
        # keep track of the total amount of champagne that flows through a glass. 
        # For example, if poured = 10 cups are poured at the top, then the total 
        # flow-through of the top glass is 10; the total flow-through of each glass 
        # in the second row is 4.5, and so on.
        # Time  complexity: O(R^2)
        # Space complexity: O(1)
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r + 1][c] += q
                    A[r + 1][c + 1] += q

        return min(1, A[query_row][query_glass])
        
# @lc code=end

