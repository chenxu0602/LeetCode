#
# @lc app=leetcode id=2227 lang=python3
#
# [2227] Encrypt and Decrypt Strings
#

# @lc code=start
from collections import Counter

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.enc = {k: v for k, v in zip(keys, values)}
        self.decrypt2 = Counter(self.encrypt(w) for w in dictionary).__getitem__

    def encrypt(self, word1: str) -> str:
        return "".join(self.enc.get(c, '#') for c in word1)

    def decrypt(self, word2: str) -> int:
        return self.decrypt2(word2)
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
# @lc code=end

