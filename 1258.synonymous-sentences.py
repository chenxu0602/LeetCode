#
# @lc app=leetcode id=1258 lang=python3
#
# [1258] Synonymous Sentences
#
# https://leetcode.com/problems/synonymous-sentences/description/
#
# algorithms
# Medium (61.05%)
# Likes:    45
# Dislikes: 22
# Total Accepted:    2.4K
# Total Submissions: 3.9K
# Testcase Example:  '[["happy","joy"],["sad","sorrow"],["joy","cheerful"]]\n' + '"I am happy today but was sad yesterday"'
#
# Given a list of pairs of equivalent words synonyms and a sentence text,
# Return all possible synonymous sentences sorted lexicographically.
# 
# Example 1:
# 
# 
# Input:
# synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
# text = "I am happy today but was sad yesterday"
# Output:
# ["I am cheerful today but was sad yesterday",
# ​​​​​​​"I am cheerful today but was sorrow yesterday",
# "I am happy today but was sad yesterday",
# "I am happy today but was sorrow yesterday",
# "I am joy today but was sad yesterday",
# "I am joy today but was sorrow yesterday"]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= synonyms.length <= 10
# synonyms[i].length == 2
# synonyms[0] != synonyms[1]
# All words consist of at most 10 English letters only.
# text is a single space separated sentence of at most 10 words.
# 
# 
#

# @lc code=start
from collections import defaultdict, deque

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:

        graph = defaultdict(dict)
        bfs = deque([text])
        ans = set()
        for k, v in synonyms:
            graph[k][v] = 1
            graph[v][k] = 1

        while bfs:
            curT = bfs.popleft()
            ans.add(curT)
            words = curT.split()
            for i, w in enumerate(words):
                if w in graph:
                    for newW in graph[w]:
                        newS = " ".join(words[:i] + [newW] + words[i+1:])
                        if newS not in ans:
                            bfs.append(newS)

        return sorted(list(ans))
        
# @lc code=end

