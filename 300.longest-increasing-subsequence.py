#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.89%)
# Likes:    3665
# Dislikes: 81
# Total Accepted:    312.3K
# Total Submissions: 745.5K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#

# @lc code=start
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Dynamic Programming
        # Time  complexity: O(n^2)
        # Space complexity: O(n)
        # n = len(nums)
        # if n == 0:
        #     return 0

        # dp, maxans = [0] * n, 0

        # for i in range(n):
        #     maxval = 0
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             maxval = max(maxval, dp[j])

        #     dp[i] = maxval + 1
        #     maxans = max(maxans, dp[i])

        # return maxans



        # Dynamic Programming with Binary Search
        # Time  complexity: O(nlogn)
        # Space complexity: O(n)
        lst = []
        for num in nums:
            i = bisect.bisect_left(lst, num)
            if i >= len(lst):
                lst.append(num)
            lst[i] = num
        return len(lst)

# @lc code=end


def longest_palindromic_subsequence(s):
    # Initializing a lookup table of dimensions len(s) x len(s)
    lookup_table = [[0 for x in range(len(s))] for x in range(len(s))]

    # Every sequence with one element is a palindrome of length 1
    for i in range(len(s)):
        lookup_table[i][i] = 1

    for start_index in reversed(range(len(s))):
        for end_index in range(start_index + 1, len(s)):

            # case 1: elements at the beginning and the end are the same
            if s[start_index] == s[end_index]:
                lookup_table[start_index][end_index] = 2 + lookup_table[start_index + 1][end_index - 1]

            # case 2: skip one element either from the beginning or the end
            else:
                lookup_table[start_index][end_index] = max(lookup_table[start_index + 1][end_index],
                                                           lookup_table[start_index][end_index - 1])

    return lookup_table[0][len(s) - 1]


def find_lps_length(s):
    # initializing a lookup table of dimensions len(s) * len(s)
    dp = [[0 for x in range(len(s))] for x in range(len(s))]

    # every string with one character is always a palindrome
    for i in range(len(s)):
        dp[i][i] = 1

    for start in reversed(range(len(s)-1)):
        for end in range(start + 1, len(s)):
            # the characters at the start and end indexes match
            if s[start] == s[end]:
                substring_length = end - start + 1

                # if the substring length is 2 or the remaining substring is a palindrome
                if substring_length == 2 or substring_length - 2 == dp[start + 1][end - 1]:
                    dp[start][end] = substring_length
                else:
                    # skip one element either from the beginning or end and select the maximum resultant value
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
            else:
                # skip one element either from the beginning or end and select the maximum resultant value
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

    return dp[0][len(s) - 1]


def count_palindromic_substring(str1):
  n = len(str1)
  # Declare a lookup table 2-D table which that
  # the answers of the tabulation
  lookup_table = [[False for _ in range(n)] for _ in range(n)]
  ps_count=0

  # start filling the lookup table with the results of the
  # palindromic substrings
  for i in range(n - 1, -1, -1):
    for j in range(i, n):
      # start checking substrings from i to j
      # if they are palindrome or not
      if str1[i] == str1[j]:
        # if the substring is palindrome set the
        # value in table as True if we have not checked it before
        if i+1 >= j:
          lookup_table[i][j] = True
        # otherwise fill it with the previously stored value
        else:
          lookup_table[i][j] = lookup_table[i+1][j-1]
      # if the substring is a palindrome increment the count of
      # the palindromic substrings by 1
      if lookup_table[i][j]:
        ps_count += 1

  return ps_count


def min_cuts_helper(s, palindrome_table, dp):

    n = len(s)

    # Filling the palindrome table
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                # If the string consists of two characters or if the remaining string, str[i + 1 : j - 1]
                # is a palindrome, str[i : j] must also be a palindrome
                if j - i == 1 or palindrome_table[i + 1][j - 1]:
                    palindrome_table[i][j] = 1

    # Traversing the dp table in reverse order
    for i in range(n - 1, -1, -1):

        # If str[i : n - 1] is a palindrome, no cuts need to be performed,
        # so dp[i] = 0
        if palindrome_table[i][n - 1] == 1:
            dp[i] = 0

        # Otherwise, we traverse the remaining string to check if it contains
        # a palindrome and perform the minimum number of cuts on it to update
        # dp[i]
        else:
            for j in range(n - 2, i - 1, -1):
                if palindrome_table[i][j] == 1:
                    dp[i] = min(dp[i], 1 + dp[j + 1])

    # We return dp[0], as it contains the minimum number of cuts over the
    # entire string
    return dp[0]


