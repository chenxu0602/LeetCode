#
# @lc app=leetcode id=1227 lang=python3
#
# [1227] Airplane Seat Assignment Probability
#
# https://leetcode.com/problems/airplane-seat-assignment-probability/description/
#
# algorithms
# Medium (59.02%)
# Likes:    95
# Dislikes: 150
# Total Accepted:    5.2K
# Total Submissions: 8.7K
# Testcase Example:  '1'
#
# n passengers board an airplane with exactly n seats. The first passenger has
# lost the ticket and picks a seat randomly. But after that, the rest of
# passengers will:
# 
# 
# Take their own seat if it is still available, 
# Pick other seats randomly when they find their seat occupied 
# 
# 
# What is the probability that the n-th person can get his own seat?
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 1.00000
# Explanation: The first person can only get the first seat.
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 0.50000
# Explanation: The second person has a probability of 0.5 to get the second
# seat (when first person gets the first seat).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# 
#

# @lc code=start

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # Each round we have 3 choices:

        # the 1st person gets his/her own seat. (with probability 1/n). Then the n-th person is sure (with probability 1) to get the n-th seat.
        # the 1st person gets the n-th person's seat. (with probability 1/n). Then the n-th person cannot (with probability 0) get the n-th seat.
        # the 1st person gets a seat between 2 and n-1 (with probability (n-2)/n). Assume the 1st person gets a-th seat. Then in the next round, we have 3 choices again:
        #     3.1) if the a-th person gets 1st seat (with probability 1/(n-1)), then this is just like 1st and a-th person swap their seats, it never affect our result for the n-th person.
        #     3.2) if the a-th person gets n-th seat (with probability 1/(n-1)), game over.
        #     3.3) if the a-th person gets a seat which is not 1st or n-th, (with probability (n-1-2)/(n-1)), we jump into a loop.
        # Therefore the dp pattern is dp[i] = 1.0 / (i+1) + 0.0 / (i+1) + dp[i-1] * (i-1) / (i+1), with dp[0]=1 for the case there's only one person. If you manually calculate it you'll find dp[i] is always 1/2 except the base condition.
        dp = [0] * n
        dp[0] = 1.0
        for i in range(1, n):
            dp[i] = 1.0 / (i + 1) + dp[i - 1] * (i - 1) / (i + 1)
        return dp[-1]


        # f(n) = 1/n                                    -> 1st person picks his own seat
        #         + 1/n * 0                                 -> 1st person picks last one's seat
        #     	+ (n-2)/n * (                            ->1st person picks one of seat from 2nd to (n-1)th
        #         1/(n-2) * f(n-1)                   -> 1st person pick 2nd's seat
        #         1/(n-2) * f(n-2)                  -> 1st person pick 3rd's seat
        #         ......
        #         1/(n-2) * f(2)                     -> 1st person pick (n-1)th's seat
    	#     )
	
        # => f(n) = 1/n * ( f(n-1) + f(n-2) + f(n-3) + ... + f(1) )

        # if n == 1:
        #     return 1.0
        # return 1.0 / n + (n - 2.0) / n * self.nthPersonGetsNthSeat(n - 1)
        
# @lc code=end

