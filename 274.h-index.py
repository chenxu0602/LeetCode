#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (35.17%)
# Likes:    515
# Dislikes: 866
# Total Accepted:    141K
# Total Submissions: 400.8K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 3, 0, 6, 1, 5 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
# 
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # Time  complexity: O(nlogn)
        # Space complexity: O(1)
        # citations.sort()
        # i = 0
        # while i < len(citations) and citations[len(citations) - 1 - i] > i:
        #     i += 1
        # return i


        # return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))



        # Counting Sort
        # Time  complexity: O(n)
        # Space complexity: O(n)
        n = len(citations)
        papers = [0] * (n + 1)
        for c in citations:
            papers[min(n, c)] += 1
        k, s = n, papers[n]
        while k > s:
            k -= 1
            s += papers[k]
        return k 
        

# @lc code=end

