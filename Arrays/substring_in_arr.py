#https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/
class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count=0
        for bro in patterns:
            if bro in word:
                count+=1
        return count