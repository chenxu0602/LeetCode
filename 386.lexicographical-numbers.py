#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (46.22%)
# Likes:    372
# Dislikes: 60
# Total Accepted:    41K
# Total Submissions: 88.3K
# Testcase Example:  '13'
#
# Given an integer n, return 1 - n in lexicographical order.
# 
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
# 
# Please optimize your algorithm to use less time and space. The input size may
# be as large as 5,000,000.
# 
#
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # O(N)

#        return list(map(int, sorted([str(i) for i in range(1, n+1)])))

        def dfs(i):
            if i <= n:
                results.append(i)
                for d in range(10):
                    dfs(10 * i + d)

        results = []
        for i in range(1, 10):
            dfs(i)

        return results
        

