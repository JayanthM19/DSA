#https://leetcode.com/problems/sort-an-array/
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums.sort()
        # return nums

        
#MergeSort
        def mergesort(arr):
            l=len(arr)

            if l>1:
                m=l//2
                L=arr[:m]
                R=arr[m:]

                mergesort(L)
                mergesort(R)

                i=j=k=0

                while i<len(L) and j<len(R):
                    if L[i]<R[j]:
                        arr[k]=L[i]
                        i+=1
                    else:
                        arr[k]=R[j]
                        j+=1
                    k+=1
                
                arr[k:]=L[i:]+R[j:]
            
            return arr
        
        mergesort(nums)

        return nums
