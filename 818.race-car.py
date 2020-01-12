#
# @lc app=leetcode id=818 lang=python3
#
# [818] Race Car
#
# https://leetcode.com/problems/race-car/description/
#
# algorithms
# Hard (35.84%)
# Likes:    319
# Dislikes: 36
# Total Accepted:    11.9K
# Total Submissions: 32.8K
# Testcase Example:  '3'
#
# Your car starts at position 0 and speed +1 on an infinite number line.  (Your
# car can go into negative positions.)
# 
# Your car drives automatically according to a sequence of instructions A
# (accelerate) and R (reverse).
# 
# When you get an instruction "A", your car does the following: position +=
# speed, speed *= 2.
# 
# When you get an instruction "R", your car does the following: if your speed
# is positive then speed = -1 , otherwise speed = 1.  (Your position stays the
# same.)
# 
# For example, after commands "AAR", your car goes to positions 0->1->3->3, and
# your speed goes to 1->2->4->-1.
# 
# Now for some target position, say the length of the shortest sequence of
# instructions to get there.
# 
# 
# Example 1:
# Input: 
# target = 3
# Output: 2
# Explanation: 
# The shortest instruction sequence is "AA".
# Your position goes from 0->1->3.
# 
# 
# 
# Example 2:
# Input: 
# target = 6
# Output: 5
# Explanation: 
# The shortest instruction sequence is "AAARA".
# Your position goes from 0->1->3->7->7->6.
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= target <= 10000.
# 
# 
#
import heapq, math

class Solution:
    def __init__(self):
        self.dp = {0: 0}

    def racecar(self, target: int) -> int:
        """
        dp = [0, 1, 4] + [float("inf")] * target
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2 ** k - 1:
                dp[t] = k
                continue
            for j in range(k-1):
                dp[t] = min(dp[t], dp[t - 2 ** (k-1) + 2 ** j] + k - 1 + j + 2)
            if 2 ** k - 1 - t < t:
                dp[t] = min(dp[t], dp[2 ** k - 1 - t] + k + 1)
        return dp[target]
        """

        if target in self.dp:
            return self.dp[target]

        n = target.bit_length()

        if 2 ** n - 1 == target:
            self.dp[target] = n
        else:
            self.dp[target] = self.racecar(2**n-1-target) + n + 1
            for m in range(n - 1):
                self.dp[target] = min(self.dp[target], \
                    self.racecar(target - 2**(n-1) + 2**m) + n + m + 1)

        return self.dp[target]


        





        

