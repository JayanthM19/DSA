#https://leetcode.com/problems/search-a-2d-matrix/
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # if target<matrix[0][0]:
        #     return False
        
        # m,n=len(matrix),len(matrix[0])

        # k=m-1

        # for i in range(m):
        #     if matrix[i][0]>target:
        #         k=i-1
        #         break

        # for j in range(n):
        #     if matrix[k][j]==target:
        #         return True
        
        # return False
        
        m,n=len(matrix),len(matrix[0])

        low=0
        high=m*n-1

        while low<=high:

            mid=(low+high)//2

            row=mid//n
            col = mid%n

            if matrix[row][col]==target:
                return True
            
            elif matrix[row][col]<target:
                low=mid+1
            else:
                high=mid-1
        
        return False