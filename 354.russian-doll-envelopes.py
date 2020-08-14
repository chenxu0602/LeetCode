#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (35.50%)
# Likes:    1186
# Dislikes: 40
# Total Accepted:    69.3K
# Total Submissions: 194.9K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You have a number of envelopes with widths and heights given as a pair of
# integers (w, h). One envelope can fit into another if and only if both the
# width and height of one envelope is greater than the width and height of the
# other envelope.
# 
# What is the maximum number of envelopes can you Russian doll? (put one inside
# other)
# 
# Note:
# Rotation is not allowed.
# 
# Example:
# 
# 
# 
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3 
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
# 
# 
# 
#

# @lc code=start
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        res = []
        for en in envelopes:
            i = bisect.bisect_left(res, en[1])
            if i == len(res):
                res.append(en[1])
            else:
                res[i] = en[1]
        return len(res)
        
# @lc code=end

