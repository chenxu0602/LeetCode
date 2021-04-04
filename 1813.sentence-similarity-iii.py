#
# @lc app=leetcode id=1813 lang=python3
#
# [1813] Sentence Similarity III
#
# https://leetcode.com/problems/sentence-similarity-iii/description/
#
# algorithms
# Medium (31.39%)
# Likes:    31
# Dislikes: 6
# Total Accepted:    2.4K
# Total Submissions: 7.7K
# Testcase Example:  '"My name is Haley"\n"My Haley"'
#
# A sentence is a list of words that are separated by a single space with no
# leading or trailing spaces. For example, "Hello World", "HELLO", "hello world
# hello world" are all sentences. Words consist of only uppercase and lowercase
# English letters.
# 
# Two sentences sentence1 and sentence2 are similar if it is possible to insert
# an arbitrary sentence (possibly empty) inside one of these sentences such
# that the two sentences become equal. For example, sentence1 = "Hello my name
# is Jane" and sentence2 = "Hello Jane" can be made equal by inserting "my name
# is" between "Hello" and "Jane" in sentence2.
# 
# Given two sentences sentence1 and sentence2, return true if sentence1 and
# sentence2 are similar. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
# Output: true
# Explanation: sentence2 can be turned to sentence1 by inserting "name is"
# between "My" and "Haley".
# 
# 
# Example 2:
# 
# 
# Input: sentence1 = "of", sentence2 = "A lot of words"
# Output: false
# Explanation: No single sentence can be inserted inside one of the sentences
# to make it equal to the other.
# 
# 
# Example 3:
# 
# 
# Input: sentence1 = "Eating right now", sentence2 = "Eating"
# Output: true
# Explanation: sentence2 can be turned to sentence1 by inserting "right now" at
# the end of the sentence.
# 
# 
# Example 4:
# 
# 
# Input: sentence1 = "Luky", sentence2 = "Lucccky"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= sentence1.length, sentence2.length <= 100
# sentence1 and sentence2 consist of lowercase and uppercase English letters
# and spaces.
# The words in sentence1 and sentence2 are separated by a single space.
# 
# 
#

# @lc code=start
from collections import Counter, defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # s1, s2 = sentence1.split(), sentence2.split()

        # if len(s1) > len(s2): s1, s2 = s2, s1

        # while s1:
        #     if s2[0] == s1[0]:
        #         s1.pop(0)
        #         s2.pop(0)
        #     elif s2[-1] == s1[-1]:
        #         s1.pop()
        #         s2.pop()
        #     else:
        #         return False

        # return True


        words1, words2 = sentence1.split(), sentence2.split()
        n1, n2 = map(len, (words1, words2))
        if n1 > n2:
            return self.areSentencesSimilar(sentence2, sentence1)

        i = 0
        while i < n1 and words1[i] == words2[i]:
            i += 1

        while i < n1 and words1[i] == words2[n2 - n1 + i]:
            i += 1

        return i == n1
        
# @lc code=end

