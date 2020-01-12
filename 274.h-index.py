#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (34.62%)
# Likes:    393
# Dislikes: 673
# Total Accepted:    123.1K
# Total Submissions: 355.6K
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
class Solution:
    def hIndex(self, citations: List[int]) -> int:
#        citations.sort(reverse=True)

#        for i, v in enumerate(citations):
#            if not v > i:
#                return i
#
#        return len(citations)

#        i = 0
#        while i < len(citations) and citations[i] > i:
#            i += 1
#
#        return i

#        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))

        """
        n = len(citations)
        count = [0] * (n+1)

        for num in citations:
            count[min(n, num)] += 1

        r = 0
        for i in range(n, -1, -1):
            r += count[i]
            if r >= i:
                return i

        return 0
        """

        citations.sort(reverse=True)
        i = 0
        while i < len(citations) and citations[i] > i:
            i += 1
        return i
        
        

