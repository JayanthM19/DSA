#https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """

        # return len(s)-len(longest palindrome in string)
        s2=s[::-1]

        m,n=len(s),len(s2)

        # dp=[[0]*(m+1) for _ in range(n+1)]
        prev=[0]*(n+1)

        for i in range(1,m+1):
            curr=[0]*(n+1)
            for j in range(1,n+1):
                if s[i-1]==s2[j-1]:
                    # dp[i][j]=1+dp[i-1][j-1]
                    curr[j]=1+prev[j-1]
                else:
                    # dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    curr[j]=max(prev[j],curr[j-1])
            
            prev=curr

        # return m-dp[m][n]
        return m-curr[n]