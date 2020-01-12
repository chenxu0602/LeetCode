#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (29.59%)
# Likes:    1486
# Dislikes: 82
# Total Accepted:    138.6K
# Total Submissions: 453.9K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
# 
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
# 
# 
# 
# Example:
# 
# 
# Input: 
# board = [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# 
# Output: ["eat","oath"]
# 
# 
# 
# 
# Note:
# 
# 
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
# 
# 
#

# @lc code=start

from collections import defaultdict

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        for word in words:
            node = trie
            for l in word:
                node = node[l]
            node['$'] = word

        m, n = len(board), len(board[0])

        res = []

        def dfs(r, c, parent):
            letter = board[r][c]
            child = parent[letter]

            word_match = child.pop('$', False)
            if word_match:
                res.append(word_match)

            board[r][c] = '#'

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in child:
                    dfs(nr, nc, child)

            board[r][c] = letter

            if not child:
                parent.pop(letter)

        for r in range(m):
            for c in range(n):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return res
        
# @lc code=end

