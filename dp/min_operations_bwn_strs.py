#https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n=len(word1),len(word2)

        #dp=[[0]*(n+1) for _ in range(m+1)]
        prev=[0]*(n+1)
        ans=0

        for i in range(1,m+1):
            curr=[0]*(n+1)
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    #dp[i][j]=1+dp[i-1][j-1]
                    curr[j]=1+prev[j-1]
                else:
                    #dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                    curr[j]=max(prev[j],curr[j-1])

                #ans=max(ans,dp[i][j])
                ans=max(ans,curr[j])
            
            prev=curr
        

        return m+n-2*ans   
        #insertions --> m-ans
        #deletions --> n-ans
        #watch https://youtu.be/yMnH0jrir0Q?si=QJV35tO8FDSS3iUO

