#
# @lc app=leetcode id=748 lang=python3
#
# [748] Shortest Completing Word
#
# https://leetcode.com/problems/shortest-completing-word/description/
#
# algorithms
# Easy (54.95%)
# Likes:    131
# Dislikes: 472
# Total Accepted:    22.9K
# Total Submissions: 41.7K
# Testcase Example:  '"1s3 PSt"\n["step","steps","stripe","stepple"]'
#
# 
# Find the minimum length word from a given dictionary words, which has all the
# letters from the string licensePlate.  Such a word is said to complete the
# given string licensePlate
# 
# Here, for letters we ignore case.  For example, "P" on the licensePlate still
# matches "p" on the word.
# 
# It is guaranteed an answer exists.  If there are multiple answers, return the
# one that occurs first in the array.
# 
# The license plate might have the same letter occurring multiple times.  For
# example, given a licensePlate of "PP", the word "pair" does not complete the
# licensePlate, but the word "supper" does.
# 
# 
# Example 1:
# 
# Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe",
# "stepple"]
# Output: "steps"
# Explanation: The smallest length word that contains the letters "S", "P",
# "S", and "T".
# Note that the answer is not "step", because the letter "s" must occur in the
# word twice.
# Also note that we ignored case for the purposes of comparing whether a letter
# exists in the word.
# 
# 
# 
# Example 2:
# 
# Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
# Output: "pest"
# Explanation: There are 3 smallest length words that contains the letters "s".
# We return the one that occurred first.
# 
# 
# 
# Note:
# 
# licensePlate will be a string with length in range [1, 7].
# licensePlate will contain digits, spaces, or letters (uppercase or
# lowercase).
# words will have a length in the range [10, 1000].
# Every words[i] will consist of lowercase letters, and have length in range
# [1, 15].
# 
# 
#
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Time  complexity: O(N)
        # Space complexity: O(1)
        def count(itera):
            ans = [0] * 26
            for letter in itera:
                ans[ord(letter) - ord('a')] += 1
            return ans

        def dominates(c1, c2):
            return all(x1 >= x2 for x1, x2 in zip(c1, c2))

        ans = None
        target = count(c.lower() for c in licensePlate if c.isalpha())
        for word in words:
            if (ans is None or len(word) < len(ans)) and dominates(count(word.lower()), target):
                ans = word

        return ans
        

