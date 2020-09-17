#
# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
#
# https://leetcode.com/problems/guess-the-word/description/
#
# algorithms
# Hard (44.43%)
# Likes:    322
# Dislikes: 346
# Total Accepted:    25.8K
# Total Submissions: 57.9K
# Testcase Example:  '"acckzz"\n["acckzz","ccbazz","eiowzz","abcczz"]\n10'
#
# This problem is an interactive problem new to the LeetCode platform.
# 
# We are given a word list of unique words, each word is 6 letters long, and
# one word in this list is chosen as secret.
# 
# You may call master.guess(word) to guess a word.  The guessed word should
# have type string and must be from the original list with 6 lowercase
# letters.
# 
# This function returns an integer type, representing the number of exact
# matches (value and position) of your guess to the secret word.  Also, if your
# guess is not in the given wordlist, it will return -1 instead.
# 
# For each test case, you have 10 guesses to guess the word. At the end of any
# number of calls, if you have made 10 or less calls to master.guess and at
# least one of these guesses was the secret, you pass the testcase.
# 
# Besides the example test case below, there will be 5 additional test cases,
# each with 100 words in the word list.  The letters of each word in those
# testcases were chosen independently at random from 'a' to 'z', such that
# every word in the given word lists is unique.
# 
# 
# Example 1:
# Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
# 
# Explanation:
# 
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6
# matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
# 
# We made 5 calls to master.guess and one of them was the secret, so we pass
# the test case.
# 
# 
# Note:  Any solutions that attempt to circumvent the judge will result in
# disqualification.
# 
#
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

from collections import Counter
import copy, functools

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        # def similarity(word1, word2):
        #     count = 0
        #     for i in range(6):
        #         if word1[i] == word2[i]:
        #             count += 1
        #     return count

        # def heuristic(target, words):
        #     freq = Counter([0, 1, 2, 3, 4, 5])
        #     for k in freq.keys():
        #         freq[k] += 1

        #     for w in words:
        #         if w != target:
        #             s = similarity(w, target)
        #             freq[s] += 1

        #     return functools.reduce(lambda x, y: x * y, freq.values())

        # def pick_word(words):
        #     values = [0] * len(words)

        #     for i in range(len(words)):
        #         values[i] = heuristic(words[i], words)

        #     argmax = 0
        #     max_v = 0
        #     for i in range(len(values)):
        #         if max_v < values[i]:
        #             argmax = i 
        #             max_v = values[i]
        #     return words[argmax]

        # words = copy.copy(wordlist)
        # for i in range(10):
        #     cur_word = pick_word(words)
        #     sim = master.guess(cur_word)
        #     if sim == 6:
        #         return
        #     words = list(filter(lambda w: w != cur_word and sim == similarity(w, cur_word), words))



        def pair_matches(a, b):
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word():
            counts = [[0 for _ in range(26)] for _ in range(6)]
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord('a')] += 1

            best_score = 0
            for word in candidates:
                score = 0 
                for i, c in enumerate(word):
                    score += counts[i][ord(c) - ord('a')]
                if score > best_score:
                    best_score = score
                    best_word = word

            return best_word

        candidates = wordlist[:]
        while candidates:
            s = most_overlap_word()
            matches = master.guess(s)

            if matches == 6:
                return

            candidates = [w for w in candidates if pair_matches(s, w) == matches]

