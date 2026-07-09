#https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
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
        

        for u,v in edges:
            union(u,v)
        
        return find(source)==find(destination)