#
# @lc app=leetcode id=753 lang=python3
#
# [753] Cracking the Safe
#
# https://leetcode.com/problems/cracking-the-safe/description/
#
# algorithms
# Hard (50.39%)
# Likes:    440
# Dislikes: 608
# Total Accepted:    28.5K
# Total Submissions: 56.2K
# Testcase Example:  '1\n1'
#
# There is a box protected by a password. The password is a sequence of n
# digits where each digit can be one of the first k digits 0, 1, ..., k-1.
# 
# While entering a password, the last n digits entered will automatically be
# matched against the correct password.
# 
# For example, assuming the correct password is "345", if you type "012345",
# the box will open because the correct password matches the suffix of the
# entered password.
# 
# Return any password of minimum length that is guaranteed to open the box at
# some point of entering it.
# 
# 
# 
# Example 1:
# 
# 
# Input: n = 1, k = 2
# Output: "01"
# Note: "10" will be accepted too.
# 
# 
# Example 2:
# 
# 
# Input: n = 2, k = 2
# Output: "00110"
# Note: "01100", "10011", "11001" will be accepted too.
# 
# 
# 
# 
# Note:
# 
# 
# n will be in the range [1, 4].
# k will be in the range [1, 10].
# k^n will be at most 4096.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # Hierholzer's Algorithm
        # Time  complexity: O(n x k^n)
        # Space complexity: O(n x k^n)
        # seen, ans = set(), []
        # def dfs(node):
        #     for x in map(str, range(k)):
        #         nei = node + x
        #         if nei not in seen:
        #             seen.add(nei)
        #             dfs(nei[1:])
        #             ans.append(x)

        # dfs('0' * (n - 1))
        # return ''.join(ans) + '0' * (n - 1)


        # s = '0' * (n - 1)
        # D = '9876543210'[-k:]
        # for _ in range(k ** n):
        #     s += next(d for d in D if (s + d)[-n:] not in s)
        # return s


        # Inverse Burrows-Wheeler Transform
        # Time  complexity: O(k^n)
        # Space complexity: O(k^n)
        M = k ** (n - 1)
        P = [q * k + i for i in range(k) for q in range(M)]
        ans = []

        for i in range(k ** n):
            j = i
            while P[j] >= 0:
                ans.append(str(j // M))
                P[j], j = -1, P[j]

        return ''.join(ans) + '0' * (n - 1)
        
# @lc code=end

