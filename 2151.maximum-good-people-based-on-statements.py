#
# @lc app=leetcode id=2151 lang=python3
#
# [2151] Maximum Good People Based on Statements
#

# @lc code=start
from os import stat


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:

        """
        n, ans = len(statements), 0
        def valid(cur):
            for i in range(n):
                if cur[i]:
                    for j in range(n):
                        if statements[i][j] != 2 and statements[i][j] != cur[j]:
                            return False
            return True

        def dfs(cur, i, cnt):
            nonlocal ans
            if i == n:
                if valid(cur):
                    ans = max(ans, cnt)
                return

            cur.append(0)
            dfs(cur, i + 1, cnt)
            cur[-1] = 1
            dfs(cur, i + 1, cnt + 1)
            cur.pop()

        dfs([], 0, 0)
        return ans
        """

        n, ans = len(statements), 0
        def valid(cur):
            for i in range(n):
                if cur & 1 << n - 1 - i:
                    for j in range(n):
                        if statements[i][j] != 2 and statements[i][j] != bool(cur & 1 << n - 1 - j):
                            return False
            return True

        return max(bin(i).count('1') if valid(i) else 0 for i in range(1 << n))

            
        
        
# @lc code=end

