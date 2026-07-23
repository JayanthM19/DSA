#https://leetcode.com/problems/split-strings-by-separator/
class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        res=[]
        for i in words:
            parts=i.split(separator)

            for p in parts:
                if p!="":
                    res.append(p)
            
        return res