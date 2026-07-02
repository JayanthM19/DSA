#https://leetcode.com/problems/longest-palindrome/description/
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        freq={}
        for hello in s:
            freq[hello]=freq.get(hello,0)+1
        
        odd=False

        for key,val in freq.items():
            if val%2==0:
                total+=val
            
            else:
                total+=val-1
                odd=True
        
        if odd:
            total+=1
        
        return total