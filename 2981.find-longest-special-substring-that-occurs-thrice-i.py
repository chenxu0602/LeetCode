#
# @lc app=leetcode id=2981 lang=python3
#
# [2981] Find Longest Special Substring That Occurs Thrice I
#

# @lc code=start
from collections import defaultdict
from itertools import groupby

class Solution:
    def maximumLength(self, s: str) -> int:

        # We parse the the string into a list of strings of one character. (For example: 'aabeee' --> ['aa', 'b', 'eee'])
        # We increment a dict to track the beautiful strings; the trick here is to account for all substrings in a particular beautiful string, as there are also shorter beautiful strings in the same character.
        # We filter the dict keys for all beautiful strings that occur three times and return the maximum length of all such beautiful strings.

        d = defaultdict(int)
        subs = [''.join(sub) for _, sub in groupby(s)]

        for sub in subs:
            d[sub] += 1
            if len(sub) > 1:
                d[sub[1:]] += 2
            if len(sub) > 2:
                d[sub[2:]] += 3

        return max(map(len, filter(lambda x: d[x] > 2, d.keys())), default=-1)
        
# @lc code=end

