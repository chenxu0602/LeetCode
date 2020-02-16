#
# @lc app=leetcode id=1257 lang=python3
#
# [1257] Smallest Common Region
#
# https://leetcode.com/problems/smallest-common-region/description/
#
# algorithms
# Medium (56.11%)
# Likes:    78
# Dislikes: 11
# Total Accepted:    3.3K
# Total Submissions: 5.8K
# Testcase Example:  '[["Earth","North America","South America"],["North America","United ' + 'States","Canada"],["United States","New ' + 'York","Boston"],["Canada","Ontario","Quebec"],["South ' + 'America","Brazil"]]\n"Quebec"\n"New York"'
#
# You are given some lists of regions where the first region of each list
# includes all other regions in that list.
# 
# Naturally, if a region X contains another region Y then X is bigger than Y.
# Also by definition a region X contains itself.
# 
# Given two regions region1, region2, find out the smallest region that
# contains both of them.
# 
# If you are given regions r1, r2 and r3 such that r1 includes r3, it is
# guaranteed there is no r2 such that r2 includes r3.
# 
# It's guaranteed the smallest region exists.
# 
# 
# Example 1:
# 
# 
# Input:
# regions = [["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# region1 = "Quebec",
# region2 = "New York"
# Output: "North America"
# 
# 
# 
# Constraints:
# 
# 
# 2 <= regions.length <= 10^4
# region1 != region2
# All strings consist of English letters and spaces with at most 20 letters.
# 
# 
#

# @lc code=start
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        parent = {}
        for region in regions:
            for child in region[1:]:
                parent[child] = region[0]

        candidates = set([region1])
        while region1 in parent:
            region1 = parent[region1]
            candidates.add(region1)

        while region2 not in candidates:
            region2 = parent[region2]

        return region2
        
# @lc code=end

