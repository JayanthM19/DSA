#
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # i,j,n=0,len(arr)-1,len(arr)

        # while i+1<n and arr[i]<arr[i+1]:
        #     i+=1
        
        # while j>0 and arr[j-1]>arr[j]:
        #     j-=1
        
        # return i

#Another Solution
        n=len(arr)
        low,high = 0,n-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid]<arr[mid+1]:
                low=mid+1
            elif arr[mid]>arr[mid+1]:
                high=mid
        

        return low