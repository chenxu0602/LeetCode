#
# @lc app=leetcode id=1338 lang=python3
#
# [1338] Reduce Array Size to The Half
#
# https://leetcode.com/problems/reduce-array-size-to-the-half/description/
#
# algorithms
# Medium (66.73%)
# Likes:    311
# Dislikes: 32
# Total Accepted:    27.1K
# Total Submissions: 40.6K
# Testcase Example:  '[3,3,3,3,5,5,5,2,2,7]'
#
# Given an array arr.  You can choose a set of integers and remove all the
# occurrences of these integers in the array.
# 
# Return the minimum size of the set so that at least half of the integers of
# the array are removed.
# 
# 
# Example 1:
# 
# 
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has
# size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array
# [3,3,3,3,5,5,5] which has size greater than half of the size of the old
# array.
# 
# 
# Example 2:
# 
# 
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the
# new array empty.
# 
# 
# Example 3:
# 
# 
# Input: arr = [1,9]
# Output: 1
# 
# 
# Example 4:
# 
# 
# Input: arr = [1000,1000,3,7]
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: arr = [1,2,3,4,5,6,7,8,9,10]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^5
# arr.length is even.
# 1 <= arr[i] <= 10^5
# 
#

# @lc code=start
from collections import Counter
import math

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # counts = Counter(arr)
        # counts = [count for number, count in counts.most_common()]

        # total_removed = 0
        # set_size = 0
        # for count in counts:
        #     total_removed += count
        #     set_size += 1
        #     if total_removed >= len(arr) // 2:
        #         break

        # return set_size


        # Hashing and Bucket Sort
        # O(n)
        counts = Counter(arr)
        max_value = max(counts.values())

        buckets = [0] * (max_value + 1)
        for count in counts.values():
            buckets[count] += 1

        set_size = 0
        arr_numbers_to_remove = len(arr) // 2
        bucket = max_value
        while arr_numbers_to_remove > 0:
            max_needed_from_bucket = math.ceil(arr_numbers_to_remove / bucket)
            set_size_increase = min(buckets[bucket], max_needed_from_bucket)
            set_size += set_size_increase
            arr_numbers_to_remove -= set_size_increase * bucket
            bucket -= 1

        return set_size
        
# @lc code=end

