#https://leetcode.com/problems/valid-mountain-array/

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3:
            return False

        i,j,n = 0,len(arr)-1,len(arr)

        while i+1<n and arr[i]<arr[i+1] :
            i+=1
        
        while j>0 and arr[j-1]>arr[j]:
            j-=1
        
        return 0<i==j<n-1
        
        
            
                
            


