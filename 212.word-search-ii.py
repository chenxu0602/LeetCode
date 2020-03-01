#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (31.83%)
# Likes:    1780
# Dislikes: 89
# Total Accepted:    161.8K
# Total Submissions: 507.4K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' + '["oath","pea","eat","rain"]'
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
from functools import reduce

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        for word in words:
            reduce(dict.__getitem__, word, trie)['$'] = word

        m, n = len(board), len(board[0])

        res = []

        def dfs(r, c, parent):
            letter = board[r][c]
            children = parent[letter]

            word_match = children.pop("$", False)
            if word_match:
                res.append(word_match)

            board[r][c] = '#'

            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in children:
                    dfs(nr, nc, children)

            board[r][c] = letter

            if not children:
                parent.pop(letter)

        for r in range(m):
            for c in range(n):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return res
        
# @lc code=end

