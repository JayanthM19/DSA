#https://leetcode.com/problems/number-of-provinces/

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)

        parent=list(range(n))

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            
            return parent[x]

        def union(a,b):
            pa=find(a)
            pb=find(b)

            if pa!=pb:
                parent[pb]=pa
        
        

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    union(i,j)

        cnt=0
        for i in range(n):
            if find(i)==i:
                cnt+=1
        
        return cnt
