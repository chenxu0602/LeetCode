#
# @lc app=leetcode id=2663 lang=python3
#
# [2663] Lexicographically Smallest Beautiful String
#

# @lc code=start
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:

        """
        A = [ord(c) - ord('a') for c in s]
        n = len(A)
        i = n - 1
        A[i] += 1
        while i >= 0:
            if A[i] == k:
                i -= 1
            elif A[i] not in A[max(i - 2, 0):i]:
                break
            A[i] += 1

        if i < 0: return ""
        for j in range(i + 1, n):
            A[j] = min({0, 1, 2} - set(A[max(0, j - 2):j]))

        return "".join(chr(ord('a') + a) for a in A)
        """

        # To make lexicographically smallest greater string, we need to check from right to left (similar to next greater integer). While traversing from right to left, we update last alphabet from right. While incrementing the last letter each time, we make sure that formed string contains first kkk letters and does not contain any substring as a palindrome.
        s = list(s)
        i = len(s) - 1
        s[i] = chr(ord(s[i]) + 1)
        while 0 <= i < len(s):
            if ord(s[i]) >= k + ord('a'):
                s[i] = 'a'
                i -= 1
                s[i] = chr(ord(s[i]) + 1)
            elif (i >= 1 and s[i] == s[i - 1]) or (i >= 2 and s[i] == s[i - 2]):
                s[i] = chr(ord(s[i]) + 1)
            else:
                i += 1

        return "" if i < 0 else "".join(s)


        
# @lc code=end

