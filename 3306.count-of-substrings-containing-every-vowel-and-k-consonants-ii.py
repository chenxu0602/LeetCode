#
# @lc app=leetcode id=3306 lang=python3
#
# [3306] Count of Substrings Containing Every Vowel and K Consonants II
#

# @lc code=start
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = 'aeiou'

        def count_at_least_m_consonants(k: int) -> int:
            vowels_cnt = Counter()
            num_consonants = res = l = r = 0
            while r < n:
                if word[r] in vowels: 
                    vowels_cnt[word[r]] += 1
                else:
                    num_consonants += 1

                while num_consonants >= k and len(vowels_cnt) == len(vowels):
                    if word[l] in vowels: vowels_cnt[word[l]] -= 1
                    else: num_consonants -= 1

                    if vowels_cnt[word[l]] == 0: del vowels_cnt[word[l]]
                    l += 1

                res += l
                r += 1
            return res

        return count_at_least_m_consonants(k) - count_at_least_m_consonants(k + 1)

        
# @lc code=end

