#
# @lc app=leetcode id=1640 lang=python3
#
# [1640] Check Array Formation Through Concatenation
#
# https://leetcode.com/problems/check-array-formation-through-concatenation/description/
#
# algorithms
# Easy (75.76%)
# Likes:    153
# Dislikes: 41
# Total Accepted:    15.3K
# Total Submissions: 20.6K
# Testcase Example:  '[85]\n[[85]]'
#
# You are given an array of distinct integers arr and an array of integer
# arrays pieces, where the integers in pieces are distinct. Your goal is to
# form arr by concatenating the arrays in pieces in any order. However, you are
# not allowed to reorder the integers in each array pieces[i].
# 
# Return true if it is possible to form the array arr from pieces. Otherwise,
# return false.
# 
# 
# Example 1:
# 
# 
# Input: arr = [85], pieces = [[85]]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: arr = [15,88], pieces = [[88],[15]]
# Output: true
# Explanation: Concatenate [15] then [88]
# 
# 
# Example 3:
# 
# 
# Input: arr = [49,18,16], pieces = [[16,18,49]]
# Output: false
# Explanation: Even though the numbers match, we cannot reorder pieces[0].
# 
# 
# Example 4:
# 
# 
# Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
# Output: true
# Explanation: Concatenate [91] then [4,64] then [78]
# 
# Example 5:
# 
# 
# Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= pieces.length <= arr.length <= 100
# sum(pieces[i].length) == arr.length
# 1 <= pieces[i].length <= arr.length
# 1 <= arr[i], pieces[i][j] <= 100
# The integers in arr are distinct.
# The integers in pieces are distinct (i.e., If we flatten pieces in a 1D
# array, all the integers in this array are distinct).
# 
# 
#

# @lc code=start
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # Time  complexity: O(N^2)
        # Space compleixty: O(1)
        # n = len(arr)
        # i = 0
        # while i < n:
        #     for p in pieces:
        #         if p[0] == arr[i]:
        #             break
        #     else:
        #         return False

        #     for x in p:
        #         if x != arr[i]:
        #             return False
        #         i += 1
        # return True


        # Binary Search
        # Time  complexity: O(NlogN)
        # Space compleixty: O(1)
        # n = len(arr)
        # p_len = len(pieces)
        # pieces.sort()

        # i = 0
        # while i < n:
        #     left, right = 0, p_len - 1
        #     found = -1
        #     # use binary search to find target piece:
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if pieces[mid][0] == arr[i]:
        #             found = mid
        #             break
        #         elif pieces[mid][0] > arr[i]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     if found == -1:
        #         return False
        #     # check target piece
        #     target_piece = pieces[found]
        #     for x in target_piece:
        #         if x != arr[i]:
        #             return False
        #         i += 1
            
        # return True


        # HashMap
        # Time  compleixty: O(N)
        # Space compleixty: O(N)
        n = len(arr)
        mapping = {p[0]: p for p in pieces}

        i = 0
        while i < n:
            if arr[i] not in mapping:
                return False
            target_piece = mapping[arr[i]]
            for x in target_piece:
                if x != arr[i]:
                    return False
                i += 1

        return True


        
# @lc code=end

