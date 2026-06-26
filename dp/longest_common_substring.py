#https://leetcode.com/problems/maximum-length-of-repeated-subarray/


class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m,n=len(nums1),len(nums2)

        # dp=[[0]*(n+1) for _ in range(m+1)]
        # ans=0

        # for i in range(1,m+1):
        #     for j in range(1,n+1):

        #         if nums1[i-1]==nums2[j-1]:
        #             dp[i][j]=1+dp[i-1][j-1]
        #             ans=max(ans,dp[i][j])

        # return ans

        prev=[0]*(n+1)   #declare with j loop variable 
        
        ans=0

        for i in range(1,m+1):
            curr=[0]*(n+1)
            for j in range(1,n+1):

                if nums1[i-1]==nums2[j-1]:
                    curr[j]=1+prev[j-1]
                    ans=max(ans,curr[j])
            
            prev=curr

        return ans
        

        