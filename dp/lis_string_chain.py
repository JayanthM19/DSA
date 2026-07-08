#https://leetcode.com/problems/longest-string-chain/

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)

        n=len(words)

        dp=[1]*n

        def ispredecessor(small,large):
            if len(small)+1!=len(large):
                return False
            
            i,j=0,0
            while i<len(small) and j<len(large):
                if small[i]==large[j]:
                    i+=1
                    j+=1
                else:
                    j+=1
                
            return i==len(small)
        
        for i in range(n):
            for j in range(i):
                if ispredecessor(words[j],words[i]):
                    dp[i]=max(1+dp[j],dp[i])

        return max(dp) 