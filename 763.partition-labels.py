#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (75.77%)
# Likes:    2704
# Dislikes: 122
# Total Accepted:    144.1K
# Total Submissions: 188.5K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# A string S of lowercase English letters is given. We want to partition this
# string into as many parts as possible so that each letter appears in at most
# one part, and return a list of integers representing the size of these
# parts.
# 
# 
# 
# Example 1:
# 
# 
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
# 
# 
# 
# 
# Note:
# 
# 
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # Greedy
        # Time  complexity: O(N)
        # Space complexity: O(1)
        last = {c: i for i, c in enumerate(S)}
        ans, j, anchor = [], 0, 0
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans
        
# @lc code=end

