#https://leetcode.com/problems/number-of-operations-to-make-network-connected/
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        parent=list(range(n))

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
                
        extra=0
        for u,v in connections:
            if not union(u,v):
                extra+=1
        
        components=0
        for i in range(n):
            if find(i)==i:
                components+=1
        
        need=components-1

        if extra>=need:
            return need
        
        return -1

