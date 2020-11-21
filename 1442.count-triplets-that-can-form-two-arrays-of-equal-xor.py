#
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/
#
# algorithms
# Medium (70.40%)
# Likes:    398
# Dislikes: 23
# Total Accepted:    14.3K
# Total Submissions: 20.2K
# Testcase Example:  '[2,3,1,6,7]'
#
# Given an array of integers arr.
# 
# We want to select three indices i, j and k where (0 <= i < j <= k <
# arr.length).
# 
# Let's define a and b as follows:
# 
# 
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# 
# 
# Note that ^ denotes the bitwise-xor operation.
# 
# Return the number of triplets (i, j and k) Where a == b.
# 
# 
# Example 1:
# 
# 
# Input: arr = [2,3,1,6,7]
# Output: 4
# Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,1,1,1,1]
# Output: 10
# 
# 
# Example 3:
# 
# 
# Input: arr = [2,3]
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: arr = [1,3,5,7,9]
# Output: 3
# 
# 
# Example 5:
# 
# 
# Input: arr = [7,11,12,9,5,2,7,17,22]
# Output: 8
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 300
# 1 <= arr[i] <= 10^8
# 
#

# @lc code=start
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # count, n = 0, len(arr)
        # for i in range(n - 1):
        #     accu = arr[i]
        #     for k in range(i + 1, n):
        #         accu ^= arr[k]
        #         if accu == 0:
        #             count += k - i
        # return count


        # We only need to find all subarrays whose XOR is zero.
        # prefix[xor]=[idxSum, cnt]
        # "idxSum": is the sum of all "index" whose prefix XOR equals "xor".
        # "cnt": means how many such "index" has prefix XOR being "xor".
        res = cur = 0
        count = {0: [1, -1]}

        for k, a in enumerate(arr):
            cur ^= a
            if cur not in count:
                count[cur] = [0, 0]
            n, total = count[cur]
            res += (k - 1) * n - total
            count[cur] = [n + 1, total + k]

        return res


        
# @lc code=end

