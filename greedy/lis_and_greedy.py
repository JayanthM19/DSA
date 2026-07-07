#https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # pairs.sort(key = lambda x:x[0])

        # n=len(pairs)
        # dp=[1]*n

        # for i in range(n):
        #     for j in range(i):
        #         if pairs[i][0]>pairs[j][1]:
        #             dp[i]=max(dp[i],1+dp[j])
        
        # return max(dp)


        pairs.sort(key=lambda x:x[1])

        count=1
        end=pairs[0][1]

        for i in range(1,len(pairs)):
            if pairs[i][0]>end:
                count+=1
                end=pairs[i][1]
        
        return count

