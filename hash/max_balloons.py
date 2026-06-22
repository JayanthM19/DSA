#https://leetcode.com/problems/maximum-number-of-balloons/description

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq={}

        for s in text:
            freq[s]=freq.get(s,0)+1
        
        return min(
            freq.get('b',0),
            freq.get('a',0),
            freq.get('l',0)//2,
            freq.get('o',0)//2,
            freq.get('n',0)
            
        )

            


        