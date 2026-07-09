#https://leetcode.com/problems/redundant-connection/

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n=len(edges)

        parent=list(range(n+1))

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            
            return parent[x]

        def union(a,b):
            pa=find(a)
            pb=find(b)

            if pa==pb:
                return False
            
            parent[pb]=pa
            return True
            
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        

