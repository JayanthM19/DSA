#https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        #s1 is given string whereas s2 is reverse of given string
        m=len(s)
        s2=s[::-1]
        n=len(s2)

        # dp=[[0]*(m+1) for _ in range(n+1)]

        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if s[i-1]==s2[j-1]:
        #             dp[i][j]=1+dp[i-1][j-1]
        #         else:
        #             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        # return dp[m][n]

        prev=[0]*(n+1)

        for i in range(1,m+1):
            curr=[0]*(n+1)
            for j in range(1,n+1):
                if s[i-1]==s2[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(prev[j],curr[j-1])
            
            prev=curr
        
        return curr[n]



        