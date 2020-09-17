#
# @lc app=leetcode id=842 lang=python3
#
# [842] Split Array into Fibonacci Sequence
#
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/
#
# algorithms
# Medium (36.29%)
# Likes:    485
# Dislikes: 169
# Total Accepted:    20.7K
# Total Submissions: 57K
# Testcase Example:  '"123456579"'
#
# Given a string S of digits, such as S = "123456579", we can split it into a
# Fibonacci-like sequence [123, 456, 579].
# 
# Formally, a Fibonacci-like sequence is a list F of non-negative integers such
# that:
# 
# 
# 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer
# type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# 
# 
# Also, note that when splitting the string into pieces, each piece must not
# have extra leading zeroes, except if the piece is the number 0 itself.
# 
# Return any Fibonacci-like sequence split from S, or return [] if it cannot be
# done.
# 
# Example 1:
# 
# 
# Input: "123456579"
# Output: [123,456,579]
# 
# 
# Example 2:
# 
# 
# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
# 
# 
# Example 3:
# 
# 
# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
# 
# 
# Example 4:
# 
# 
# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not
# valid.
# 
# 
# Example 5:
# 
# 
# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
# 
# 
# Note: 
# 
# 
# 1 <= S.length <= 200
# S contains only digits.
# 
# 
#

# @lc code=start
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        for i in range(min(10, len(S))):
            x = S[:i+1]
            if x != '0' and x.startswith('0'): break
            a = int(x)
            for j in range(i+1, min(i+10, len(S))):
                y = S[i+1:j+1]
                if y != '0' and y.startswith('0'): break
                b = int(y)
                fib = [a, b]
                k = j + 1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2**31 - 1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib

        return []

        
# @lc code=end

