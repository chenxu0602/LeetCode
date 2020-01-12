#
# @lc app=leetcode id=1093 lang=python3
#
# [1093] Statistics from a Large Sample
#
# https://leetcode.com/problems/statistics-from-a-large-sample/description/
#
# algorithms
# Medium (43.53%)
# Likes:    30
# Dislikes: 159
# Total Accepted:    5.3K
# Total Submissions: 11.8K
# Testcase Example:  '[0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]'
#
# We sampled integers between 0 and 255, and stored the results in an array
# count:  count[k] is the number of integers we sampled equal to k.
# 
# Return the minimum, maximum, mean, median, and mode of the sample
# respectively, as an array of floating point numbers.  The mode is guaranteed
# to be unique.
# 
# (Recall that the median of a sample is:
# 
# 
# The middle element, if the elements of the sample were sorted and the number
# of elements is odd;
# The average of the middle two elements, if the elements of the sample were
# sorted and the number of elements is even.)
# 
# 
# 
# Example 1:
# Input: count =
# [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
# Example 2:
# Input: count =
# [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
# 
# 
# Constraints:
# 
# 
# count.length == 256
# 1 <= sum(count) <= 10^9
# The mode of the sample that count represents is unique.
# Answers within 10^-5 of the true value will be accepted as correct.
# 
# 
#
import bisect

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = sum(count)
        mi = next(i for i in range(256) if count[i]) * 1.0
        ma = next(i for i in range(255, -1, -1) if count[i]) * 1.0
        mean = sum(i*v for i, v in enumerate(count)) * 1.0 / n
        mode = count.index(max(count)) * 1.0

        for i in range(255):
            count[i+1] += count[i]

        median1 = bisect.bisect(count, (n-1)//2)
        median2 = bisect.bisect(count, n//2)
        median = (median1 + median2) / 2.0

        return [mi, ma, mean, median, mode]
        

